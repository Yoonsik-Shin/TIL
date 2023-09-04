# Nest (2)

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

- `manager`

```ts
await queryRunner.manager(): EntityManager
```

- `save`
- `remove`
- fineOn

​	

2. transaction 함수 이용



​    

### 2. Prisma

#### 설치 / 설정

#### Entity

#### DB 주입

#### 트랜잭션



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
- 명령 (command)
  - 시스템의 상태를 변경
  - Create, Update, Delete
- 조회 (query)
  - 시스템 상태를 변경하지 않아 부작용 없음
  - Read

```bash
$ yarn add @nestjs/cqrs
```

```ts
import { CqrsModule } from '@nestjs/cqrs'

@Module({
    imports: [CqrsModule]
})
```

