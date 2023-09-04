# Nest (4)

## JWT 로그인

```bash
$ npm install @nestjs/passport passport passport-local
$ npm install -D @types/passport-local
```

```typescript
// jwt.guard.ts
import { AuthGuard } from '@nestjs/passport'

@Injectable()
export class JwtAuthGuard extends AuthGuard('jwt') {} // AuthGuard는 strategy를 자동으로 실행해줌
```

```typescript
// jwt.strategy.ts
import { ExtractJwt, Strategy } from 'passport-jwt'
import { PassportStrategy } from '@nestjs/passport'

@Injectable()
export class JwtStrategy extends PassPortStrategy(Strategy) {
  constructor(private readonly testRepository: TestRepository) {
    super({
      jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),  // request에서 jwt토큰 추출
      secretOrKey: '시크릿키',  // 유출되면 안됨
      ignoreExpiration: false,  // 만료기간 무시여부
    })
  }
  
  async validate(payload: Payload) {
    const user = await this.TestRepository.findUserByIdWithoutPassword(payload.sub)
    if (user) return user  // request.user = user
    
    throw new UnauthorizedException()
  }
}

type Payload = {
  email: string
  sub: string
}

// test.Repository.ts
...
async findUserByIdWithoutPassword(id: string): Promise<Test | null> {
  const user = await this.testModel.findById(id),select('-password')
	return user
}
```

```typescript
// auth.module.ts
import { PassportModule } from '@nestjs/passport'
import { JwtModule } from '@nestjs/jwt'
import { JwtStrategy } from './jwt.strategy'

@Module({
  imports: [
    PassportModule.register({
      defaultStrategy: 'jwt',
      session: false  // 세션쿠키 사용여부
    }),
    JwtModule.register({
      secret: '시크릿키',
      signOptions: { expiresIn: '1y' }
    })
  ],
  providers: [
    AuthService,
    JwtStrategy
  ]
})
```

```typescript
// auth.service.ts
@Injectable()
export class AuthService {
  constructor(private readonly testRepository: TestRepository) {}
  
  async login(data: LoginRequestDto) {
  	const { email, password } = data
    
    // email 일치여부
    const user = await this.TestRepository.findUserByEmail(email)
    if (!user) throw new UnauthorizedException('이메일과 비밀번호를 확인해주세요.')
    
    // password 일치여부
    const isPasswordValidated: boolean = await bcrypt.compare(password, user.password)
    if (!isPasswordValidated) throw new UnauthorizedException('이메일과 비밀번호를 확인해주세요.')
    
    const payload = { email: email, sub: user.id }
    
    return {
      token: this.jwtService.sign(payload)
    }
  }
}
```



순환참조모듈

- 모듈간 순환 종속성을 해결하기 위해 `forwardRef()`함수 사용

```typescript
@Module({
  imports: [
    forwardRef(() => TestModule)
  ]
})
```

​    

### 커스텀 데코레이터

```typescript
// user.decorator.ts
import { createParamDecorator, ExecutionContext } from '@nestjs/common';

export const CurrentUser = createParamDecorator(
  (data: unknown, ctx: ExecutionContext) => {
    const request = ctx.switchToHttp().getRequest();
    return request.user;
  },
);
```



## 파일업로드

- express용 multer 미들웨어 사용
- http post요청을 통해 multipart/form-data 형식의 데이터를 처리

```bash
$ npm install -D @types/multer
$ yarn add -D @types/multer
```

```typescript
// main.ts
import * as path from 'path'
import { NestExpressApplication } from '@nestjs/platform-express'

async function bootstrap() {
  const app = await NestFactory.create<NestExpressApplication>(AppModule)
  ...
	app.useStaticAssets(path.join(__dirname, './common', 'uploads'), {
  	prefix: '/media'
	})
  ...
}

```

```typescript
// test.module.ts
@Module({
  imports: [
    MulterModule.register({
      dest: './upload'
    })
  ]
})
```

```typescript
// commons/utils/multer.options.ts
import * as multer from 'multer'
import * as path from 'path'
import * as fs from 'fs'
import { MulterOptions } from '@nestjs/platform-express/multer/interfaces/multer-options.interface'

// 새로운 upload폴더생성
const createFolder = (folder: string) => {
	try {  // upload 폴더생성
    console.log('💾 새로운 폴더를 생성 후 업로드합니다.')
		fs.mkdirSync(path.join(__dirname, '..', `uploads`))
  } catch (error) {
		console.log('이미 폴더가 존재합니다.')
	}
  
	try {  // upload안에 폴더생성
 		console.log(`💾 Create a ${folder} uploads folder...`)
		fs.mkdirSync(path.join(__dirname, '..', `uploads/${folder}`))
	} catch (error) {
		console.log(`The ${folder} folder already exists...`)
  }
}

const storage = (folder: string): multer.StorageEngine => {
	createFolder(folder)
	return multer.diskStorage({
		// 저장 위치 지정    
		destination(req, file, cb) { 
			const folderName = path.join(__dirname, '..', `uploads/${folder}`)
    	cb(null, folderName)
 		},
    // 저장할 파일명 지정
 		filename(req, file, cb) {
    	const ext = path.extname(file.originalname)
      const fileName = `${path.basename(file.originalname, ext)}${Date.now()}${ext}`
      cb(null, fileName)
 		},
  })
}

export const multerOptions = (folder: string) => {
  const result: MulterOptions = { storage: storage(folder),}
	return result
}
```

mkdirSync : 폴더를 만드는 명령

path.join(__dirname) : 현재폴더를 의미

path.join(__dirname, '..') : 현재폴더의 부모폴더

path.join(__dirname, '..', 'uploads') : 현재폴더의 부모폴더에 uploads라는 폴더를 만들어라

path.extname('index.html') : 확장자 추출 ('.html')



### 단일 파일

```typescript
// controller.ts
import { UploadedFile } from '@nestjs/common'
import { FileInterceptor } from '@nestjs/platform-express'
...
@Post('upload')
@UseInterceptors(FileInterceptor('file'))
uploadFile(@UploadedFile() file: Express.Multer.File) {
  
}
```

FileInterceptor / FilesInterceptor 의 인자

- fieldName : 프론트엔드에서 전달하는 필드명
- maxCount : FilesInterceptor에서만 사용가능, 업로드가능한 파일수 지정
- options



### 다중파일

```typescript
// controller.ts
import { UploadedFiles } from '@nestjs/common'
import { FilesInterceptor } from '@nestjs/platform-express'

@Post('upload')
@UseInterceptors(FilesInterceptor('file', 10, multerOptions('저장할폴더명')))
@UseGuards(JwtAuthGuard)
uploadFile(
  @UploadedFiles() files: Array<Express.Multer.File>
  @CurrentUser() user: Test
) {
  return this.testService.uploadImage(user, files)
}
```

```typescript
// service.ts
...
async uploadImage(user: Test, files: Express.Multer.File[]) {
  const fileName = `test/${files[0].filename}`
  const newImageUser = await this.testRepository.findByIdUpdateImage(user.id, fileName)
  return newImageUser
}
```

```typescript
// repository.ts
...
async findByIdUpdateImage(id: string, fileName: string) {
  const user = await this.testModel.findById(id)
  user.imgUrl = `http://~~/media/${fileName}`
  const newImageUser = await user.save()
  retunr newImageUser.readOnlyData
}
```



## socket 통신

```bash
$ npm install @nestjs/websockets @nestjs/platform-socket.io
$ yarn add @nestjs/websockets @nestjs/platform-socket.io
```

```typescript
// chats.module.ts
import { Module } from '@nestjs/common';
import { ChatsGateway } from './chats.gateway';

@Module({
  providers: [ChatsGateway],
})
export class ChatsModule {}

// app.module.ts
@Module({
  imports: [
    ...
    ChatsModule,
    ...
  ]
})
```

```typescript
// chats.gateway.ts
import { Socket } from 'socket.io'
import { 
	ConnectedSocket,
  MessageBody,
  SubscribeMessage,
  WebSocketGateway
} from '@nestjs/websockets'

@WebSocketGateway(80, { namespace: 'chattings' })
export class ChatsGateway {
  @SubscribeMessage('메시지명(From Front)')
  handleNewUser(
  	@MessageBody() username: string,
    @ConnectedSocket() socket: Socket
  ) {
  	console.log(username)
    console.log(socket.id)
    socket.emit('메시지명(To Front)' ,`반갑습니다 ${username}`)
    socket.broadcast.emit('메시지명(To Front)', `보낼내용`) // 연결된 모든 socket에게 데이터 전송
    return username
  }
}
```

namespace : 영역분리 (chatting, stock)



생명주기 hooks

- `OnGatewayInit`

```typescript
export class ChatsGateway implements OnGatewayInit {
  afterInit() {}  // constructor 다음으로 실행됨
```

- `OnGatewayConnection` 

```typescript
export class ChatsGateway implements OnGatewayConnection {
  handleConnection(@ConnectedSocket() socket: Socket) {}  // 클라이언트와 연결되면 실행됨
```

- `OnGatewayDisconnet`

```typescript
export class ChatsGateway implements OnGatewayDisconnet {
  handleDisconnect(@ConnectedSocket() socket: Socket) {}  // 클라이언트와의 연결이 종료되면 실행됨
```

