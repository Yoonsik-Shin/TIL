# Nest (1)

> 설치

```bash
# CLI 설치
$ npm install -g @nestjs/cli

# 프로젝트 시작
$ nest new 프로젝트이름
```

> 주요 cli 명령어

```bash
$ nest g resource 폴더명 # 기본 CRUD 생성
$ nest g mo 모듈명  # Module 파일 자동 생성
$ nest g co 컨트롤러명 --no-spec  # Controller 파일 자동 생성 (--no-spec 옵션 설정시, 테스트파일제외)
$ nest g s 서비스명 # Service 파일 자동 생성
$ nest g middleware 미들웨어명  # Middleware 파일 자동 생성
```

> `nest -h`로 모든 명령어 확인

![image-20230810223804282](Nest(1).assets/image-20230810223804282.png)

​    

## 1️⃣ 기본개념

### 1. Controller

- 클라이언트에서 들어오는 __요청(request)__을 처리하고, __응답(response)__을 반환하는 역할
- Express.js와 유사한 방식으로 라우팅 처리
- 클래스로 정의되며, `@Controller` 데코레이터를 사용

``` bash
# Controller 파일 자동 생성 명령어
$ nest g co 컨트롤러명
```

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

>  request 객체

| 종류                             | 설명                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| `@Req()`                         | 요청(request) 객체에 대한 접근                               |
| `@Res()`                         | 응답(response) 객체에 대한 접근                              |
| `@Body(param?: string)`          | 요청(request)의 body 객체에 대한 접근, param 매개변수로 특정값 접근가능 |
| `@Param(param?: string)`         | 경로(:id) 매개변수를 가져옴, param 매개변수로 특정 경로값 접근가능 |
| `@Query(param?: string)`         | 쿼리(?) 매개변수를 가져옴, param 매개변수로 특정 쿼리 접근가능 |
| `@Headers(name?: string)`        | HTTP 헤더 접근 가능, name 매개변소로 특정 헤더값 접근가능    |
| `@Next()`                        | 다음 미들웨어 함수에 대한 접근                               |
| `@UploadFile() / @UploadFiles()` | 업로드된 파일에 대한 접근                                    |
| `@Session()`                     | 세션 객체에 접근                                             |

 ``` typescript
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

> 라우트 매개변수 (패스 매개변수)

- `@Param` 데코레이터로 주입받을 수 있음
- 전달받는 방식으로 2가지 방법이 있음

1. 객체로 한번에 받기

   - params의 타입이 any가 되어 권장하지 않음
   - 라우트 매개변수는 항상 string이므로 명시적으로 `{ [key: string]: string }` 타입으로 지정해도됨

   ```ts
   @Delete(':userId/memo/:memoId')
   deleteUserMemo(
   	@param() params: { [key: string]: string }
   ) {
       return `userId: ${params.userId}, memoId: ${params.memoId}`
   }
   ```

2. 각각 따로 받기

```ts
@Delete(':userId/memo/:memoId')
deleteUserMemo(
	@Param('userId') userId: string,
    @Param('memoId') memoId: string
) {
    return `userId: ${params.userId}, memoId: ${params.memoId}`
}
```

​    

> 응답 (Response) 조작 옵션

1. Standard (권장됨)

   - Nest에 기본 내장된 기능(메서드) 활용
   - Object type을 반환할 때, 자동으로 JSON으로 변환(직렬화)되어 처리함
   - primitive type을 반환할 때는 값 그대로 전송
   - 기본적 상태코드는 200이고, POST만 201
   - `HttpCode()`데코레이터를 사용하여 기본 상태코드값을 변경할 수 있음

   ```js
   import { Controller, Get, HttpCode } from '@nestjs/common';
   
   @Controller('cats')
   export class CatsController {
     @Get()
     @HttpCode(200)
     findAll(): string {
       return 'This action returns all cats';
     }
   }
   ```

2. Library-specific

   - Express등의 다른 라이브러리의 응답(response) 객체를 사용

   ```js
   import { Controller, Get, Res, HttpStatus } from '@nestjs/common';
   import { Response } from 'express'
   
   @Controller('cats')
   export class CatsController {
     @Get()
     findAll(@Res({ passthrough: true }) res: Response) {
       res.status(HttpStatus.OK).send({
         test: '됨?', 
         problem: '뭐가 문제야?',
         solved: 'return도 JSON으로 직렬화하고 send도 JSON으로 직렬화해서 나는 오류같아',
       });
     }
   }
   ```

   - `return`문의 반환값도 자동으로 JSON으로 직렬화해주고, `res.send()`도 자동으로 JSON으로 직렬화해줘서, 두가지 모두 사용하면 오류발생!
   - 이 방식을 사용할 때는 `return` 키워드를 안써야함

> 주의사항

- `@Res()` 또는 `@Next()` 사용시, __Library-specific__ 옵션이 선택된 것으로 감지함
- 따라서 Standard 방식이 자동으로 비활성화됨
- 동시에 두가지 접근 방식을 사용하려면 아래 예시처럼 사용해야함

```typescript
@Res({ passthrough: true })
@Next({ passthrough: true })
```

​    

> DTO

- Data Trasfer Object (데이터 전송 객체)
- 데이터가 네트워크를 통해 전송되는 방식을 정의하는 객체
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

> HTTP 메서드 데코레이터

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

​     

> 상태코드

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

>  커스텀 헤더

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

> Redirect

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
getDocs(
    @Query('version') version
) {
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

### 2. Providers

- Controller로부터 복잡한 작업을 위임받아 수행한 후 결과값 반환 (비지니스 로직 수행)
- Provider의 핵심은 __의존성 주입 (DI)__
- Service, Repository, Factory, helpers(헬퍼)등의 기본적인 Nest 클래스는 모두 Provider로 취급될 수 있음
- 애플리케이션과 동일한 수명을 가짐
- 애플리케이션 부팅시 모든 의존성이 해결되어야 하므로 모든 provider가 인스턴스화됨

​    

>  프로퍼티 기반주입

- Property-based injection
- 프로바이더를 직접 주입받아 사용하지 않고 상속 관계에 있는 자식 클래스를 주입받아 사용하고 싶은 경우
- 자식 클래스에서 부모 클래스가 제공하는 함수를 호출하기 위해서는 부모 클래스에서 필요한 프로바이더를 super()로 전달해야함

```ts
// base-service.ts (@Injectable 사용 x)
export class BaseService {
    constructor() {}
    ttt() {}
    qqq() {
        return this.AAA.ttt()
    }
}

// AAA.ts 
@Injectable()
export class AAA {
    ttt() {
        return '12345'
    }
}

// BBB.ts
@Injectable()
export class BBB extends BaseService {
    constructor(private readonly _aaa: AAA) {
        super(_aaa)
    }
    ttt() {
        return this.qqq()
    }
}
```

- 프로퍼티 기반주입을 활용하면 위 방식을 더욱 쉽게 활용할 수 있음

```ts
export class BaseService {
    @Inject(AAA) private readonly aaa: AAA ✔️✔️
}
```

- 상속관계에 있지 않는 경우에는 속성기반 주입을 사용하지말고 생성자 기반 주입을 사용하는 것이 권장됨

​    

>  Injection scopes

- 의존성 주입 컨테이너를 통해 프로바이더의 수명을 제어
- 필요한 스코프에 따라 인스턴스를 생성하거나 공유
- 싱글톤 스코프를 사용하는 것을 권장함

```typescript
import { Injectable, Scope } from '@nestjs/common';

@Injectable({ scope: Scope.DEFAULT }) ✔️✔️
@Injectable({ scope: Scope.REQUEST }) ✔️✔️
@Injectable({ scope: Scope.TRANSIENT }) ✔️✔️
export class CatsService {}

// 커스텀 프로바이더
{
    provide: '',
    useClass: ,
    scope: Scope.TRANSIENT ✔️✔️
}
```

1. `DEFAULT`
   - provider가 애플리케이션 전체에서 공유되는 __싱글톤__으로 동작함
   - 기본적으로 모든 provider는 Default Scope를 가짐
   - 인스턴스 수명은 애플리케이션 라이프사이클에 직접적으로 연결됨
2. `REQUEST`
   - 매 요청마다 provider 인스턴스를 생성 (new)
   - 인스턴스는 요청 처리가 완료된 후 가비지 컬렉션됨
3. `TRANSIENT`
   - 매 주입마다 provider 인스턴스를 생성 (new)
   - 소비자간에 인스턴스가 공유되지 않음

> 제한사항

- 웹소켓 게이트웨이는 단일 인스턴스로 작동해야 하므로 요청 스코프 provider를 사용해서는 안됨
- Passport 전략이나 Cron 컨트롤러와 같은 다른 몇 가지 provider에도 적용

​    

#### Custom Provider

1. Nest가 생성해주는 인스턴스 대신, 직접 인스턴스를 생성하고 싶을때
2. 여러 클래스가 의존관계에 있을 때, 이미 존재하는 클래스를 재사용하고자 할 때
3. 테스트를 위해 모의 버전으로 프로바이더를 재정의하려고 할 때

> ModuleMetadata 속 provider 프로퍼티

```ts
export interface ModuleMetadata {
    ...
    providers: Provider[]  // Provider타입을 값으로 갖는 배열타입
}
```

> Provider 타입

```typescript
export declare type Provider<T = any> = 
    Type<any> | ClassProvider<T> | ValueProvider<T> | FactoryProvider<T> | ExistingProvider<T>
```

1. Value Provider

   - `provide`와 `useValue` 속성을 가짐

   ```ts
   export interface ValueProvider<T = any> {
       provider: string | symbol | Type<any> | Abstract<any> | Function // Injection token
       useValue: T
   }
   ```

   - `useValue`는 어떤 타입도 받을 수 있어 외부 라이브러리의 프로바이더를 삽입하거나 모의 객체로 대체할 수 있음

   ```ts
   // 모의 객체
   const mockTestService = {} 
   
   @Module({
       imports: [TestModule],
       providers: [
           {
               provide: TestService,
               useValue: mockTestService
           }
       ]
   })
   ```

   - `useValue`에는 `provide`에 선언된 클래스와 동일한 인터페이스를 가진 리터럴 객체나 new로 생성한 인스턴스를 사용해야함
   - `provide` 토큰을 이름으로 사용하여 프로바이더에 주입받아 사용할 수 있음

   ```ts
   import { connection } from './connection'
   
   @Module({
       provider: [
           {
               provide: 'CONNECTION',  // 원하는 이름으로 토큰이름 지정 
               useValue: connection  // 프로바이더에서 사용할 값
           }
       ]
   })
   ```

   ```ts
   @Injectable()
   export class TestRepository {
       constructor(
       	@Inject('CONNECTION') connection: Connection
       ) {}
   }
   ```

2. Class Provider

   - `useClass` 속성 사용

   ```ts
   export interface ClassProvider<T = any> {
       provider: string | symbol | Type<any> | Abstract<any> | Function // Injection token
       useClass: Type<T>  // 프로바이더 인스턴스
       scope?: Scope
   }
   ```

   - 프로바이더로 사용해야 할 인스턴스를 동적으로 구성 가능

   ```ts
   const configServiceProvider = {
       provider: ConfigService,
       useClass: 
       	process.env.NODE_ENV === 'development'
       		? DevelopmentConfigService
       		: ProductionConfigService
   }
   
   @Module({
       providers: [configServiceProvider]
   })
   ```

3. Factory Provider

   - 클래스 프로바이더와 마찬가지로, 프로바이더 인스턴스를 동적으로 구성하고자 할 때 사용
   - `useFactory` 속성 사용

   ```ts
   export interface FactoryProvider<T = any> {
       provider: string | symbol | Type<any> | Abstract<any> | Function // Injection token
       useFactory: useFactory: (...args: any[]) => T  // 타입을 함수로 정의
       inject?: Array<Type<any> | string | symbol | Abstract<any> | Function>
       scope?: Scope;
   }
   ```

   - 함수를 수행하는 과정에서 다른 프로바이더를 주입 받아 사용할 수 있음
   - 이때, 주입받은 프로바이더를 `inject` 속성에 다시 선언해줘야함

   ```ts
   const connectionFactory = {
       provider: 'CONNECTION',
       useFactory: (optionsProvider: OptionsProvider) => {  // OptionsProvider 주입
           const opitons = optionsProvider.get()
           return new DatabaseConnection(options)
       }, 
       inject: [OptionsProvider]  // 주입한 프로바이더 명시
   }
   
   @Module({
       providers: [connectionFactory]
   })
   ```

4. Alias Provider

   - 프로바이더에 별칭을 붙여 동일한 프로바이더를 별칭으로 접근할 수 있게 해줌
   - `useExisting` 속성 사용

   ```ts
   export interface ExistingProvider<T = any> {
       provider: string | symbol | Type<any> | Abstract<any> | Function // Injection token
       useExisting: any
   }
   ```

   - 싱글턴 스코프일 때만 가능

   ```ts
   // 별칭으로 사용하고 싶은 프로바이더
   @Injectable()
   export class LoggerService {
       private ggg() {
           return 'lll'
       }
   }
   
   // 별칭 프로바이더 설정
   const loggerAliasProvider = {
       provide: 'AliasedLoggerService',
       useExisting: LoggerService
   }
   
   @Module({
       providers: [
           LoggerService,
           loggerAliasProvider
       ]
   })
   ```

   ```ts
   @Controller()
   export class AppController {
       constructor(
       	@Inject('AliasedLoggerService') private readonly serviceAlias: any
       ) {}
   }
   ```

> 프로바이더 내보내기

- 다른 모듈에 있는 프로바이더를 사용하기 위해서는 해당모듈에서 프로바이더를 export 해줘야함
- export에는 토큰, 프로바이더 객체를 사용할 수 있음

```ts
const connectionFactory = {
    provider: 'CONNECTION', ✔️✔️
    useFactory: (optionsProvider: OptionsProvider) => {  // OptionsProvider 주입
        const opitons = optionsProvider.get()
        return new DatabaseConnection(options)
    }, 
    inject: [OptionsProvider]  // 주입한 프로바이더 명시
}

// 토큰 사용
@Module({
    providers: [connectionFactory],
    exports: ['CONNECTION']  ✔️✔️ 
})

// 객체 그대로
@Module({
    providers: [connectionFactory],
    exports: ['connectionFactory']  ✔️✔️ 
})
```

​     

#### Services

- 비지니스 로직 작성

```bash
# Service 파일 자동 생성
$ nest g s 서비스명
```

```typescript
// cats.service.ts
import { Injectable } from '@nestjs/common';
import { Cat } from './interfaces/cat.interface';

@Injectable() ✔️✔️ 
export class CatsService {
  private readonly cats: Cat[] = [];

  create(cat: Cat) {
    this.cats.push(cat);
  }

  findAll(): Cat[] {
    return this.cats;
  }
}

// interfaces/cat.interface.ts
export interface Cat {
  name: string;
  age: number;
  breed: string;
}
```

- service는 controller 클래스의 constructor를 통해 의존성 주입 (DI: Dependency Injection)됨

```typescript
// cats.controller.ts
import { Controller, Get, Post, Body } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';
import { CatsService } from './cats.service';
import { Cat } from './interfaces/cat.interface';

@Controller('cats')
export class CatsController {
  constructor(private catsService: CatsService ✔️✔️) {}

  @Post()
  async create(@Body() createCatDto: CreateCatDto) {
    this.catsService.create(createCatDto);
  }

  @Get()
  async findAll(): Promise<Cat[]> {
    return this.catsService.findAll();
  }
}
```

​    

---

### 3. Module

- `@Module` 데코레이더 사용
- 인수로는 `ModuleMetadata`를 받음

```ts
export declare function Module(metadata: ModuleMetadata): ClassDecorator

export interface ModuleMetadata {
    imports?: Array<Type<any> | DynamicModule | Promise<DynamicModule> | ForwardReference>
    controllers: Type<any>[]
    providers?: Provider[]
    exports?: 
    	Array<DynamicModule | Promise<DynamicModule> | string | symbol | Provider 
          | ForwardReference | Abstract<any> | Function>
}
```

- `import`
  -  해당 모듈에서 사용하기 위한 프로바이더를 가지고 있는 다른 모듈을 가져옴
- `controllers | providers`
  - 모듈 전반에서 컨트롤러와 프로바이더를 사용할 수 있도록 Nest가 객체를 생성하고 주입할 수 있게 해줌
- `export`
  - 해당 모듈에서 제공하는 컴포넌트를 다른 모듈에서 import해서 사용하고자 한다면 export를 해줘야함
  - export로 선언했다는 뜻은 어디에서나 가져다 쓸 수 있다는 의미로, public 인터페이스(API)로 간주

> 모듈은 모듈 간 순환 종속성이 발생하기 때문에 프로바이더처럼 주입해서 사용할 수 없음

​    

>  캡슐화 

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
  exports: [BBBService]  ✔️✔️ 
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

> 전역모듈

- Nest는 모듈 범위 내에서 프로바이더를 캡슐화하므로, 사용하려면 모듈을 먼저 가져와야함
- 하지만, 전역적으로 사용해야하는 프로바이더가 필요한 경우가 있음
- 이때, `@Global` 데코레이터를 사용하여 전역 프로바이더를 만들 수 있음

```ts
@Global()
@Module({
    providers: [CommonService], // 따로 선언 안해도 전역에서 사용가능
    exports: [CommonService]
})

export class CommonModule {}
```

​    

---

### 4. middleware

- 라우트 핸들러가 클라이언트의 요청을 처리하기 이전에 수행되는 함수
- Express의 미들웨어와 동일
- `@Injectable` (DI 가능)

>  미들웨어 사용처

1. 쿠키 파싱 : 쿠키를 파싱하여 사용하기 쉬운 데이터 구조로 변경
2. 세션 관리 : 세션 쿠키를 찾아 세션 상태를 조회해 request에 세션 정보를 추가하여 다른 핸들러가 세션 객체를 이용할 수 있게 해줌
3. 인증 / 인가 : 사용자가 서비스에 접근 가능한 권한이 있는지 확인 (Nest는 인가를 구현할 때는 `Guard` 사용을 권장)
4. 본문 파싱 : body로 들어오는 JSON 이외의 데이터를 해석하여 매개변수에 넣는 작업 수행

> 전역 적용

- 함수로 만든 미들웨어는 프로바이더를 주입받아 사용할 수 없는 단점이 있음

```ts
// loggerFun.middleware.ts
import { Request, Response, NextFunction } from 'express'

export function loggerFun(
    req: Request,
    res: Response,
    nest: NextFunction
) {
    // 미들웨어 로직 실행
    next() // 미들웨어 종료
}
```

```ts
// main.ts
import { loggerFunc } from '...'

async function bootstrap() {
    const app = await NestFactory.create(AppModule)
    app.use(loggerFunc) ✔️✔️
    await app.listen(3000)
}

bootstrap()
```

​    

#### Logger Middleware

- `NestMiddleware` 인터페이스를 구현한 클래스로 미들웨어 작성가능

```ts
// logger.middleware.ts
import { Injectable, NestMiddleware } from '@nestjs/common'
import { Request, Response, NextFunction } from 'express'

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
    use(
    	req: Request,
    	res: Response,
    	nest: NextFunction
    ) {
    	this.logger.log(req)  // 미들웨어 로직 실행
        ...
        next() // 미들웨어 종료
    }
}
```

```ts
// app.module.ts
import { MiddlewareConsumer, Module, NestModule } from '@nestjs/common'

@Module()
export class AppModule implements NestModule {
    configure(consumer: MiddlewareConsumer): any {
        consumer
        	.apply(LoggerMiddleware)
        	.forRoutes('*') // 전체 엔드포인트에서 실행 
          // .forRoutes('/test') // `/test` 경로로 들어오는 요청 수행시 먼저 실행
    }
}
```

> MiddlewareConsumer 객체

- MiddlewareConsumer  객체를 이용하여 미들웨어를 어디에 적용할 지 관리할 수 있음
- `apply` 메서드의 인수 순서대로 미들웨어가 실행됨

```typescript
apply(...middleware: (Type<any> | Function)[]): MiddlewareConfigProxy;
```

```ts
import { MiddlewareConsumer, Module, NestModule } from '@nestjs/common'

@Module()
export class AppModule implements NestModule {
    configure(consumer: MiddlewareConsumer): any {
        consumer
        	.apply(LoggerMiddleware, LoggerMiddleware2, LoggerMiddleware3) ✔️✔️
       		.forRoutes('/test')
    }
}
```

- `forRoutes` 메서드는 `apply`함수의 리턴타입인 `MiddlewareConfigProxy`에 정의

```ts
export interface MiddlewareConfigProxy {
    exclude(...routes: (string | RouteInfo)[]): MiddlewareConfigProxy;
    forRoutes(...routes: (string | Type<any> | RouteInfo)[]): MiddlewareConsumer;
}
```

- `forRoute`의 인수로 문자열 형식의 경로를 직접주거나, 컨트롤러 클래스 이름, RouteInfo 객체를 넘길 수 있음
- 보통 컨트롤러 클래스를 많이 활용

```ts
import { MiddlewareConsumer, Module, NestModule } from '@nestjs/common'

@Module()
export class AppModule implements NestModule {
    configure(consumer: MiddlewareConsumer): any {
        consumer
        	.apply(LoggerMiddleware, LoggerMiddleware2, LoggerMiddleware3) 
       		.forRoutes(TestController) ✔️✔️
    }
}
```

- `exclude` 함수는 미들웨어를 적용하지 않을 라우팅 경로를 설정

```ts
import { MiddlewareConsumer, Module, NestModule } from '@nestjs/common'

@Module()
export class AppModule implements NestModule {
    configure(consumer: MiddlewareConsumer): any {
        consumer
        	.apply(LoggerMiddleware, LoggerMiddleware2, LoggerMiddleware3) 
        	.exclude({ path: '/nest', method: RequestMethod.GET }) // /nest경로로 Get요청을 보내면 미들웨어 무시됨
       		.forRoutes(TestController) 
    }
}
```

​       

---

### 5. Guard

- 인증은 주로 `Middleware`로 인가는 `Guard`를 이용하여 구현
- 미들웨어는 실행 컨텍스트(ExecutionContext)에 접근할 수 없고, 다음에 어떤 핸들러가 실행될 지 알 수 없음
- 가드는 실행 컨텍스트 인스턴스에 접근할 수 있어서, 다음 실행될 작업을 정확히 알 수 있음

> 인가 (Authorization) : 인증을 통과한 유저가 요청한 기능을 사용할 권한이 있는지 판별하는 것



#### Guard 구현

```ts
import { CanActivate, ExecutionContext, Injectable } from '@nestjs/common'
import { Observable } from 'rxjs'

@Injectable()
export class TestGuard implements CanActivate {
    canActivate(context: ExecutionContext): boolean | Promise<boolean> | Observable<boolean> {
        const request = context.switchToHttp().getRequest()
    }
}
```

- `canActivate`함수는 `ExecutionContext`인스턴스를 인수로 받음
- `ExecutionContext`는 `ArgumentHost`를 상속받고, `request`와 `response`에 대한 정보를 가지고 있음
- `switchToHttp()`함수를 사용해 필요한 정보를 가져올 수 있음

```typescript
export interface ExecutionContext extends ArgumentHost {
    getClass<T = any>(): Type<T>
    getHandler(): Function
}

export interface ArgumentHost {
    getArgs<T extends Array<any> = any[]>(): T
    getArgByIndex<T = any>(index: number): T
    switchToRpc(): RpcArgumentsHost
    switchToHttp(): HttpArgumentsHost
    switchToWs(): WsArgumentsHost
    getType<TContext extends string = ContextType>(): TContext
}

export interface HttpArgumentsHost {
    getRequest<T = any>(): T
    getResponse<T = any>(): T
    getNext<T = any>: T
}
```



#### Guard 적용

- `Controller`범위 또는 `method` 범위에 적용가능
- `UseGuards(TestGuard)`와 같이 적용함, 이 때 `AuthGuard`인스턴스의 생성은 Nest가 맡아서 진행
- 여러 종류의 가드를 적용하려면 `,` 를 이용하여 이어서 선언

```ts
@UseGuards(TestGuard)  // 클래스 범위 적용
@Controller()
export class AppController {
    constructor(private readonly appService: AppService) {}
    
    @UseGuards(TestGuard)  // 메서드 범위 적용
    @Get()
    ttt() {
        return this.appService.qqq()
    }
}
```

> 전역으로 가드 적용

```typescript
async function bootstrap() {
    const app = await NestFactory.create(AppModule)
    app.useGlobalGuards(new TestGaurd()) ✔️✔️
    await app.listen(3000)
}
bootstrap()
```

> 가드에 종속성 주입을 사용해 다른 프로바이더를 사용하고 싶을 때 커스텀 프로바이더로 선언

```ts
// app.module.ts
import { APP_GUARD } from '@nestjs/core'

@Module({
    providers: [
        {
            provide: APP_GUARD,
            useClass: TestGuard
        }
    ]
})
```

​    

---

### 6. Interceptors

- request와 response를 가로채 변형을 가할 수 있는 컴포넌트
- `@Injectable` 데코레이터 사용, DI 가능
- 관점 지향 프로그래밍에서 영향을 많이 받음
  - 메서드 실행 전/후 추가로직 바인딩
  - 함수 반환 결과 변환
  - 함수에서 던져진 예외 변환
  - 기본 기능 동작 확장
  - 특정 조건에 따라 기능 완전 재정의 (캐싱)
  - 핵심기능에서 재사용이 가능한 부분들을 하나의 모듈로 묶기
- 미들웨어와 수행하는 일이 비슷하지만, 수행 시점의 차이가 존재
- 미들웨어는 라우트 핸들러로 전달되기 전에 동작, 인터셉트는 요청에 대한 라우트 핸들러 처리 전/후 호출되어 요청과 응답을 다를 수 있음

```typescript
// logging.interceptor.ts
import { Injectable, NestInterceptor, ExecutionContext, CallHandler } from '@nestjs/common';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  // NestInterceptor 인터페이스는 intercept함수를 구현해야함
  intercept(context: ExecutionContext, next: CallHandler): Observable<any> { 
    console.log('Before...')  // 컨트롤러 이전에 실행됨 (pre-controller)
    const now = Date.now()

    return next
      .handle()
      .pipe(  // 컨트롤러 이후에 실행됨 (post-controller)
        tap(() => console.log(`After... ${Date.now() - now}ms`))
      );
  }
}
```

> 전역 적용

```ts
async function bootstrap() {
    const app = await NestFactory.create(AppModule)
    app.useGlobalInterceptors(new LoggingInterceptor())  ✔️✔️
    await app.listen(3000)
}
```

> 특정 컨트롤러 / 메서드 적용

```ts
@UseInterceptors(LoggingInterceptor)
@Get('/test')
test() {}
```

> NestInterceptor의 정의

```ts
// NestInterceptor
import { NestInterceptor, ExecutionContext, CallHandler } from '@nestjs/common';

export interface NestInterceptor<T = any, R = any> {
    intercept(
    	context: ExecutionContext,
    	next: CallHandler<T>
    ): Observable<R> | Promise<Observable<R>>
}

// CallHandler
import { Observable } from 'rxjs';

export interface CallHandler<T = any> {
    handle(): Observable<T>
}
```

- `CallHandler` 인터페이스는 `handle()`메서드를 구현해야함
- `handle` 메서드는 라우트 핸들러에서 전달된 응답 스트림을 돌려주고 `RxJs`의 `Observable`로 구현되어 있음
- 인터셉터에서 핸들러가 제공하는 `handle()`메서드를 호출하지 않으면 라우터 핸들러가 동작하지 않음
- `handle()`메서드를 호출하고 Observable을 수신한 후에 응답 스트림에 추가 작업을 수행할 수 있음

> 응답 매핑

- 응답에 변형을 가하는 커스텀 인터셉터

```ts
import { CallHandler, ExecutionContext, Injectable, NestInterceptor } from '@nestjs/common'
import { Observable } from 'rxjs'
import { map } from 'rxjs/operators'

export interface Response<T> {
    data: T
}

@Injectable()
export class TransformInterceptor<T> implements NestInterceptor<T, Response<T>> {
    interceptor(context: ExecutionContext, next: CallHanlder): Observable<Response<T>> {
        return next
        	.handle()
        	.pipe(map((data) => return { data })
    }
}
```

- 전역 적용

```ts
async function bootstrap() {
    const app = await NestFactory.create(AppModule)
    app.useGlobalInterceptors(new TransformInterceptor())  ✔️✔️
    await app.listen(3000)
}
```

​    

### 7.  Pipes

- 클라이언트 요청에서 들어오는 데이터를 유효성 검사 및 변환을 수행해 서버가 원하는 데이터를 얻을 수 있도록 도와주는 클래스
- 사용사례
  - 변환 (transformation) : 입력데이터를 원하는 형식으로 변환
  - 유효성 검사 (validation) : 입력데이터 평가, 데이터가 올바르지 않으면 예외 발생

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

- `ParseIntPipe`, `ParseBoolPipe`, `ParseArrayPipe`, `ParseUUIDPipe`는 전달된 인수의 타입을 검사함

```ts
// controller.ts
@Get(':id')
getData(@Param('id', ParseIntPipe) param: number) {}
```

- 생성할 파이프 객체의 동작을 원하는 대로 커스텀하고 싶을 경우, 클래스를 전달하지 않고 파이프 객체를 직접 생성하여 전달할 수도 있음

```ts
// controller.ts
@Get(':id')
getData(@Param('id', new ParseIntPipe({ errorHttpStatusCode: HttpStatus.NOT_ACCEPTABLE })) param) {}
```

- `DefaultValuePipe`는 인수의 값에 기본값을 설정할 때 사용

```ts
@Get()
findAll(
	@Query('offset', new DefaultValuePipe(0), ParseIntPipe) offset: number;
    @Query('limit', new DefaultValuePipe(10), ParseIntPipe) limit: number;
) {}
```



#### 커스텀 파이프

- ❗`ValidationPipe`는 Nest에 이미 구현되어 있음 

> 전역 적용

```ts
import { ValidationPipe } from '@nestjs/common'

async function bootstrap() {
    const app = await NestFactory.create(AppModule)
    app.useGlobalPipes(new ValidationPipe({
        transform: true  // class-transform을 적용하려면 true로 지정해줘야함
    }))
    await app.listen(3000)
}
```

​    

> 동작원리

- `PipeTransfrom` 인터페이스를 상속받는 클래스에 `@Injectable` 데코레이터를 붙임

```ts
// validation.pipe.ts
import { PipeTransform, Injectable, ArgumentMetadata } from '@nestjs/common'

@Injectable()
export class ValidationPipe implements PipeTransfrom {
    transform(value: any, metadata: ArgumentMetadata) {
        return value
    }
}
```

```ts
// PipeTransform
export interface PipeTransform<T = any, R = any> {
	transform(
    	value: T, // 현재 파이프에 전달된 인스
         metadata: ArgumentMetadata  // 현재 파이프에 전달된 인수의 메타데이터
     ): R
}
```

```ts
// ArgumentMetadata
export interface ArgumentMetadata {
    readonly type: Paramtype  // 파이프에 전달된 인수 종류
    readonly metatype?: Type<any> | undefined  // 라우트 핸들러에 정의된 인수 타입, 핸들러타입을 생략하거나 바닐라 JS 사용시 undefined
    readonly data?: string | undefined  // 데코레이터에 전달된 문자열, 매개변수의 이름
}

export declare type Paramtype = 'body' | 'query' | 'param' | 'custom'
```

```ts
// 예시
@Get(':id')
findOne(@Param('id', ValidationPipe) id: number) {
    return ...
}

// transform 함수에 전달된 인수 출력시
value = 1
metadata = {
    metatype: [Function: Number],
    type: 'param',
    data: 'id'
}
```



#### 유효성검사 파이프 구현

```ts
import { PipeTransform, Injectable, ArgumentMetadata, BadRequestException } from '@nestjs/common'
import { validate } from 'class-validator'
import { plainToClass } from 'class-transformer'

@Injectable()
export class ValidationPipe implements PipeTransform<any> {
    async transform(value: any, { metatype }: ArgumentMetadata) {
        if (!metatype || !this.toValidate(metatype)) return value  // 전달된 metatype이 파이프가 지원하는 타입인지 검사
        const object = plainToClass(metatype, value)  // 순수 자바스크립트 객체를 클래스 객체로 바꿔줌
        const errors = await validate(object) 
        if (errors.length > 0) throw new BadRequestException('Validation failed')        
        return value
    }
    
    private toValidate(metatype: Function): boolean {
        const types: Function[] = [String, Boolean, Number, Array, Object]
        return !types.includes(metatype)
    }
}
```

- 구현한 `ValidationPipe` 적용

```ts
@Post()
create(@Body(ValidationPipe) createTestDto: CreateTestDto) {
    return ...
}
```



#### 유효성검사 적용

`UsePipes` 데코레이터와 `class-validator`와 `class-transformer` 라이브러리를 이용하여 커스텀 파이프를 바인딩

```bash
$ yarn add class-validator class-transformer
```

- 전역 적용

```ts
import { ValidationPipe } from '@nestjs/common'

async function bootstrap() {
    const app = await NestFactory.create(AppModule)
    app.useGlobalPipes(new ValidationPipe({
        transform: true  // class-transform을 적용하려면 true로 지정해줘야함
    }))
    await app.listen(3000)
}
```

-  DTO에 `class-validator`와 `class-transformer` 적용

```ts
import { IsEmail, IsString, Matches, MaxLength, MinLength } from 'class-validator'
import { Transform } from 'class-transformer'

export class CreateTestDto {
    @Transform(params => params.value.trim()) 
    @IsString()
    @MinLength(2)
    @MaxLength(30)
    readonly name: string
    
    @IsString()
    @IsEmail()
    @MaxLength(60)
    readonly email: string
    
    @IsString()
    @Matches(/^[A-Za-z\d!@#$%^&*()]{8,30}$/)
    readonly password: string
}
```

> `class-validator` 데코레이터

- primitive 타입

| 데코레이터                          | 설명                                                |
| ----------------------------------- | --------------------------------------------------- |
| @IsEmpty()                          | null, undefined, ""인지 확인                        |
| @IsNotEmpty()                       | null, undefined, ""이 아닌지 확인                   |
| @IsString()                         | string타입인지 확인                                 |
| @IsBoolean()                        | boolean타입인지 확인                                |
| @IsNumber(options: IsNumberOptions) | number타입인지 확인                                 |
| @IsInt()                            | integer타입인지 확인                                |
| @IsDate()                           | Date타입인지 확인                                   |
| @Contains(seed: string)             | 문자열에 매개변수로 주어진 seed값이 포함인지 확인   |
| @NotContains(seed: string)          | 문자열에 매개변수로 주어진 seed값이 미포함인지 확인 |
| @Min(min: number)                   | min 값보다 크거나 같은지 확인                       |
| @Max(max: number)                   | max 값보다 작거나 같은지 확인                       |
| @MinLength(min: number)             | 문자열의 최소 길이 확인                             |
| @MaxLength(max: number)             | 문자열의 최대 길이 확인                             |
| @Length(min: number, max?: number)  | 문자열 길이의 최대 최소 확인                        |
| @IsEmail(options?: IsEmailOptions)  | 문자열이 이메일인지 확인                            |

- Reference 타입

| 데코레이터                            | 설명                                       |
| ------------------------------------- | ------------------------------------------ |
| @IsArray()                            | 배열타입인지 확인                          |
| @IsObject()                           | 문자열이 객체인지 확인                     |
| @IsIn(values: any[])                  | 주어진 값이 values 배열에 있는지 확인      |
| @IsNotIn(values: any[])               | 주어진 값이 values 배열에 없는지 확인      |
| @ArrayNotEmpty()                      | 배열이 빈 배열이 아닌지 확인               |
| @ArrayUnique(identifier?: (O) => any) | 배열에 있는 모든 값들이 고유한 값인지 확인 |

- 기타 데코레이터

| 데코레이터                                    | 설명                                       |
| --------------------------------------------- | ------------------------------------------ |
| @Matches(pattern: RegExp, modifiers?: string) | 문자열이 정규표현식에 매치되는 값인지 확인 |
| @IsAlpha()                                    | 문자열이 a-zA-z로만 되어 있는지 확인       |
| @IsAlphanumeric()                             | 문자열이 숫자나 알파벳인지 확인            |
| @IsAscii()                                    | 문자열이 ASCII 문자인지 확인               |
| @IsFQDN(options?: IsFQDNOptions)              | 문자열이 도메인 주소인지 확인 (aaa.com)    |
| @IsIP(version?: "3" \| "6")                   | 문자열이 IP주소인지 확인 (3 or 6)          |
| @IsJson()                                     | 문자열이 유효한 JSON인지 확인              |

> `class-transformer`

- `@Transform` 데코레이터

```ts
export default function Transform(
	transformFn: (params: TransformFnParams) => any,
	options?: TransformOptions
): PropertyDecorator

export interface TransformFnParams {
    value: any
    key: string
    obj: any
    type: TransformationType
    options: ClassTransformOptions
}
```

- 데코레이터가 적용되는 속성의 값(value)과 그 속성을 가지고 있는 객체(obj)등을 인수로 받아 속성을 변형한 후 리턴하는 함수인 `transformFn`을 인수로 받음

```ts
// DTO
@Transform(params => {
    console.log(params)
    return params.value
})
@IsString()
@Length(2, 30)
readonly name: string

...
readonly email: string
readonly password: string

// Post요청
{
    "name": "이름",
    "email": "test@email.com",
    "password": "crud1234"
}

// Tranform 함수 params 출력
{
    value: "이름",
    key: "name",
    object: {
        "name": "이름",
        "email": "test@email.com",
        "password": "crud1234"
    },
    type: 0,
    options: {
        enableCircularCheck: false,
        enableImplicitConversion: false,
        excludeExtraneousValues: false,
        excludePrefixes: undefined,
        exposeDefaultValues: false,
        exposeUnsetFields: true,
        groups: undefined,
        ignoreDecorators: false,
        strategy: undefined,
        targetMaps: undefined,
        version: undefined
    }
}
```

- obj 속성을 이용한 유효성 검사

```ts
@Transform({ value, obj }) => {
    if (obj.password.includes(obj.name.trim())) 
        throw new BadRequestException('password는 name과 같은 문자열을 포함할 수 없습니다.')
    return value.trim()
}
```

​    

#### 커스텀 유효성검사

- 직접 유효성 검사를 수행하는 데코레이터 생성하여 활용
- Nest의 기술이 아니고 class-validator의 영역이지만 유용함

```ts
// not-in.ts
import { 
    registerDecorator, 
    ValidationOptions, 
    ValidationArguments, 
    ValidationConstraint, 
    ValidatorContrainInterface
} from 'class-validator'

// 데코레이터 인수는 객체에서 참조하려고 하는 다른 속성의 이름과 ValidationOptions를 받음
export function NotIn(property: string, validationOptions?: ValidationOptions) { 
  
  // registerDecorator를 호출하는 함수 리턴, 인수로 데커레이터가 선언될 객체와 속성이름을 받음
  return (object: Object, propertyName: string) => { 
    registerDecorator({  // ValidationDecoratorOptions 객체를 인수로 받음
      name: 'NotIn',  // 데커레이터 이름
      target: object.constructor,  // 데코레이터 객체가 생성될 때 적용
      propertyName,  
      options: validationOptions,  // 유효성 옵션은 데코레이터의 인수로 전달받은 것을 사용
      constraints: [property],  // 속성에 적용되도록 제약 부여
       
      // 가장 중요한 유효성 검사 규칙 기술, ValidatorConstraint Interface를 구현한 함수
      validator: {
        validate(value: any, args: ValidationArguments) {
            const [relatedPropertyName] = args.constraints
            const relatedValue = (args.object as any)[relatedPropertyName]
            return typeof value === 'string' && typeof relatedValue === 'string' && !relatedValue.includes(value)
        }
      }
    })   
  }
}
```

```ts
// 활용
@NotIn('password', { message: "password는 name과 같은 문자열을 포함할 수 없습니다." })
name: string
```



---

### 8. Exception filters

- Nest는 프레임워크 내에 예외 레이어를 두고 있어 이 곳에서 애플리케이션이 실행중 제대로 처리하지 못한 예외를 처리함
- Nest는 예외에 대한 많은 클래스를 제공함
- Nest에서 제공하는 기본 예외 클래스는 모두 생성자가 같은 모양을 가짐

```ts
constructor(objectOrError?: string | object | any, description: string)
```

- 에러를 처리할 때 기본으로 내장된 전역 예외필터가 JSON 형식으로 바꿔줌
- 내장 예외 필터는 인식할 수 없는 에러를 `InternalServerErrorException`으로 변환

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

- 대부분의 에러는 `HttpException`을 상속받고, 이는 다시 `Error`를 상속받음
- 모든 예외는 `Error`객체로 부터 파생됨

```ts
export declare class HttpException extends Error {
    constructor(
    	response: string | Record<string, any>,  // JSON 응답 본문
    	status: number  // 에러 속성을 나타내는 HTTP 상태코드
    );
}
```

- Nest에서 제공하는 모든 예외들도 `HttpException`을 상속받고 있음

```ts
import { HttpStatus } from '@nestjs/common'

@Get()
aaa() {
  throw new HttpException({
    status: HttpStatus.FORBIDDEN,
    error: '에러메시지'
  }, HttpStatus.FORBIDDEN)
}
```

​    

#### 커스텀 예외처리 필터

- Nest에서 제공하는 전역 예외 필터외에 직접 예외 필터 레이어를 둬, 원하는 대로 예외를 다루고 싶을 때
- 예외가 일어났을 때 로그를 남기거나 응답 객체를 원하는 대로 변경하고자 할 때 사용

```typescript
// http-exception.filter.ts
import { ExceptionFilter, Catch, ArgumentsHost, HttpException,  } from '@nestjs/common';
import { Request, Response } from 'express';

@Catch(HttpException)  // @Catch 데코레이터는 처리되지 않는 모든 예외를 잡으려고 할 때 사용
export class HttpExceptionFilter implements ExceptionFilter {
  catch(exception: HttpException, host: ArgumentsHost) {
    const ctx = host.switchToHttp()
    const res = ctx.getResponse<Response>()
    const req = ctx.getRequest<Request>()
    const status = (exception as HttpException).getStatus()
    const response = (exception as HttpException).getResponse()

    if (!(exception instanceof HttpException)) {
        exception = new InternalServerErrorException()
    }
    
    res
      .status(status)
      .json({
        statusCode: status,
        timestamp: new Date().toISOString(),
        path: req.url,
        response
      });
  }
}
```

> 특정 엔드포인트 적용

```ts
@Controller('test')
export class TestController {
    @UseFilters(HttpExceptionFilter) ✔️✔️ 
    @Post()
    test(@Body() testDto: TestDto) {
      throw new UnauthorizedException()
    }
}
```

> 특정 컨트롤러 전체 적용

```ts
@Controller('test')
@UseFilters(HttpExceptionFilter) 
export class TestController {
    ...
}
```

> 전역 적용

```ts
// main.ts
async function bootstrap() {
  ...
  app.useGlobalFilters(new HttpExceptionFilter())
  ...
}
```

- 부트스트랩 과정에서 전역필터 적용시 필터에 의존성 주입을 할 수 없음
- 의존성 주입을 받고자 한다면 예외필터를 커스텀 프로바이더로 등록해야함

```ts
import { APP_FILTER } from '@nestjs/core'

@Module({
    providers: [
        {
            provide: APP_FILTER,
            useClass: HttpExceptionFilter
        }
    ]
})
```

```ts
export class HttpExceptionFilter implements ExceptionFilter {
    constructor(private logger: Logger)  ✔️✔️ // Logger 객체 의존성 주입
}
```

> Logger 모듈과 연계

- ExceptionModule 생성

```ts
import { Logger, Module } from '@nestjs/common'
import { APP_FILTER } from '@nestjs/core'
import { HttpExceptionFilter } from './http-exception.filter'

@Module({
    providers: [
        Logger,
        {
            provide: APP_FILTER,
            useClass: HttpExceptionFilter
        }
    ]
})
```

- AppModule에 import

```ts
import { ExceptionModule } from './exception/ExceptionModule'

@Module({
    imports: [
        ExceptionModule
    ]
})
```

```ts
// http-exception.filter.ts
import { ExceptionFilter, Catch, ArgumentsHost, HttpException,  } from '@nestjs/common';
import { Request, Response } from 'express';

@Catch(HttpException) 
export class HttpExceptionFilter implements ExceptionFilter {
  constructor(private logger: Logger) {}
    
  catch(exception: HttpException, host: ArgumentsHost) {
    ...
    const stack = exception.stack
 	this.logger.log({
        timestamp: new Date(),
        url: req.url,
        response,
        stack
    })
    ...
  }
}
```

​     

---

## 2️⃣ Configuration 

- nestjs는 `dotenv`패키지를 내부적으로 사용하는 `@nestjs/config`패키지를 제공

```bash
$ yarn add @nestjs/config
```

```typescript
// app.module.ts
import { ConfigModule } from '@nestjs/config'

@Module({
  imports: [
    ConfigModule.forRoot({  
      // ConfigModuleOptions
      isGlobal: true,  // 전역에서 사용가능
    })
  ]
})
```

- forRoot는 DynamicModule을 리턴하는 정적메서드

```ts
static forRoot(options?: ConfigModuleOptions): DynamicModule
```

- 동적 모듈을 작성할 때 forRoot대신 다른 이름 써도 되지만, 관례적으로 forRoot나 register를 사용
- 비동기함수일 경우에는 forRootAsync, registerAsync 사용

> ConfigModuleOptions

```ts
export interface ConfigModuleOptions {
    cache?: boolean;  // 메모리 환경변수를 캐시할지 여부, 애플리케이션 성능을 향상시켜줌
    isGlobal?: boolean; // true이면 global module로 등록되어 다른 모듈에서 따로 import 안해줘도 사용가능
    load?: Array<ConfigFactory>;  // 커스텀 환경 설정파일 로딩시에 사용 (ts, yaml)
    envFilePath?: string | string[];  // 환경변수 파일들의 경로
    ignoreEnvFile?: boolean; // true이면 .env파일 무시
    ignoreEnvVars?: boolean;  // true이면 환경변수 무효처리
    endcoding?: string;  // 환경변수 파일 인코딩
    validate?: (config: Record<string, any>) => Record<string, any>; // 환경변수 유효성 검증함수
    validationSchema?: any;  
    validationOptions?: Record<string, any>;
    expandVariables?: boolean;
}
```

> 환경변수 적용

```bash
# .env
TEST_URI=https://test.com
```

- 환경변수 주입받아 사용

```typescript
// 환경변수 사용
const BASE_URI = process.env.TEST_URI
```

- ConfigService 주입 받아 사용

```ts
// test.controller.ts
import { ConfigService } from '@nestjs/config'

@Controller()
export class TestController {
    constructor(private configService: ConfigService) {}  // ConfigService 주입
    
    @Get()
    ttt() {
        return this.configService.get('TEST_URI')
    }
}
```



> 개발환경별 환경변수 설정

- `envs` 폴더 생성

```bash
폴더구조
```

- package.json scripts 수정

```json
// package.json
// Window
"scripts": {
    dev: "set NODE_ENV=dev && nest start --watch"
    staged: "set NODE_ENV=staged && node dist/main"
    prod: "set NODE_ENV=prod && node dist/main"
}

// Mac, Linux
"scripts": {
    dev: "NODE_ENV=dev nest start --watch"
    staged: "NODE_ENV=staged node dist/main"
    prod: "NODE_ENV=prod node dist/main"
}
```

- 환경별로 `.env` 파일 작성

```json
// envs/dev.env
TEST_URI=http:localhost:3000

// envs/staged.env
TEST_URI=https://staged.abc100.com

// envs/prod.env
TEST_URI=https://abc100.com
```

- app.module에 `envFilePath` 설정

```ts
// app.module.ts
import { ConfigModule } from '@nestjs/config'
import { join } from 'path';

@Module({
  imports: [
    ConfigModule.forRoot({  
      isGlobal: true,
      envFilePath: join(process.cwd(), '/envs/', `${process.env.NODE_ENV}.env`) // 오류날 경우 process.env.NODE_ENV에 trim() 메서드
    })
  ]
})
```



### 커스텀 Config 파일

- 환경변수를 가져다 쓸 때 의미 있는 단위로 묶어서 처리하고 싶을때 사용
- `registerAs` 함수를 사용하여 구현

```ts
// testConfig.ts
import { registerAs } from '@nestjs/config'

export default registerAs('KEY', () => ({
    test1: process.env.TEST_URI,
    test2: {
        subTest1: process.env.TEST_TEST
        subTest2: process.env.TEST_SUBTEST
    }
}))
```

- `nest-cli.json`파일에서 옵션 변경

```json
// nest-cli.json
{
    ...
    conpilerOptions: {
        "assets": [
            {
                "include": './envs/*.env',
                "outDir": "./dist"
            }
        ]
    }
}
```

- `joi`를 사용하여 유효성검사 진행

```ts
import * as Joi from 'Joi'

export const validationSchema = Joi.object({
    TEST_URI: Joi.string().required().uri()
})
```

- app.module에 `load`와 `validationSchema` 설정

```ts
// app.module.ts
import { ConfigModule } from '@nestjs/config'
import { join } from 'path';
import testConfig from './envs/config/testConfig'
import { validationSchema } from './envs/config/validationSchema'

@Module({
  imports: [
    ConfigModule.forRoot({  
      isGlobal: true,
      envFilePath: join(process.cwd(), '/envs/', `${process.env.NODE_ENV}.env`) // 오류날 경우 process.env.NODE_ENV에 trim() 메서드
      load: [testConfig]  ✔️✔️
      validationSchema  // joi를 통해 유효성 검사
    })
  ]
})
```

- 설정완료된 testConfig 주입받아 사용

```ts
import { Config}

@Injectable()
export class TTService {
    constructor(
    	@Inject(testConfig.KEY) private config: ConfigType<typeof testConfig>
    ) {}
         
    qqq() {
    	const a = this.config.test1
    	const b = this.config.test2.subTest1
    }
}
```

​     

---

## 3️⃣ 요청 생명주기

- 들어오는 요청이 어떤 컴포넌트를 거쳐 처리되고, 생성된 응답이 어떤 컴포넌트를 거쳐 처리되는지를 의미

![KakaoTalk_20230901_211833732](Nest(1).assets/KakaoTalk_20230901_211833732.jpg)

![KakaoTalk_20230901_212008663](Nest(1).assets/KakaoTalk_20230901_212008663.jpg)

1. 미들웨어

   1. 전역에서 바인딩된 미들웨어 실행
   2. 모듈에서 바인딩되는 미들웨어 실행
   3. 다른 모듈에 바인딩되어 있는 미들웨어들이 있으면 먼저 루트 모듈에 바인딩된 미들웨어를 실행하고, imports에 정의한 순서대로 실행

2. 가드

   1. 전역에서 바인딩된 가드 실행
   2. 컨트롤러에 정의된 순서대로 가드 실행

   ```ts
   // Guard1, Guard2, Guards3 순서대로 실행됨
   @UseGuards(Guard1, Guard2)
   @Controller('test')
   export class TestController {
       constructor(private testService: TestService) {}
       
       @UseGuards(Guards3)
       @Get()
       ttt() {
           return ...
       }
   }
   ```

3. 인터셉터

   - `RxJS`의 `Observable`객체를 반환하는데, 이 객체는 요청의 실행 순서와 반대 순서로 동작
   - 요청은 전역 > 컨트롤러 > 라우터 순으로 동작
   - 응답은 라우터 > 컨트롤러 > 전역 순으로 동작

4. 파이프

   - 동작하는 순서가 독특함
   - 파이프가 적용된 라우터의 매개변수가 여러 개 있을 때는 정의한 순서의 역순으로 적용됨

   ```ts
   @UsePipes(GeneralValidationPipe)
   @Controller('test')
   export class TestController {
       constructor(private testService: TestService) {}
       
       @UsePipes(RouteSpecificPipe)
       @Patch(':id')
       testTTT(
       	@Body() body: TestDto,
       	@Param() params: TestParams,
       	@Query() query: TestQuery
       ) {
           return ...
       }
   }
   ```

   - `GeneralValidationPipe` > `RouteSpecificPipe`순으로 적용
   - ❗매개변수는 `query` > `params` > `body` 순으로 적용
   - `GeneralValidationPipe`가  `query` > `params` > `body`의 순서대로 적용된 후,  `RouteSpecificPipe` 가  `query` > `params` > `body`로 적용됨

5. 예외필터

   - 라우터 > 컨트롤러 > 전역으로 바인딩된 순서대로 동작
