# Nest (3)

Schema-First : typeDefs를 직접 작성하는 방식

Code-First : 타입스크립트가 적용된 코드를 작성하면 자동으로 Schema 생성 (Nest.js에서 사용됨)

## 1️⃣ ORM

- 객체 관계 매핑 (Object-Relational mapping)
- DB의 관계를 객체로 바꿔 개발자가 DB를 쉽게 다룰 수 있도록 도와주는 도구
- ORM에서 제공하는 인터페이스를 통해 일반적인 라이브러리를 호출하듯 DB에 데이터를 업데이트하고 조회할 수 있음

​    

### 1. TypeORM

#### 설치 / 설정

```bash
$ yarn add typeorm @nestjs/typeorm mysql2
```

```typescript
// app.module.ts
@Module({
  imports: [
    TypeOrmModule.forRoot({
      // 기본설정
      type: (process.env.DATABASE_TYPE || 'mysql') as 'mysql',
      host: process.env.DATABASE_HOST, // Docker 사용시 네임리졸류션 사용
      port: Number(process.env.DATABASE_PORT),
      username: process.env.DATABASE_USERNAME, // 로그인 유저
      password: process.env.DATABASE_PASSWORD, // 로그인 비밀번호
      database?: process.env.DATABASE_DATABASE, // DB이름, DB가 존재해야 정상적으로 연결됨
        
      // entity 클래스 개별지정
      entities: [
          Test1,
          Test2
      ],
        
      // entity 경로지정
      entities: [__dirname + '/**/*.entity{.ts,.js}']
        
      // 개발중에 유용한 옵션들
      logging: true  // SQL 실행 로그 확인
      synchronize: true
    })
  ]
})
```

```json
// env 파일
DATABASE_TYPE=mysql
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USERNAME=root
DATABASE_PASSWORD=rootPw
DATABASE_DATABASE=dbName
```

> DB별 타입 (`type`)

| 이름       | 타입       |
| ---------- | ---------- |
| MySQL      | 'mysql'    |
| PostgreSQL | 'postgres' |
| SQLite     | 'sqlite'   |

> synchronize

- 서비스 구동시 엔티티 객체를 읽어 DB 스키마들 만들거나 변경해줌
- 프로덕션 레벨에서는 데이터가 삭제될 수 있기 때문에 true로 지정하면 안됨

> 추가적으로 사용가능한 옵션 (`TypeOrmModuleOptions 객체`)

```typescript
export declare type TypeOrmModuleOptions = {
    retryAttempts?: number;
    retryDelay?: number;'
    toRetry?: (err: any) => boolean;
    autoLoadEntities?: boolean;
    keepConnectionAlive?: boolean;
} & Partial<DataSourceOptions>
```

- `keepConnectionAlive` : 애플리케이션 종료 후에도 연결을 유지할 지 여부
- `autoLoadEntities` : 엔티티를 자동으로 로드할지 여부
- `retryAttempts` : 연결시 재시도 횟수, 기본값은 10
- `retryDelay` : 재시도 간의 지연시간 (ms), 기본값은 3000
- `toRetry` : 에러가 났을 때 연결을 시도할지 판단하는 함수

​    

#### Entity

- DB는 단수형 명사 사용
- 테이블의 schema

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



#### DB 주입

- DB를 사용할 모듈에 Entity 주입

```ts
@Module({
    imports: [
        TypeOrmModule.forFeature([
            TestEntity, //
            TestEntity2, //
        ])
    ]
})
```

- DB를 사용할 서비스에 Repository 주입

```ts
import { InjectRepository } from '@nestjs/typeorm'
import { Repository } from 'typeorm'

export class testService {
    constructor(
    	@InjectRepository(TestEntity)
         private testRepository: Repository<TestEntity>
    ) {}
}
```

> 사용빈도가 높은 `Repository<Entity>` 메서드

1. find

   - select와 같은 역할
   - conditons에는 쿼리 조건문 작성
   - 반환값 : `Promise<Entity[]>`

   ```ts
   find(conditions?: FindCondition<Entity>): Promise<Entity[]>
   ```

2. findOne

   - 하나의 값을 찾을 때 사용
   - 반환값 : `Promise<Entity>`

   ```ts
   findOne(id?: string | number | Date | ObjectID, options?: FindOneOptions<Entity>)
   findOne(options?: FindOneOptions<Entity>)
   findOne(conditions?: FindConditions<Entity>, options?: FindOneOptions<Entity>)
   ```

3. findAndCount

   - find로 찾아오는 객체와 그 객체의 수가 필요한 경우에 사용
   - 반환값 : `Promise<[Entity[], number]>`

   ```ts
   findAndCount(options?: FindManyOptions<Entity>)
   findAndCount(conditions?: FindConditions<Entity>)
   ```

4. create

   - 새로운 엔티티 인스턴스를 만들때 사용
   - DB에는 영향없음

   ```ts
   entity.create()
   ```

5. update

   - 엔티티의 일부를 업데이트할 때 사용
   - 엔티티 데이터가 DB에 존재하는지 확인하지 않음
   - 결과값 : `Promise<UpdateResult>`

   ```ts
   update(조건, Partial<Entity>, 옵션)
   ```

6. save

   - 엔티티를 DB에 저장
   - 엔티티가 없다면 insert하고, 있으면 update함
   - 반환값: `Promise<T[]>`

   ```ts
   save<T>(entities: T[])
   ```

7. delete

   - 엔티티가 DB에 있는지 체크하지않고 조건에 해당하는 delete쿼리 실행
   - 반환값 : `Promise<DeleteResult>`

   ```ts
   delete(조건)
   ```

8. remove

   - 받은 엔티티를 DB에서 삭제
   - 반환값 : `Promise<Entity[]>`

   ```ts
   remove(entity: Entity)
   remove(entity: Entity[])

​    

####  트랜잭션 

- 요청을 처리하는 과정에서 DB에 변경이 일어나는 요청을 독립적으로 분리하고, 에러가 발생한 경우 이전 상태로 되돌리기 위해 사용

> 트랜잭션을 사용하는 방법

1. QueryRunner를 이용해 단일 DB 커넥션 상태를 생성하고 관리

```ts
import { DataSource } from 'typeorm'

@injectable()
export class testService {
    constructor(
    	private dataSource: DataSource,  // DataSource 객체 주입 ✔️✔️
    ) {}
    
    async saveTestUsingQueryRunner() {
        const queryRunner = this.dataSource.createQueryRunner()  // 주입받은 DataSource객체로 QueryRunner 생성
        await queryRunner.connect()  // DB 연결
        await queryRunner.startTransaction()  // 트랙잭션 시작
        
        try {
            await queryRunner.query("SELECT * FROM TABLE")  // SQL문 실행
            await queryRunner.commitTransaction();  // 트랜잭션 종료 및 커밋
        } catch(error) {
            await queryRunner.rollbackTransaction();  // 에러발생시 모든 동작 롤백
        } finally {
      		await queryRunner.release(); // release가 없으면, commit이 끝나도 커넥션이 안 끊기면 문제됨 (하지만, 에러나면 자동으로 끊김)
    	}
    }
}
```

> queryRunner 객체

1. Query 실행

   - `query` : 주어진 SQL 쿼리 실행

   ```ts
   await queryRunner.query(sql: string, parameters?: any[])
   ```

2. 트랜잭션

   - `startTransaction` : 트랜잭션 시작

   ```ts
   await queryRunner.startTransaction(isolationLevel?: "READ UNCOMMITTED" | "READ COMMITED" | "REPEATABLE READ" | "SERIALIZABLE")
   ```

   - `commitTransaction` : 트랙잭션 커밋

   ```ts
   await queryRunner.commitTransaction()
   ```

   - `rollbackTransaction` : 트랜잭션 롤백

   ```ts
   await queryRunner.rollbackTransaction()
   ```

   - ``isTransactionActive` : 현재 트랙잭션이 활성화되어 있는지 여부를 확인

   ```ts
   await queryRunner.isTransactionActive()
   ```

3. 스키마 변경

   - `dropDatabase` : DB 삭제

   ```ts
   await queryRunner.dropDatabase(database: string, ifExist?: boolean): Promise<void>;
   ```

4. 인덱스 및 제약조건

   - `createIndex` : 인덱스 생성

   ```ts
   await queryRunner.createIndex(table: Table | string, index: TableIndex): Promise<void>;
   ```

   - `` : 인덱스 삭제

   ```ts
   await queryRunner.dropIndex(table: Table | string, index: TableIndex | string): Promise<void>;
   ```

   - `createForeignKey` : 외래키 생성

   ```ts
   await queryRunner.createForeignKey(table: Table | string, foreignKey: TableForeignKey): Promise<void>;
   ```

   - `dropForeignKey` : 외래키 삭제

   ```ts
   await queryRunner.dropForeignKey(table: Table | string, foreignKeyOrName: TableForeignKey | string): Promise<void>;
   ```

5. 기타

   - `connect` : querRunner를 DB에 연결

   ```ts
   await queryRunner.connect()
   ```

   - `release` : queryRunner 해 및 반납

   ```ts
   await queryRunner.release()
   ```

   - `isReleased` : queryRunner 해제 여부 확인

   ```ts
   await queryRunner.isReleased()
   ```

> `EntityManager` 객체 

```ts
await queryRunner.manager(): EntityManager
```

- 메서드

  - `create` : 엔터티 인스턴스를 생성

  ```ts
  await queryRunner.manager.create(entity: Entity): Entity
  ```

  - `update`

  ```ts
  await queryRunner.manager.update(
      entity: Entity, 
      criteria: any, 
      data: object
  ): Promise<UpdateResult>
  ```

  - `insert` : 엔티티를 데이터베이스에 삽입

  ```ts
  await queryRunner.managerinsert(entity: Entity): Promise<InsertResult>
  ```

  - `save` : 엔티티를 데이터베이스에 저장하거나 업데이트

  ```ts
  await queryRunner.manager.save(entity: Entity, options?: SaveOptions): Promise<Entity>
  await queryRunner.manager.save(entites: Entity[], options?: SaveOptions): Promise<Entity[]>
  ```

  - `remove` : 엔티티를 데이터베이스에서 삭제

  ```ts
  await queryRunner.manager.remove<Entity>(
      entity: Entity, 
      options?: RemoveOptions
  ): Promise<Entity>;
  ```

  - `fineOne` : 엔티티를 조건에 따라 데이터베이스에서 하나 찾음

  ```ts
  await queryRunner.manager.fineOne(entity: Entity, options?: FindOneOptions): Promise<Entity>
  ```

  - `find` : 엔티티를 조건에 따라 데이터베이스에서 여러 개 찾음

  ```ts
  await queryRunner.manager.find(entity: Entity, options?: FindManyOptions): Promise<Entity[]>: 
  ```

  - `count` : 엔티티의 개수를 세어 반환

  ```ts
  await queryRunner.manager.count(entity: Entity, options?: FindManyOptions): Promise<number>
  ```

  - `findOneOrFail` :  `findOne`과 유사하지만 결과를 찾지 못할 경우 예외를 throw

  ```ts
  await queryRunner.manager.findOneOrFail(entity: Entity, options?: FindOneOptions): Promise<Entity>
  ```

  - `findAndCount` : 조건에 따라 엔티티를 찾고 결과 개수를 반환

  ```ts
  await queryRunner.manager.findAndCount(
      entity: Entity, 
      options?: FindManyOptions
  ): Promise<[Entity[], number]>
  ```

  - `increment` : 엔티티의 특정 필드를 증가시킴

  ```ts
  await queryRunner.manager.increment(
      entity: Entity, 
      criteria: any, 
      propertyPath: string, 
      value: number
  ): Promise<UpdateResult>
  ```

  - `decrement` : 엔티티의 특정 필드를 감소시킴

  ```ts
  await queryRunner.manager.decrement(
      entity: Entity, 
      criteria: any, 
      propertyPath: string, 
      value: number
  ): Promise<UpdateResult>
  ```

  - `query` : 직접 SQL 쿼리를 실행

  ```ts
  await queryRunner.manager.query(query: string, parameters?: any[]): Promise<any>
  ```

  - `createQueryBuilder` : 쿼리 빌더를 생성

  ```ts
  await queryRunner.manager.createQueryBuilder(queryRunner?: QueryRunner): SelectQueryBuilder<any>;
  ```

  - `getRepository` : 엔티티에 대한 리포지토리 인스턴스를 가져옴

  ```ts
  await queryRunner.manager.getRepository<T>(entity: EntityTarget<T>): Repository<T>
  ```

  - `clear` : EntityManager의 캐시를 지움

  ```ts
  await queryRunner.manager.clear<Entity>(entityClass: EntityTarget<Entity>): Promise<void>;
  ```

​    

2. transaction 함수 이용

- `dataSource` 객체 내의 `transaction` 함수를 바로 이용

```ts
/**
  * `transaction`메서드는 주어진 함수 실행을 트랙잭션으로 래핑
  * 모든 데이터베이스 연산은 제공된 엔티티 매니저를 이용하여 실행해야 함
*/
transaction<T>(runInTransaction: (entityManager: EntityManager) => Promise<T>): Promise<T>
```

```ts
// 사용 예시
private async saveUserUsingTransaction(
	name: string,
	email:string,
    password: string;
) {
    await this.dataSource.transaction(async (manager) => {
        const user = new UserEntity()
        ...
        await manager.save(user)
    })
}
```

   

#### 마이그레이션

​     

---

### 2. Prisma

#### 설치 / 설정

#### Entity

#### DB 주입

#### 트랜잭션

#### 마이그레이션



---

## 2️⃣ ODM

### mongoose

#### 설치 / 설정

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

​    

#### MongoDB Atlas

![image-20230502113300912](Nest(2).assets/image-20230502113300912.png)

![image-20230502113320577](Nest(2).assets/image-20230502113320577.png)

![image-20230502113535084](Nest(2).assets/image-20230502113535084.png)

​    

#### schema

- class-validator 활용

```typescript
// test.schema.ts
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose'
import { Document, SchemaOptions } from 'mongoose'
import { IsEmail, IsNotEmpty } from 'class-validator'

const options: SchemaOptions = {
  timestamps: true  // 
}

@Schema(options) ✔️✔️
export class Test extends Document {
  @Prop({
    required: true,
    unique: true
  })  ✔️✔️
  @IsEmail()
  @IsNotEmpty()
  email :string
  
  @Prop({ required: true })  ✔️✔️
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
  constructor(private readonly testService: TestService) {}
  
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

​    

> 프론트엔드에서 보여지면 안되는 항목 숨기기

- mongoDB의 virtual field 활용

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

​     

---

## 3️⃣ Repository 패턴

- DB와 같은 저장소를 다루는 로직을 데이터 레이어로 분리하여 핵심 비지니스 로직에 집중할 수 있도록 해줌

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

​    

---

## 4️⃣ CQRS

- command query responsibility separation
- 명령(command)과 조회(query)를 분리하여 성능과 확장성 및 보안성을 높일 수 있도록 해주는 아키텍처 패턴

```bash
$ yarn add @nestjs/cqrs
```

```ts
// 사용할 모듈에 imports
import { CqrsModule } from '@nestjs/cqrs'

@Module({
    imports: [CqrsModule]
})
export class CreateTestModule {}
```

​    

### 명령 (command)

- 시스템의 상태를 변경
- Create, Update, Delete
- 서비스 계층이나 컨트롤러, 게이트웨이에서 직접 발송할 수 있음
- 전송한 커맨드는 커맨드 핸들러가 받아 처리

```ts
// create-test.command.ts
// 커맨드 정의
import { ICommand } from '@nestjs/cqrs'  ✔️✔️

export class CreateTestCommand implements ICommand {   ✔️✔️
    constructor(
    	readonly name: string,
    	readonly test: string
    ) {}
}
```

```ts
// controller
import { CommandBus } from '@nestjs/cqrs'
import { CreateTestCommand } from './create-test.command'

@Controller('test')
export class TestController {
    constructor(
    	private commandBus: CommandBus  ✔️✔️
    ) {}
    
    @Post()
    async createTest(@Body() createTestDto: CreateTestDto) {
        const command = new CreateTestCommand(createTestDto)  ✔️✔️
        return this.commandBus.execute(command)  ✔️✔️
    }
}
```

```ts
// create-test.handler.ts
import { CommandHandler, ICommandHandler } from '@nestjs/cqrs'
import { CreateTestCommand } from './create-test.command'

@Injectable()
@CommandHandler(CreateTestCommand)
export class CreateTestHandler implements ICommandHandler<CreateTestCommand> {
    async execute(command: CreateTestCommand) {
        // 기존 service 로직 수행
    }
}
```

```ts
@Module({
    providers: [CreateTestHandler]
})
```

​    

 ### 이벤트

- 2가지 이벤트 정의

```ts
// test-created.event.ts
import { IEvent } from '@nestjs/cqrs'
import { CqrsEvent } from './cqrs-event'

export class TestCreatedEvent extends CqrsEvent implements IEvent {
    constructor(
    	readonly ttt: string
    ) {
    	super(TestCreatedEvent.name)        
    }
}

// test.event.ts
import { IEvent } from '@nestjs/cqrs'
import { CqrsEvent } from './cqrs-event'

export class TestEvent extends CqrsEvent implements IEvent {
    constructor() {
    	super(TestEvent.name)        
    }
}
```

- `TestCreatedEvent`는 `CqrsEvent`를 상속받음 
- `@nestjs/cqrs` 패키지에서 제공되는 것이 아니고, 이벤트 핸들러에서 이벤트를 구분하기 위해 만든 추상 클래스

```ts
// cqrs-event.ts
export abstract class CqrsEvent {
    constructor(readonley name: string) {}
}
```

- 이벤트를 처리할 이벤트 핸들러를 만들고 프로바이더로 제공

```ts
import { EventsHandler, IEventHandler } from '@nestjs/cqrs'
import { TestCreatedEvent } from './test-created.event'
import { TestEvent } from './test.event'

@EventHandler(TestCreatedEvent, TestEvent)
export class TestEventsHandler implements IEventHandler<TestCreatedEvent | TestEvent> {
    constructor() {}
    
    async handle(event: TestCreatedEvent | TestEvent) {
        if (event.name === TestCreatedEvent·name) {}
        if (event.name === TestEvent.name) {}
    }
}
```

```ts
@Module({
    providers: [TestEventsHandler]
})
```

​    

> `@EventsHandler` 정의

- `IEvent` 인터페이스 배열을 인수받아 여러 이벤트를 처리할 수 있음

```ts
export declare const EventsHandler: (...events: IEvent[]) => ClassDecorator
```

> `IEventHandler` 인터페이스

```ts
import { IEvent } from './event.interface'

export interface IEventHandle<T extends IEvent = any> {
    handle(event: T): any
}
```

​    

### 조회 (query)

- 시스템 상태를 변경하지 않아 부작용 없음
- Read

```ts
// get-test-info.query.ts
import { IQuery } from '@nestjs/cqrs'  ✔️✔️

export class GetTestInfoQuery implements IQuery {  ✔️✔️
    constructor(readonly testId) {}
}
```

```ts
// get-test-info.handler.ts
import { IQueryHandler, QueryHandler } from '@nestjs/cqrs'
import { GetTestInfoQuery } from './get-test-info.query'

@QueryHandler(GetTestInfoQuery)  ✔️✔️
export class GetTestInfoQueryHandler implements IQueryHandler<GetTestInfoQuery> {  ✔️✔️
    constructor(
    	@InjectRepository(TestEntity)
    	private testRepository: Repository<TestEntity>
	) {}
                                                                                 
    async execute(query: GetTestInfoQuery): Promise<TestInfo> {
		// DB 조회
	}
}
```

```ts
// test.controller.ts
import { QueryBus } from '@nestjs/cqrs'  ✔️✔️
import { GetTestInfoQuery } from './query/get-test-info.query'

@Controller('test')
export class TestController {
    constructor(
    	private queryBus: QueryBus  ✔️✔️
    ) {}
    
    @Get('/testId')
    async getTestInfo(@Param('id') testId: string) {
        const getTestInfoQuery = new GetTestInfoQuery(testId)
        return this.queryBus.execute(getTestInfoQuery)
    } 
}
```

