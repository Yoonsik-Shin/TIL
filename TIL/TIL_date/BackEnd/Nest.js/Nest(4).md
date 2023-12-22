# Nest (4)

```bash
$ yarn add bcrypt
$ yarn add -D @types/bcrypt
```



## 1️⃣ 로그인

### JWT  방식

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

​    

### 세션방식

```bash
$ npm install @nestjs/passport passport passport-local express-session
$ npm install -D @types/passport-local @types/express-session
```

```ts
// main.ts
import * as session from 'express-session';
import * as passport from 'passport';

async function bootstrap() {	
    const app = await NestFactory.create(AppModule);
    app.use(
    	session({
            secret: '시크릿키',
            resave: false,
            saveUninitialized: false,
            cookie: { maxAge: 1000 * 60 * 60 * 30 },
    	}),
    );
    
    // passport 초기화 및 세션 저장소 초기화
    app.use(passport.initialize());
  	app.use(passport.session());
    await app.listen(8000);
}
```



​     

---

## 2️⃣ 파일업로드

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

​    

```bash
$ yarn add @aws-sdk/client-s3
```





---

## 3️⃣ socket 통신

- 프로토콜이 `ws`이면 `gateway`(게이트웨이)로 부터 요청을 받음

```bash
$ nest g gateway chat
```

- 게이트웨이는 컨트롤러와 유사하지만, 프로바이더이므로 모듈의 providers에 등록해줘야함

```ts
@Module({
    providers: [ChatGateway]
})
```





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

>  `@WebSocketGateway()`

- 게이트웨이 설정을 위한 데코레이터
- 내부적으로는 socket.io 서버를 생성하는 것과 같아, 생성시 옵션도 동일하게 줄 수 있음

```ts
@WebSocketGateway(port, options)
```

> `@WebSocketServer()`

- 웹소켓 서버 인스턴스에 접근하는 데코레이터
- 사용자가 직접 웹소켓 서버의 인스턴스를 생성하는 것이 아니기 때문에 이 데코레이터를 사용해야함

> `@SubscribeMessage('이벤트명')`

- 이벤트를 구독하는 리스너
- 이 데코레이터가 붙는 메서드는 인수로 `socket(client)`과 `data(payload)`를 가짐
- 클라이언트에서 해당 이벤트로 데이터가 전송되면 그 데이터는 `data` 인수에 담김
- `socket` 인수의 타입은 `Socket`이고, 이는 웹소켓 연결에 대한 인스턴스를 받음 

```ts
import { SubscribeMessage, WebSocketGateway } from '@nestjs/websockets';
import { Server, Socket } from 'socket.io';

@WebSocketGateway()
export class ChatGateway {
  @SubscribeMessage('message')
  handleMessage(client: Socket, payload: any): string {
    return ...;
  }
}
```

- 만약 인수중 하나라도 생략하고 싶다면 각각 속성에 맞는 매개변수 데코레이터를 사용해야함

```ts
import { Socket } from 'socket.io'
import { MessageBody } from '@nestjs/websockets';

// socket 인수를 생략한 경우
@SubscribeMessage('message')
handleMessage(
	@MessageBody() data: any
) {}

// data 인수를 생략한 경우
import { Socket } from 'socket.io'
import { ConnectedSocket } from '@nestjs/websockets';

@SubscribeMessage('message')
handleMessage(
	@ConnectedSocket() socket: Socket
) {}
```

`emit()`

- 클라이언트 전체에 메시지를 보냄
- 첫 번째 인수는 이벤트명
- 두번째 인수는 클라이언트로 보내주는 데이터

> namespace : 영역분리 (chatting, stock)

- 네임스페이스로 지정된 곳에만 이벤트를 발생시키고 메시지를 전송함 (멀티플렉싱)
- 



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





- 
