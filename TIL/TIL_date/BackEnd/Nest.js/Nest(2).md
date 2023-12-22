# Nest (2)

## 1️⃣ 인증

### 세션 기반 인증

- 세션을 생성하고 나서 DB에 저장한 후, 이후 사용자의 요청에 포함된 세션 정보가 세션 DB에 저장되어있는지 확인
- 세션 방식의 단점은 브라우저에 저장된 데이터를 탈취당할 수 있다는 것
- 세션은 서버의 저장소에 저장되고 빠른 응답을 위해 메모리에 상주시키는 경우가 많음
- 이로 인해 서비스가 몰렸을 경우 요청마다 세션을 확인해야하므로 DB에 많은 부하를 일으켜 메모리부족으로 서비스장애가 발생할 수 있음
- 이에 `Redis`같은 인메모리 DB에 세션을 저장하여 좀 더 빠르게 처리함
- 서비스가 여러 도메인으로 나누어져 있을 경우 CORS 문제로 인해 도메인 간 세션 공유가 어려움



### 토큰 기반 인증

- 사용자가 로그인 했을 때 서버에서 토큰을 생성하여 전달하고 따로 저장소에 저장하지는 않는 방식
- 로그인 이후 요청에 대해 클라이언트가 전달한 토큰 검증만 수행
- `Jwt`를 가장 많이 사용함
- 세션 방식과 달리 상태 관리가 필요없어 어느 도메인이라도 같은 인증을 수행할 수 있음



### JWT

- JSON 웹 토큰
- https://jwt.io에서 JWT를 JSON 객체로 인코딩하거나 디코딩해볼 수 있음
- JWT는 헤더, 페이로드, 시그니처 3가지 요소를 가지며, 이를 점(`.`)으로 구분함
- 헤더와 페이로드는 각각 `base64`로 인코딩 되어 있음

​    

#### 헤더

- 일반적으로 JWT의 유형(`typ`)과 알고리즘(`alg`) 정보를 담고 있음

```json
{
    "typ": "JWT",
    "alg": "HS256"
}
```

- `type`
  - `JWS`와 `JWE`에 정의된 미디어 타입
  - JWT를 처리하는 애플리케이션에게 페이로드가 무엇인지 알려주는 역할
- `alg`
  - 토큰을 암호화하는 알고리즘
  - 암호화하지 않을 경우 `none`으로 정의

​     

#### 페이로드

- 페이로드는 클레임(Claim)이라 부르는 정보를 포함

> registered 클레임

- IANA JWT 클레임 레지스트리에 등록된 클레임
- 필수는 아니지만 JWT가 상호 호환성을 가지려면 작성해야함
- `iss (issuer, 발급자)`
  - 누가 토큰을 발급했는지 나타냄
  - 애플리케이션에서 임의로 정의한 문자열이나 URI형식을 가짐
- `sub (subject, 주제)`
  - 주제에 대한 설명
  - 토큰 주제는 발급자가 정의하는 문맥상 또는 전역으로 유일한 값을 가져야함
  - 문자열이나 URI형식을 가짐
- `aud (audience, 수신자)`
  - 누구에게 토큰이 전달되는가를 나타냄
  - 주로 보호된 리소스의 URL을 값으로 설정
- `exp (expiration, 만료시간)`
  - 언제 토큰이 만료되는지를 나타냄
  - 일반적으로 UNIX Epoch 시간을 사용
- `nbf (not before, 정의된 시간 이후)`
  - 정의된 시간 이후에 토큰이 활성화됨
  - 토큰이 유효해지는 시간이전에 미리 발급되는 경우 사용
  - 일반적으로 UNIX Epoch 시간을 사용
- `iat (issued at, 토큰발급시간)`
  - 언제 토큰이 발급되었는지를 나타냄
  - 일반적으로 UNIX Epoch 시간을 사용
- `jti (JWT ID, 토큰식별자)`
  - 토큰의 고유 식별자
  - 같은 값을 가질 확률이 없는 암호학적인 방법으로 생성되어야함

> Public 클레임

- 공개해도 무방한 페이로드를 공개클레임으로 정의
- 이름 충돌 방지를 위해 IANA JWT 클레임 레지스트리에 클레임 이름을 등록하거나 합리적인 예방조치를 해야함
- 보통 URI 형식으로 정의함

```json
{
    "http://example.com/is_root": true
}
```

> Private 클레임

- JWT 발급자와 사용자간에 사용하기로 약속한 클레임
- 서비스 도메인 내에서 필요한 이름과 값을 비공개 클레임으로 정의
- 이름 충돌이 발생하지 않도록 주의해야함
- 비공개 클레임에는 비밀번호와 같은 중요한 정보를 포함해서는 안됨

​    

#### 시그니처

- 헤더와 페이로드는 단순히 `base64`로 인코딩하기 때문에 조작하기 쉽기 때문에 
- 생성된 토큰이 유효한지 검증하는 장치가 필요
- `HS256` 방식의 암호화는 헤더와 페이로드를 `base64`로 인코딩한 문자열과 서버의 salt를 이용하여 `HMACSHA256`알고리즘에 넣어줌

```json
HMACSHA256(
	base64UrlEncode(header) + "." + 
	base64UrlEncode(payload),
    'salt값'
)
```

- JWT를 공격자가 다시 구성하여 페이로드를 수정한 후 salt값이 다른 JWT를 생성하여 전송하면 `Invaild Signature`라고 표기됨

​    

---

## 2️⃣ CORS

```typescript
// main.ts
...
app.enableCors({
	origin: true,  // 개발시에만 true, 배포시에는 특정 url만 사용하도록 변경
 	credentials: true
})
```

​    

---

## 3️⃣ Graphql

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

​    

---

## 4️⃣ Swagger

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

> `@ApiResponse()`에 Dto를 전달하는 방법

```ts
@ApiCreatedResponse({
    schema: {
        allOf: [{ $ref: getSchemaPath(CreateTestDto) }]
    }
})
```

커스텀 데코레이터로 만들어서 사용하면 컨트롤러의 코드를 줄일수 있음



`@ApiPropertyOptional`

- 필수 옵션이 아닌 것에 `@ApiProperty` 대신 사용



`@ApiExtraModels`

- swagger에서 인식하지 못하고 있는 DTO들을 등록해줌

```ts
@ApiTags('Test')
@ApiExtraModels(FindTestDto) ✔️✔️ 
@Controller()
export class TestController {}
```



​    

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

---

## 5️⃣ 로깅

> 로깅 옵션 조절시 가능한 동작 제어

- 로깅 비활성화
- 로그 레벨 지정 : `log`, `error`, `warn`, `debug`, `verbose`
- 로거의 타임스탬프 재정의
- 기본 로거 재정의 (오버라이딩)
- 기본 로거를 확장하여 커스텀 로거 작성
- 의존성 주입으로 로거 주입하거나 테스트 모듈로 제공



### 내장로거 

-  내장`Logger`클래스는 `@nset/common` 패키지에서 제공

```ts
import { Injectable, Logger } from '@nestjs/common'

@Injectable()
export class AppService {
    private readonly logger = new Logger(AppService.name)
    
    ttt() {
        this.logger.error('에러메시지')
        this.logger.warn('경고메시지')
        this.logger.log('일반로그')
        this.logger.verbose('')
        this.logger.debug('디버그')
    }
}
```

> 내장로거 비활성화

```ts
// main.ts
const app = await NestFactory.create(AppModule, {
    logger: false ✔️✔️
})
```

> 로그 레벨 지정

- 프로덕션 환경에서는 `debug`로그를 남기지 않는 것이 좋음
- 일반적으로 실행 환경에 따라 로그 레벨을 지정해줌

```ts
const app = await NestFactory.create(AppModule, {
    logger: process.env.NODE.ENV === 'production'
   		? ['error', 'warn', 'log']
    	: ['error', 'warn', 'log', 'verbose', 'debug']
})
```

- 로그 레벨을 하나만 설정하면 해당 레벨보다 큰 숫자를 가진 레벨들도 함께 출력됨

```ts
const LOG_LEVEL_VALUES: Record<LogLevel, number> = {
    debug: 0,
    verbose: 1,
    log: 2,
    warn: 3,
    error: 4
}
```

​    

### 커스텀로거

- `@nestjs/common` 패키지의 `LoggerService`인터페이스를 구현해야함

```ts
export interface LoggerService {
    log(message: any, ...optionalParams: any[]): any
    error(message: any, ...optionalParams: any[]): any
    warn(message: any, ...optionalParams: any[]): any
    debug?(message: any, ...optionalParams: any[]): any
    verbose?(message: any, ...optionalParams: any[]): any
    setLogLevelss?(levels: LogLevel[]): any
}
```

```ts
export class CustomLogger implements LoggerService {
    log(message: any, ...optionalParams: any[]) {}
    error(message: any, ...optionalParams: any[]) {}
    warn(message: any, ...optionalParams: any[]) {}
    debug?(message: any, ...optionalParams: any[]) {}
    verbose?(message: any, ...optionalParams: any[]) {}
}
```

- `ConsoleLogger`를 상속받으면 더 디테일한 커스텀을 할 수 있음

```ts
export class CustomLogger extends ConsoleLogger implements LoggerService {
    log(message: any, stack?: string, context?: string) {
        super.log.apply(this, arguments)
    }
    ...
}
```

> 커스텀 로거 전

```ts
async function bootstrap() {
    const app = await NestFactory.create(AppModule)
    app.useLogger(app.get(CustomLogger))  ✔️✔️
    await app.listen(3000)
}
```

> 커스텀 로거 주입

```ts
// LoggerModule
import { CustomLogger } from './?.service'

@Module({
    providers: [CustomLogger],
    exports: [CustomLogger] 
})
export class LoggerModule
```

```ts
// AppModule
@Module({
    imports: [LoggerModule]
})
export class AppModule {}
```

```ts
@Injectable()
export class AppService {
    constructor(private customLogger: CustomLogger) {}
    
    ttt() {
        this.customLogger.error('에러')
        return ...
    }
}
```

​    

### winston 라이브러리

- 프로덕션레벨에서는 로그를 콘솔에 출력만 하는게 아니라 파일에 저장하거나 DB에 저장하여 쉽게 검색할 수 있게 해야함
- Nest에서는 `nest-winston`을 통해 편하게 구현할 수 있음

```bash
$ yarn add nest-winston winston
```

```ts
// AppModule
import * as winston from 'winston'
import {
    utilities as nestWinstonModuleUtilties,
    WinstonModule
} from 'nest-winston'

@Module({
    imports: [
        WinstonModule.forRoot({
            transport: [
                new winston.transports.Console({
                    level: process.env.NODE_ENV === 'production' ? 'info' : 'silly', // 로그레벨 지정
                    format: wiston.format.combine(
                    	winston.format.timestamp(),  // 로그를 남긴 시간 표시
                    	nestWinstonModuleUtilities.format.nestLike('앱이름', { prettyPrint: true })
                    )
                })
            ]
        })
    ]
})
```

> winston이 지원하는 로그 레벨

```ts
{
    error: 0,
    warn: 1,
    info: 2,
    http: 3,
    verbose: 4,
    debug: 5,
    silly: 6        
}
```

> winston Logger 객체 주입

```ts
import { Logger as WinstonLogger } from 'winston'
import { WINSTON_MODULE_PROVIDER } from 'nest-winston'

export class UserController {
    constructor(
    	@Inject(WINSTON_MODULE_PROVIDER) private readonly logger: WinstonLogger
    ) {}
    
    private printWinstonLog(dto) {
        console.log(this.logger.name)
        this.logger.error('')
        this.logger.warn('')
    }
    
    @Post()
    async createTest(@Body() createTestDto: CreateTestDto) {
        this.printWinstonLog(createTestDto)
    }
}
```

> 내장로거 대체

- `nest-winston`은 `LoggerService`를 구현한 `WinstonLogger`클래스를 제공함

1. 부트스트랩 과정 미포함

```ts
// main.ts
import { WINSTON_MODULE_NEST_PROVIDER } from 'nest-winston'

async function bootstrap() {
    const app = await NestFactory.create(AppModule)
    app.useLogger(app.get(WINSTON_MODULE_NEST_PROVIDER)) ✔️✔️ 
    await app.listen(3000)
}
bootstrap()
```

```ts
import { LoggerService } from '@nestjs/common'
import { WINSTON_MODULE_NEST_PROVIDER } from 'nest-winston'

export class TestController {
    constructor(
    	@Inject(WINSTON_MODULE_NEST_PROVIDER) private readonly logger: LoggerService ✔️✔️
    ) {}
}
```

2. 부트스트랩 과정 포함

```ts
import { WinstonModule } from 'nest-winston'

async function bootstrap() {
   const app = await NestFactory.create(AppModule, {
       logger: WinstoModule.createLogger({
           transports: [
               new winston.transports.Console({
                   level: process.env.NODE_ENV === 'production' ? 'info' : 'silly',
                   format: winston.format.combine(
                       winston.format.timestamp(),
                       nestWinstonModuleUtilities.format.nestLike('앱이름', { prettyPrint: true })
                   )
               })
           ]
       })
   })
   await app.listen(3000)
}
bootstrap()
```

```ts
// 로그를 남길 모듈
import { Logger } from '@nestjs/common'

@Module({
    providers: [Logger]
})
export class TestModule {}
```

```ts
import { Logger } from '@nestjs/common'

export class TestController {
    constructor(
    	@Inject(Logger) private readonly logger: LoggerService
    ) {}
}
```



---

## 6️⃣ 태스크 스케줄링

- Nest에서는 `node-cron`을 통합한 `@nestjs/schedule` 패키지를 제공함

```bash
$ yarn add @nestjs/schedule @types/cron
```

- 태스크 스케줄링은 모든 모듈이 예약된 작업을 로드하고 확인하는 `onApplicationBootstrap` 생명주기 훅이 발생할 때 등록됨

```ts
// Batch 모듈
import { ScheduleModule } from '@nestjs/schedule'

@Module({
    imports: [
        ScheduleModule.forRoot() ✔️✔️ // 스케줄러 초기화 및 크론잡, 타임아웃, 인터벌을 등록
    ]
})
export class BatchModule {}
```

- 타임아웃 : 스케줄링이 끝나는 시각
- 인터벌 : 주기적으로 반복되는 시간 간격



### 선언방식

#### 1. 크론잡

- `@Cron()` 데코레이터를 선언한 메서드를 태스크로 구현하는 방식

```ts
import { Cron } from '@nestjs/schedule'

@Injectable()
export class TaskService {
    @Cron('* * * * *', { name: 'cronTask' })
    ttt() {}
}
```

- `@Cron()`의 첫번째 인수는 태스크 반복 주기로 표준 크론 패턴을 따름

```ts
a b c d e
```

| 위치 | 의미                   | 값                                                      |
| ---- | ---------------------- | ------------------------------------------------------- |
| a    | 분 (Min)               | 0 ~ 59분                                                |
| b    | 시 (Hour)              | 0 ~ 23시                                                |
| c    | 일 (Day)               | 1 ~ 31일                                                |
| d    | 월 (Month)             | 1 ~ 12월                                                |
| e    | 요일 (Day of the week) | 0 : 일요일<br />1 : 월<br />2 : 화<br />...<br />6 : 토 |

> 한번만 수행되는 태스크 등록

- `Date` 객체 활용

```ts
@Cron(new Date(Date.now() + 3 * 1000))  // 앱 실행후 3초후 태스크 수행
```

> 자주 사용하는 크론 패턴

- Nest에서 자주 사용하는 크론 패턴을 `CronExpession` 열거형으로 제공함
- https://github.com/nestjs/schedule/blob/master/lib/enums/cron-expression.enum.ts

```ts
@Cron(CronExpession.MONDAY_TO_FRIDAY_AT_1AM)
```

- `@Cron()`의 두번째 인수는 `CronOptions` 객체

| 속성         | 설명                                                         |
| ------------ | ------------------------------------------------------------ |
| name         | 태스크이름, 선언한 크롭잡에 엑세스하거나 제어할 때 유용      |
| timeZone     | 실행 시간대 지정 (`Asia/Seoul`)                              |
| utcOffset    | timeZone 대신 UTC 기반으로 시간대의 오프셋 지정 (국내 : '+09:00' or 숫자 9) |
| unrefTimeout | Node.js의 timeout.unref()와 관련됨, 이벤트 루프를 계속 실행하는 코드가 있고 크론 잡의 상태에 관계없이 잡이 완료될 때 노드 프로세스를 중단하고 싶을 때 사용 |

- timeZone 옵션과 utcOffset 옵션을 함께 사용하면 이상동작을 일으킬 수 있으므로 같이 사용하면 안됨

​    

#### 2. 인터벌

- `@interval` 데코레이터 사용
- 첫번째 인수는 태스크의 이름
- 두번째 인수는 타임아웃 시간

```ts
@Interval('intervalTask', 3000)  // 앱실행후 3초후 첫 수행후, 3초마다 반복
ttt() {}
```

​    

#### 3. 타임아웃

- 앱이 실행된 이후 태스크를 단 한 번만 수행
- 인수는 인터벌과 동일

```ts 
@TimeOut('timeoutTask', 5000)
qqq() {}
```

​    

### 동적 스케줄링

- 앱 구동중 특정 조건을 만족했을 경우 태스크를 등록해야하는 경우
-  `SchedulerRegistry`에서 제공하는 API를 사용

```ts
import { Cronjob } from 'cron'
import { SchedulerRegistry } from '@nestjs/schedule'

@Injectable()
export class TaskService {
    constructor(private schedulerRegistry: SchedulerRegistry) { ✔️✔️
        this.addCronJob()
    }
    
    addCronJob() {
        const name = 'test'
        const job = new Cronjob('* * * * *', () => {
            // 실행할 job
        })
        
        this.schedulerRegistry.addCronJob(name, job)
    }
}
```

- 아직 `SchedulerRegistry`에 크론잡을 추가만 해둔 것이고, 태스크 스케줄링을 등록한 것은 아니므로 앱을 구동해도 아무런 동작도 하지 않음
- 등록된 크론잡을 스케줄링에서 동작시키고 동작시키는 컨트롤러가 필요

```ts
import { SchedulerRegistry } from '@nestjs/schedule'

@Controller('batches')
export class BatchController {
    constructor(private scheduler: SchedulerRegistry) {}
    
    @Post('/start-job')
    start() {
        const job = this.scheduler.getCronJob('test')  // 크론잡을 등록할 때 선언한 이름
        job.start()
    }
    
    @Post('/stop-job')
    stop() {
        const job = this.scheduler.getCronJob('test')  // 크론잡을 등록할 때 선언한 이름
        job.stop()
    }
}
```

> `Cronjob` 객체 매서드

- `stop()` : 실행이 예약된 작업을 중지
- `start()` : 중지된 작업을 다시 시작
- `setTime(time: CronTime)` : 현재 작업을 중단하고 새로운 시간을 설정하여 재시작
- `lastDate()` : 작업이 마지막으로 실해오딘 날짜를 반환
- `nextDates(count: number): moment[]`
  - 예정된 작업의 실행시각을 count 개수만큼 배열로 반환
  - 배열의 각 요소는 `moment` 객체

​    

---

## 7️⃣ 헬스체크

- Nest는 `Terminus` 헬스체크 라이브러리를 제공 (`@nestjs/terminus`)
- `Terminus`는 다양한 상태 표시기(health indicator)를 제공하고, 필요하면 직접 만들어서 사용할 수 있음

> 상태 표시기(health indicator) 종류

- `HttpHealthIndicator`
- `MongooseHealthIndicator`
- `TypeOrmHealthIndicator`
- `SequelizeHealthIndicator`
- `MicroserviceHealthIndicator`
- `MemoryHealthIndicator`
- `GRPCHealthIndicator`
- `DiskHealthIndicator`



### `Terminus` 적용

```bash
$ yarn add @nestjs/terminus
```

- 특정 라우터 엔드포인트로 요청을 보내고 응답을 확인하는 방법 사용

```ts
import { TerminusModule } from '@nestjs/terminus'
import { HealthCheckController } from './health-check/health-check.controller'

@Module({
    imports: [TerminusModule],
    providers: [HealthCheckController]
})
export class AppModule {}
```



### Http Heath Check

- `HttpHealthIndicator`는 `@nestjs/axios`를 사용함

```bash
$ yarn add @nestjs/axios
```

```ts
import { HttpModule } from '@nestjs/axios'
import { TerminusModule } from '@nestjs/terminus'
import { HealthCheckController } from 'health-check.controller'

@Module({
    imports: [TerminusModule, HttpModule],
    providers: [HealthCheckController]
})
export class AppModule {}
```

```ts
import { HealthCheckService, HttpHealthIndicator, HealthCheck } from '@nestjs/terminus'

@Controller('health-check')
export class HealthCheckController {
    constructor(
    	private health: HealthCheckService,  ✔️✔️
    	private http: HttpHealthIndicator,  ✔️✔️
    ) {}
    
    @Get()
    @HealthCheck()  ✔️✔️
    check() {
        return this.health.check([
            () => this.http.pingCheck('응답결과이름', '요청보낼url')
        ])
    }
}
```

> `HealthCheckResult` 타입

```ts
export interface HealthCheckResult {
    status: HealthCheckStatus  // 헬스체크를 수행한 전반적인 상태 ('error' | 'ok' | 'shutting_down')
    info?: HealthIndicatorResult  // 상태가 'up'일 때의 상태정보
    error?: HealthIndicatorResult  // 상태가 'down'일 때의 상태정보
    details: HealthIndicatorResult  // 모든 상태표시기의 정보
}
```

​    

### TypeOrm Health Check

- `TypeOrmHealthIndicator`는 단순히 DB가 잘 살아 있는지 확인

```ts
import { HealthCheckService, HttpHealthIndicator, HealthCheck, TypeOrmHealthIndicator } from '@nestjs/terminus'

@Controller('health-check')
export class HealthCheckController {
    constructor(
    	private health: HealthCheckService,
    	private http: HttpHealthIndicator,
    	private db: TypeOrmHealthIndicator  ✔️✔️
    ) {}
    
    @Get()
    @HealthCheck()  ✔️✔️
    check() {
        return this.health.check([
            () => this.http.pingCheck('응답결과이름', '요청보낼url'),
            () => this.db.pingCheck('database')  ✔️✔️
        ])
    }
}
```

​    

### 커스텀 상태표시기

- `@nestjs/terminus`에서 제공하지 않는 상태표시기가 필요할 경우, `HealthIndicator`를 상속받아 커스텀 가능

```ts
export declare abstract class HealthIndicator {
    protected getStatus(
    	key: string,  // 상태를 나타냄
    	isHealthy: boolean, // 상태 표시기가 상태를 측정한 결과
    	data?: { [key: string]: any }  // 결과에 포함될 데이터
    ): HealthIndicatorResult
}
```

```ts
import { HealthIndicator, HealthIndicatorResult, HealthCheckError } from '@nestjs/terminus'

export interface Test {
    name: string;
    type: string;
}

@Injectable()
export class TestHealthIndicator extends HealthIndicator {
    private tests: Test[] = [
        { name: 'ttt', type: "qqq" },
        { name: 'uuu', type: 'vvv' }
    ]
    
    async isHealthy(key: string): Promise<HealthIndicatorResult> {
        const data = this.tests
        const isHealthy = ...
        
        this.getStatus(key, isHealthy, { data })
        
        if (isHealthy) return result
        throw new HealthCheckError('헬스체크 실패', result)
    }
}
```

```ts
import { TestHealthIndicator } from './health-check/test.health'

@Module({
    providers: [TestHealthIndicator]
})
export class AppModule {}
```

```ts
import { HealthCheckService, HttpHealthIndicator, HealthCheck, TypeOrmHealthIndicator } from '@nestjs/terminus'
import { TestHealthIndicator } from './test.health'

@Controller('health-check')
export class HealthCheckController {
    constructor(
    	private health: HealthCheckService,
    	private http: HttpHealthIndicator,
    	private db: TypeOrmHealthIndicator,
    	private testHealthIndicator: TestHealthIndicator  ✔️✔️
    ) {}
    
    @Get()
    @HealthCheck()
    check() {
        return this.health.check([
            () => this.http.pingCheck('응답결과이름', '요청보낼url'),
            () => this.db.pingCheck('database'),
            () => this.testHealthIndicator.isHealthy('키')  ✔️✔️
        ])
    }
}
```
