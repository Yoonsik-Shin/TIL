# Nest (1)

​    

## 0️⃣ 설치

```bash
# CLI 설치
$ npm install -g @nestjs/cli
$ yarn add -g @nestjs/cli

# 프로젝트 시작
$ nest new project-name
```

> cli 명령어

```bash
$ nest g mo 모듈명  # Module 파일 자동 생성
$ nest g co 컨트롤러명  # Controller 파일 자동 생성
$ nest g middleware 미들웨어명  # Middleware 파일 자동 생성
```

​    

---

## 1️⃣ 기본개념

### Controller

``` bash
# Controller 파일 자동 생성 명령어
$ nest g co 컨트롤러명
```

- 클라이언트에서 들어오는 __요청(request)__을 처리하고, __응답(response)__을 반환하는 역할
- Express.js와 유사한 방식으로 라우팅 처리
- 클래스로 정의되며, `@Controller` 데코레이터를 사용

```typescript
// app.controller.ts
import { Controller, Get } from '@nestjs/common'

@Controller('end-point')
export class AppsController {
  @Get()
  fetchAll() {
    return 'fetch all things'
  }
}
```

- `@Controller`를 통해 라우트 end-point를 그룹화

```typescript
// users로 그룹화
@Controller('users')  
export class UserController {
  // users/signup
  @Get('/signup')  
  ...
  
  // users/upload
  @Get('/upload')
	...
}
```



> 라우트 와일드카드

- 정규표현식 활용가능

```typescript
@Get('ab*cd')
```

​    

#### request 객체

| 종류                             | 설명                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| `@Req()`                         | 요청(request) 객체에 대한 접근                               |
| `@Res()`                         | 응답(response) 객체에 대한 접근                              |
| `@Body(param?: string)`          | 요청(request)의 body 객체에 대한 접근, param 매개변수로 특정값 접근가능 |
| `@Param(param?: string)`         | 경로(:id) 매개변수를 가져옴, param 매개변수로 특정 경로값 접근가능 |
| `@Query(param?: string)`         | 쿼리 (?) 매개변수를 가져옴, param 매개변수로 특정 쿼리 접근가능 |
| `@Headers(name?: string)`        | HTTP 헤더 접근 가능, name 매개변소로 특정 헤더값 접근가능    |
| `@Next()`                        | 다음 미들웨어 함수에 대한 접근                               |
| `@UploadFile() / @UploadFiles()` | 업로드된 파일에 대한 접근                                    |
| `@Session()`                     | 세션 객체에 접근                                             |

 ```typescript
 // apps.controller.ts
 import { Controller, Get, Req, Res, Body, Param } from '@nestjs/common'
 import { Request, Response } from 'express'
 
 @Controller()
 export class AppsController {
   // Req 활용
   @Get()
   fetchData(@Req() request: Request) {  ✔️✔️
     return ...
   }
   
   // Body, Res 활용
   @Post()
   createDate(
     @Body() createDto: CreateDto
     @Res({ passthrough: true }) res: Response
   ) {
     return ...
   }
   
   // Params 활용 (1)
   @Get(':id/:category')
   findOne(@Param() params: any): T {
     console.log(params.id);
     console.log(params.category);
     return ...
   }	
     
   // Params 활용 (2)
   @Get(':id/:category')
   findOne(
     @Param('id') id: number
     @Param('category') category: string
   ): T {
     console.log(id);
     console.log(category);
     return ...
   }	
 }
 ```



- Express에서 사용하는 응답객체 사용가능
- 이 경우 따로 설정이 필요함

```typescript
@Res({ passthrough: true })
```



- Standard
- Nest에 기본 내장된 기능 활용



- Library-specific
- Express등의 다른 라이브러리의 응답(response) 객체를 사용

```typescript

```



#### DTO

- Data Trasfer Object (데이터 전송 객체)
- DTO 클래스 자체를 타입으로 지정가능

```typescript
// create-app.dto.ts
export class CreateAppDto {
	name: string;
  age: number;
}
```

```typescript
// apps.controller.ts
@Post()
async create(@Body() createAppDto: CreateAppDto) {  ✔️✔️
  return ...
}
```

​    

#### HTTP 메서드 데코레이터

| 종류         | 설명                  |
| ------------ | --------------------- |
| `@Get()`     |                       |
| `@Post()`    |                       |
| `@Put()`     |                       |
| `@Delete()`  |                       |
| `@Patch()`   |                       |
| `@Options()` |                       |
| `@Head()`    |                       |
| `@All()`     | 모든 HTTP 메서드 처리 |



#### 상태코드

- 응답 기본 상태코드는 __200__ (Post 요청은 __201__)
- `@HttpCode()` 데코레이터를 통해 상태코드 커스텀 가능 (__Standard 방식__)

```typescript
import { HttpCode } from '@nestjs/common'

@Post()
@HttpCode(204)  ✔️✔️
create() { 
  return 'created' 
}
```

- 상태코드가 동적일 때는 __library-specific 방식__으로 사용함 (Express 방식)

```typescript
import { Controller, Get, Res, HttpStatus } from '@nestjs/common';
import { Response } from 'express';

@Controller()
export class AppsController {
  @Get()
  findAll(@Res({ passthrough: true }) res: Response) {  // passthrough 옵션 필수 ✔️✔️
    const userHasPermission = checkUserPermission(); // 권한 확인하는 함수
    
    // 조건에 따라 상태코드 분기
    if (userHasPermission) {
      res.status(HttpStatus.OK).json({ message: 'Success' });
    } else {
      res.status(HttpStatus.FORBIDDEN).json({ message: 'Access denied' });
    }
  }
}
```

​    

#### 커스텀 헤더

- __Standard 방식__ : `@Header()` 데코레이터를 통해 커스텀 응답 헤더 지정 가능

```typescript
import { Header } from '@nestjs/common'

@Get()
@Header('Custom-Header', 'Custom-Header-Value')
findAll() {
	return 'found All'
}
```

- __library-specific 방식__

```typescript
import { Controller, Get, Res } from '@nestjs/common';
import { Response } from 'express';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(@Res() res: Response) {
    // 응답 헤더 설정
    res.setHeader('Custom-Header', 'Custom Value');
		
    // 응답 헤더 해제
    res.removeHeader('WantRemovHeader')
  }
}
```

​    

#### Redirect

- __Standard 방식__ :`@Redirect()` 데코레이터 사용
- 매개변수로 이동할 `url`과 상태코드를 받음 (상태코드 기본값: __302__)

```typescript
@Get()
@Redirect('https://yoonsik.com', 301)
redirectToPage() {
  // none
}

// 객체로 표현
@Redirect({
  'url': 'https://yoonsik.com',
  'statusCode': 301
})
```

> HTTP 상태코드나 redirect URL을 동적으로 결정하고 싶을때

```typescript
@Get()
@Redirect('https://yoonsik.com', 301)  // 조건에 맞으면 무시됨
getDocs(@Query('version') version) {
  // 조건에 맞으면 해당 페이지로 인자가 변경된 후 리다이렉트됨
  if (version === '5') {
    return { 
      url: 'https://yoonsik.com/v5/',
      statusCode: 302
    }  
  }
}
```

- __library-specific 방식__

```typescript
import { Controller, Get, Res } from '@nestjs/common';
import { Response } from 'express';

@Controller('cats')
export class CatsController {
  @Get()
  findAll(@Res() res: Response) {
    // 응답 헤더 설정
    res.redirect('https://yoonsik.com')
  }
}
```

​    

---

### Providers

- Controller로부터 복잡한 작업을 위임받아 수행한 후 결과값 반환
- Provider의 핵심은 __의존성 주입 (DI)__
- Service, Repository, Factory, 헬퍼등의 기본적인 Nest 클래스는 모두 Provider로 취급될 수 있음



#### Services

```bash
# Service 파일 자동 생성
$ nest g s 서비스명
```

```typescript
// apps.controller.ts
import { Controller, Get, Post, Body } from '@nestjs/common';
import { AppsService } from './apps.service';

@Controller()
export class AppsController {
  constructor(private appsService: AppsService) {} ✔️✔️

  @Get()
  async findAll(): Promise<Apps[]> {
    // service.ts로 비지니스 로직을 넘김
    return this.appsService.findAll() ✔️✔️
  }
}
```



#### 의존성 주입 (DI: Dependency Injection)



### Module



### 캡슐화 

- module의 providers에 사용하는 Service를 모두 추가해주는 방식
- 사용하는 서비스가 많아지면 추가할 값들이 너무 많아짐

```typescript
@Module({
  imports: [AAAModule, BBBModule, CCCModule],
  ...
  // providers에 값들이 너무 많아짐
  providers: [
     AAAService,
     BBBService,
     CCCService,
     DDDService
  ]
})
```

- 해당 module에서 export해준 Service는 다른 모듈에서 사용할 때, providers에 추가할 필요없이 사용가능

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

​    

### CORS

```typescript
// main.ts
...
app.enableCors({
  origin: true,  // 개발시에만 true, 배포시에는 특정 url만 사용하도록 변경
 	credentials: true
})
```

​    

### middleware

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

​    

### Exception filters (예외처리)

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

​    

### Pipes

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

​    

### Interceptors

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

​    

### Repository 패턴

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



---

## Graphql

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



DTO : Data Transfer Object 데이터 전송 객체

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



## DB 연동

### MySQL

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



### MongoDB

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


