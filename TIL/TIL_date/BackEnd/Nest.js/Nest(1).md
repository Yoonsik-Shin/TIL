# Nest (1)

​    

설치

```bash
# CLI 설치
$ npm install -g @nestjs/cli
$ yarn add -g @nestjs/cli

# 프로젝트 시작
$ nest new project-name
```



```bash
$ nest g mo 모듈명  # Module 파일 자동 생성
$ nest g co 컨트롤러명  # Controller 파일 자동 생성
$ nest g middleware 미들웨어명  # Middleware 파일 자동 생성
```



캡슐화

module의 providers에 사용하는 Service를 모두 추가해주는 방식

사용하는 서비스가 많아지면 추가할 값들이 너무 많아짐

```typescript
@Module({
  imports: [AAAModule, BBBModule, CCCModule],
  ...
  providers: [
     AAAService,
     BBBService,
     CCCService,
     DDDService
  ]
})
```

해당 module에서 export해준 Service는 다른 모듈에서 사용할 때, providers에 추가할 필요없이 사용가능

```typescript
@Module({
  providers: [BBBService],
  exports: [BBBSerive]  ✔️✔️ 
})
export BBBModule{}
```

```typescript
@Module({
  imports: [AAAModule, BBBModule, CCCModule],  // 모듈이 import되어있다면 Service 생략가능
  providers: [
    AAAService,
    // 작성하지 않았지만 BBB Module에서 export된 Service인 BBBSerive를 이용할 수 있음
  ]
})
export class AAAModule {}
```



CORS

```typescript
// main.ts
...
app.enableCors({
  origin: true,  // 개발시에만 true, 배포시에는 특정 url만 사용하도록 변경
 	credentials: true
})
```





## middleware

- 라우트 핸들러 이전에 호출되는 함수
- Express의 미들웨어와 동일
- DI 가능

```typescript
// logger.middleware.ts
import { Injectable, NestMiddleware } from '@nestjs/common'
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  private logger = new Logger('HTTP')
  
  use(
  	req: Request,
  	res: Response,
  	next: NextFunction
  ) {
    // 로직
    this.logger.log(req)
  	next()    
  }
}
```



```typescript
import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { LoggerMiddleware } from './common/middleware/logger.middleware';

@Module({
  imports: [AAAModule],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(LoggerMiddleware)
      .forRoutes('*');  // 전체 엔드포인트에서 실행 
  }
}
```



## 예외처리

Exception filters

```typescript
import { HttpStatus } from '@nestjs/common'

@Get()
aaa() {
  throw new HttpException({
    status: HttpStatus.FORBIDDEN,
    error: '에러메시지'
  }, HttpStatus.FORBIDDEN)
}
```

```typescript
// 내장 HTTP Exception들
BadRequestException
UnauthorizedException
NotFoundException
ForbiddenException
NotAcceptableException
RequestTimeoutException
ConflictException
GoneException
HttpVersionNotSupportedException
PayloadTooLargeException
UnsupportedMediaTypeException
UnprocessableEntityException
InternalServerErrorException
NotImplementedException
ImATeapotException
MethodNotAllowedException
BadGatewayException
ServiceUnavailableException
GatewayTimeoutException
PreconditionFailedException
```

- 커스텀 예외처리 필터

```typescript
// http-exception.filter.ts
import { ExceptionFilter, Catch, ArgumentsHost, HttpException } from '@nestjs/common';
import { Request, Response } from 'express';

@Catch(HttpException)
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp()
    const response = ctx.getResponse<Response>()
    const request = ctx.getRequest<Request>()
    const status = exception.getStatus()
    const error = exception.getResponse()

    response.status(status).json({
      statusCode: status,
      timestamp: new Date().toISOString(),
      path: request.url,
      error
    });
  }
}
```



filter 각각 적용, 

@UseFilters() 데코레이터 사용

```typescript
// test.controller.ts
@Post()
@UseFilters(HttpExceptionFilter)
test(@Body() testDto: TestDto) {
  throw new UnauthorizedException()
}
```



전역 적용

- main.ts에 적용

```typescript
async function bootstrap() {
  ...
  app.useGlobalFilters(new HttpExceptionFilter())
  ...
}
```



## Pipes

- 클라이언트 요청에서 들어오는 데이터를 유효성 검사 및 변환을 수행해 서버가 원하는 데이터를 얻을 수 있도록 도와주는 클래스
- 사용사례
  - 변환 : 입력데이터를 원하는 형식으로 변환
  - 유효성 검사 : 입력데이터 평가, 데이터가 올바르지 않으면 예외 발생

```typescript
// controller.ts
@Get(':id')
getData(@Param('id', ParseIntPipe) param) {
  
}
```



```bash
# 내장 파이프들
ValidationPipe
ParseIntPipe
ParseFloatPipe
ParseBoolPipe
ParseArrayPipe
ParseUUIDPipe
ParseEnumPipe
DefaultValuePipe
ParseFilePipe
```



## Interceptors

`@Injectable` 데코레이터 사용, DI 가능

핵심기능에서 재사용이 가능한 부분들을 하나의 모듈로 묶어놓은 것

```typescript
// logging.interceptor.ts
import { Injectable, NestInterceptor, ExecutionContext, CallHandler } from '@nestjs/common';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
    console.log('Before...')  // 컨트롤러 이전에 실행됨 (pre-controller)

    return next.handle().pipe(  // 컨트롤러 이후에 실행됨 (post-controller)
        map((data) => ({  // 컨트롤러의 데이터
          success: true,
          data
        }))
      );
  }
}
```





Schema-First : typeDefs를 직접 작성하는 방식

Code-First : 타입스크립트가 적용된 코드를 작성하면 자동으로 Schema 생성 (Nest.js에서 사용됨)



injectable

인젝션 스코프

1. 싱글톤 : new 한 번만 실행
2. Request 스코프 : 매 요청마다 new 실행
3. Transient 스코프 : 매 주입마다 new 실행

```typescript
import { Injectable, Scope } from '@nestjs/common'

// 아예 안쓰면 싱글톤이 default
@Injectable({ scope: Scope.DEFAULT })  // 싱글톤
@Injectable({ scope: Scope.REQUEST })  // Request
@Injectable({ scope: Scope.TRANSIENT })  // Transient
```



```typescript
import { Body, Controller, Get, Param, Req } '@nestjs/common'

@Controller('/')
export class TestController {
  @Get('test/:id')
  testHello(
 		@Req() req: Request,
  	@Body() fetchBodyDto,
  	@Param() param
  ): string {
    return this.testService.fetchHello()
  }
}
```

@Body에는 Dto를 활용



Graphql

```bash
$ npm install @nestjs/graphql @nestjs/apollo graphql apollo-server-express
$ yarn add @nestjs/graphql @nestjs/apollo graphql apollo-server-express
```



RestAPI와 다른점

Controller 대신 Resolver 사용

@Get, @Post, @Put, @Patch, @Delete 대신 @Query, @Mutation 사용

타입 적용방식 조금 다름

```typescript
// Test.resolver.ts
import { Args, Mutation, Query, Resolver } from '@nestjs/graphql'

@Resolver()
export class TestResolver {
  constructor(private readonly testService: TestService) {}
  
  @Query(() => String, { nullable: true })
  testHello(): string {
    return this.testService.startTest()
  }
  
  @Mutation(() => [TestRepo])
  testPost(
  	// 하나씩 사용하기보다는 DTO를 활용
  	// @Args('test1') test1: string,
  	// @Args('test2') test2: string,
  	// @Args({ name: 'test3', nullable: true }) test3: string
  	@Args("createTestInput") createTestInput: CreateTestInput
  ): TestRepo[] {
   	return this.testService.createTest({ createTestInput })
  }
}
```



DTO : Data Transfer Object

```typescript
// /dto/createTest.input.ts
import { Field, InputType } from '@nestjs/graphql'

@InputType() 
export class CreateTestInput {
  @Field(() => String)
  test1: string
  
  @Field(() => String)
  test2: string
  
  @Field(() => String)
  test3: string
}
```



module 파일에서 controllers 항목 대신, providers에 Resolver 작성

```typescript
@Module({
  providers: [
    TestResolver,
    TestService
  ]
})
```





Graphql 초기설정

```typescript
import { ApolloDriver, ApolloDriverConfig } from '@nestjs/apollo'
import { GraphQLModule } from '@nestjs/graphql'

@Module({
  imports: [
    GraphQLModule.forRoot<ApolloDriverConfig>({
      driver: ApolloDriver,
      // 자동으로 생성될 스키마 파일 저장 위치
      autoSchemaFile: "src/commons/graphql/schema.gql"  
    })
  ]
})
export class AppModule {}
```



entities

DB는 단수형 명사 사용

테이블의 schema라고 생각하면 됨

```typescript
// test.entities.ts
import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm'

@Entity()  // Mysql
@ObjectType()  // Graphql
class Test { 
  @PrimaryGeneratedColumn('')  // Mysql ('uuid' | 'increment')
  @Field(() => Int)  // Graphql
	userName: string
  
  @Column()  // Mysql
  @Field(() => String)  // Graphql
  email: string
  
  @Column()  // Mysql
  @Field(() => String)  // Graphql
  password: string
}
```



mysql 초기설정

```typescript
@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: "mysql",
      host: "localhost",  // Docker 사용시 네임리졸류션 사용
      port: 3306,
      username: "",  // 로그인 유저
      password: "",  // 로그인 비밀번호
      database: "",  // DB이름, DB가 존재해야 정상적으로 연결됨
      entities: [Test],  // entity 파일
      logging: true
    })
  ]
})
```



configuration

```typescript
// app.module.ts
import { ConfigModule } from '@nestjs/config'

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,  // 전역에서 사용가능
    })
  ]
})
```

```bash
# .env
TEST_URI=https://test.com
```

```typescript
// 환경변수 사용
const BASE_URI = process.env.TEST_URI
```





mongodb / mongoose

```bash
$ npm install @nestjs/mongoose mongoose
$ yarn add @nestjs/mongoose mongoose
```

```typescript
// app.module.ts
import { MongooseModule } from '@nestjs/mongoose'
import { ConfigModule } from '@nestjs/config'

@Module({
  imports: [
    ConfigModule.forRoot()
    MongooseModule.forRoot(process.env.MONGODB_URI, {
    	// 옵션
    	useNewUrlParser : true,  // mongodb url을 읽을 수 있도록 설정
      useUnifiedTopology : true  // 최신 mongodb 드라이버 엔진을 사용하도록 설정
    })
  ]
})
export class AppModule implements NestModule {
  private readonly isDev: boolean = process.env.MODE === 'dev' ? true : false
  
  configure(consumer: MiddlewareConsumer) {
    mongoose.set('debug', this.isDev)  // mongoose query 보기
  }
}

// .env
MONGODB_URI=mongodb+srv://<ID>:<password>@cluster0.~~~lr1.mongodb.net/?retryWrites=true&w=majority
MODE=dev
```

![image-20230502113300912](Nest(1).assets/image-20230502113300912.png)

![image-20230502113320577](Nest(1).assets/image-20230502113320577.png)

![image-20230502113535084](Nest(1).assets/image-20230502113535084.png)



schema

- class-validator

```typescript
// test.schema.ts
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose'
import { Document, SchemaOptions } from 'mongoose'
import { IsEmail, IsNotEmpty } from 'class-validator'

const options: SchemaOptions = {
  timestamps: true  // 
}

@Schema(options)
export class Test extends Document {
  @Prop({
    required: true,
    unique: true
  })
  @IsEmail()
  @IsNotEmpty()
  email :string
  
  @Prop({ required: true })
  password :string
}
export const TestSchema = SchemaFactory.createForClass(Test)
```



```typescript
// tests.module.ts
@Module({
  imports: [
    MongooseModule.forFeature([
      { name: Test.name, schema: TestSchema }  // 이해 x, 그렇게 정해진 것
    ])
  ]
})
```

```typescript
// tests.controller.ts
export class TestController {
  constructor(private readonly catService: CatService) {}
  
  @Post()
  async signup(@Body() testRequestDto: TestRequestDto) {
    return this.testService.create(testRequestDto)
  }
}
```



```typescript
// tests.service.ts
@Injectable()
export class TestService {
  constructor(
  	@InjectModel(Test.name)
    private testModel: Model<TestDocument>
  ) {}
  
  async create(testRequestDto: TestRequestDto): Promise<Test> {
    const createdTest = new this.testModel(testRequestDto)
    createdTest.save()
    return createdTest.readOnlyData
  }
}
```



프론트엔드에서 보여지면 안되는 항목 숨기기

mongoDB의 virtual field 활용

```typescript
// test.schema.ts
@Schema(options)
export class Test extends Document {
  @Prop({ required: true, unique: true })
  email :string
  
  @Prop({ required: true })
  password :string
  
  readonly readOnlyData: {
    id: string,
    email: string
  }
}
export const TestSchema = SchemaFactory.createForClass(Test)

TestSchema.virtual('readOnlyData').get((this: Test) => {
  return {
    email: this.email
  }
})
```



## Swagger

```bash
$ npm install @nestjs/swagger
$ yarn add @nestjs/swagger
```

```typescript
// app.module.ts
import { SwaggerMdoule, DocumentBuilder, OpenAPIObject } from '@nestjs/swagger'

async function bootstrap() {
 	const app = await NestFactory.create(AppModule)
  ...
  const config = New DocumentBuilder()
  	.setTitle('테스트 API')  // API 이름
  	.setDescription('API 간단 설명')  // API 간단설명
  	.setVersion('1.0.0')  // API 버전
  	.build()
  const document: OpenAPIObject = SwaggerModule.createDocument(app, config)
  SwaggerModule.setup('docs', app, document)  // 엔드포인트 지정 (https://.../docs)
}
```

```typescript
// test.controller.ts
import { ApiOperation } from '@nestjs/swagger'
...
@ApiOperation({ summary: '회원가입' })
@ApiResponse({ status: 401, decription: "권한 없음"})
@ApiResponse({ status: 200, decription: "성공", type: ReadOnlyTestDto })
@Post()
async signUp() {}
```

```typescript
// test.request.dto.ts
import { ApiProperty } from '@nestjs/swagger'

export class TestRequestDto {
  // request 예시
  @ApiProperty({  
    example: "aaa1234@gmail.com",
    description: email,
    required: true
  })
  email: string
  ...
}
```



### 보안추가

```bash
$ npm install express-basic-auth
```

```typescript
// main.ts
import * as expressBasicAuth from 'express-basic-auth'

app.use(
	['/doc', '/docs-json'],
  expressBasicAuth({
    challenge: true,
    users: {
      [process.env.SWAGGER_USER]: process.env.SWAGGER_PASSWORD  // id와 password 설정
    }
  })
)
```





Schema상속을 통한 DTO 리팩토링

```typescript
// dto
// Pick타입으로 필요한 부분만 상속
// Omit타입으로 필요없는 부분만 제외하고 상속도 가능
export class ReadOnlyTestDto extends PickType(Test, ['email']) {  
  @ApiProperty({
    example: '123',
    description: 'id'
  })
  id: string
}
```

​    

## Repository 패턴

```typescript
@Injectable()
export class TestRepository {
  constructor(
  	@InjectModel(Test.name)
  	private readonly testModel: Model<Test>
  ) {}
  
  async existsByEmail(email: string): Promise<boolean> {
    try {
      const result = await this.testModel.exists({ email })
      retunr result
    } catch (error) {
      throw new HttpException('DB 에러발생', 400)
    }
  }
}
```

```typescript
// module
@Module({
  ...
  providers: [TestRepository]
})

// service
...
export class TestService { 
	constructor(private readonly testRepository: TestRepository) {}
  
  async signUp() {
    ...
    const isExist = await this.testRepository.existsByEmail(email)
    ...
  }
}
```



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



