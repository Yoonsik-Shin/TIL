# Node.js (2) 

## 1️⃣ Express

- Node에서 웹서버를 개발할 수 있도록 도와주는 프레임워크

​    

### 설치

```bash
$ npm install express
$ yarn add express
```



### 기본 세팅

```js
import express from 'express'  // 'module' 방식
const express = require('express')  // 'common.js'
```

```js
import express, { Express } from 'express'
const app: Express = express();

// listen(서버를 띄울 포트번호, 띄운 후 실행할 코드)
app.listen(8080, () => {
  
});
```

- 서버 실행

```bash
$ node 파일명
$ node index.js
```

​    

### req, res

- `req`
  - `Request`를 줄여서 사용하는 변수명
  - 클라이언트에서 보낸 HTTP 요청이 들어있음 (브라우저 주소, 쿠키, 바디, 쿼리등)

- `res`
  - `Response`를 줄여서 사용하는 변수명
  - 서버에서 다시 클라이언트로 응답을 보낼때 사용
  - 쿠키, HTTP 상태코드, JSON 등의 내용을 담아 보낼 수 있음

> JSON 활용하기

```js
import express from 'express'

const app = express()

app.use(express.json())  ✔️✔️
app.use(express.urlencoded({ extended: true}))
```

​    

### 미들웨어

- 미들웨어 이후의 라우터에만 미들웨어 실행값이 적용되어 실행순서가 중요함

```ts
app.use((req, res, next) => {
    // 라우터로 가기전 먼저 실행할 것들
    next();  // 모두 실행후 next함수 실행시 해당하는 라우터 실행
})
```

```ts
// 404 에러처리
// 마지막 부분에 작성
app.use((req, res, next) => {
    res.send({ error: '404 Not Found'})
})

app.listen(8000, () => {})
```

​    

### GET 요청

```js
import { Request, Response } from "express";

app.get('/URL', (req: Request, res: Response) => {
  // 1. 데이터를 조회하는 로직 => DB에 접속해서 데이터 꺼내오기
  // 2. 꺼내온 결과 응답 주기
  res.send()
})

app.listen(3000, () => {}) // 서버실행

// 예시1
app.get('경로', (요청내용, 응답방법) => {
  응답.send(); 
  응답.sendFile(보낼 파일의 경로);  // 파일보내기
  응답.json({}) // JSON 파일 내보내기
})

// 예시2
app.get('/hi', (req, res) => {
  res.send();
  res.sendFile(__dirname + '/index.html')
  res.json({ say: 'hi' })
})
```

> __dirname : 현재 파일의 경로

```js
// 동적경로
app.get('/:id', (req, res) => {
  db.collection('').findOne({_id: parseInt(req.params.id)}, (error, result) => {
    res.render('파일', { data: result })
  })
})
```

​    

### POST 요청

```js
app.post('/', (req, res) => {
  console.log(req.body) // 객체가 잘들어오는지 확인
  // 1. 데이터를 등록하는 로직 => DB에 접속해 데이터 저장하기
  // 2. 꺼내온 결과 응답 주기
})

// 예시1
app.post('경로', (요청내용, 응답방법) => {
  응답.send();
})

// 예시2
app.post('/bye', (request, response) => {
  response.send();
})
```

​    

### PUT / PATCH 요청

- `PUT` 

  - 수정할 요소가 있으면 업데이트로 동작 (Update)
  - 수정할 요소가 없다면 새롭게 생성 (Create)
  - 수정하고 싶은 값과 수정되지 않아야 하는 값이 모두 있어야함
  - 만약 수정할 값만 보낸다면 나머지 값들은 빈값으로 덮어씌워짐

  ```js
  app.put('/', (req, res) => {
      const body = req.body  // { id:  }
  })
  ```

- `PATCH`

  - 요소를 부분적으로 업데이트
  - 수정하고 싶은 값만 받아 수정하고, 나머지 요소는 그대로 나둠

  ```js
  app.patch('/', (req, res) => {
      const body = req.body
  })
  ```

​    

### Query Parameter

- 동적으로 라우팅하고 싶을 때 사용

```js
// http://.../패스파라미터1/체크
app.get('/:path-params1/:check', (req, res) => {
    console.log(req.params) // { path-params: '패스파라미터', check: '체크' }
})
```

​    

### Path Parameter

- Get 요청에서 데이터를 전송하고 싶을 때 사용
- 보안에 좋지 못함

```js
// http://..?id=10&category=food
app.get('/', (req, res) => {
    console.log(req.query)  // { id: '10', category: 'food' }
})
```

​    

### CORS

- `Cross-Origin-Resource-Sharing`
- 서로 다른 출처(origin)를 가진 주소로 요청이 들어왔을 때 발생

```bash
$ npm install cors
$ yarn add cors
```

```js
import cors from 'cors'

app.use(cors())

// cors 옵션 작성가능
const corsOptions = {
  origin: ...,
  ...
}
app.use(cors(corsOptions))
```

> [cors 옵션확인](https://github.com/expressjs/cors#readme)

​     

### 디자인 패턴

#### 싱글톤 패턴

- 객체의 인스턴스를 오직 하나만 생성하여 사용하는 패턴
- 객체에 접근할 때 메모리를 줄일 수 있음
- 다른 클래스간의 데이터 공유가 쉬움

```typescript
import express, { Application, Express } from "express";
import catsRouter from "./cats/cats.route";

class Server {
    public app: Application;

    constructor() {
        this.app = express();
    }

    private setRoute() {
        this.app.use(catsRouter);
    }

    private setMiddleWare() {
        this.app.use(express.json());
        this.setRoute();
        this.app.use((req, res, next) => {
            res.send({ error: "404 Not Found" });
        });
    }

    public listen() {
        this.setMiddleWare();
        this.app.listen(8000, () => {
            console.log(`서버가 정상적으로 실행됨 (http://localhost:}/)`);
        });
    }
}

function init() {
    const server = new Server();
    server.listen();
}

init();

```

​    

#### 서비스 패턴

- router와 비지니스 로직 분리

```js
// example.route.ts
import { Router } from 'express'

const router = Router()

router.get('/', readAll)
router.get('/:id', readOne)
router.post('/', createOne)

export default router
```

```js
// example.service.ts
import { Request, Response } from 'express'

export const readAll = () => { 비지니스 로직 }
export const readOne = () => { 비지니스 로직 }
export const createOne = () => { 비지니스 로직 }
```

​     

>  body-parser

- input에 적은 정보 추출 
- body-parser 라이브러리가 express에 기본 포함이라 따로 설치 x

```js
// js파일 기본세팅
app.use(express.json()); 

// 예전 세팅
import bodyParser from 'body-parser'

app.use(express.json()); 
app.use(express.urlencoded({extended : true}));
```

- form 데이터의 input태그에 name 속성 추가

```html
<input type="" name=""> 
```

​     

---

## 2️⃣ MySQL

```bash
$ yarn add mysql2
$ yarn add @types/node -D
```

```js
// commonjs
const mysql = require('mysql2')

// ESM
import mysql from 'mysql2'
```

```js
// 기본 DB연결
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'test'
});
```

```js
// connection pools 사용 ✔️✔️
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  database: 'test',
  waitForConnections: true,
  connectionLimit: 10,
  maxIdle: 10, // max idle connections, the default value is the same as `connectionLimit`
  idleTimeout: 60000, // idle connections timeout, in milliseconds, the default value 60000
  queueLimit: 0,
  enableKeepAlive: true,
  keepAliveInitialDelay: 0
});
```

​    

---

## 3️⃣ [Swagger](https://practice.codebootcamp.co.kr/api-docs/)

-  REST API를 쉽게 문서화하고 테스트할 수 있도록 도와주는 도구

-  설치 및 등록

```bash
$ yarn add swagger-ui-express swagger-jsdoc
```

> [swagger-ui-express](https://www.npmjs.com/package/swagger-ui-express?activeTab=readme)
>
> [swagger-jsdoc](https://www.npmjs.com/package/swagger-jsdoc)

- `swagger` 폴더 만들기

![image-20230103173621720](Node.js(2).assets/image-20230103173621720.png)

- 폴더안에 `*.swagger.js` 파일을 만들기

```js
// *.swagger.js

/**
 * @swagger
 * /boards:
 *   get:
 *     summary: 게시글 가져오기
 *     tags: [Board]
 *     parameters:
 *          - in: query
 *            name: number
 *            type: int
 *     responses:
 *       200:
 *         description: 성공
 *         content:
 *           application/json:
 *              schema:
 *                  type: array
 *                  items:
 *                      properties:
 *                          number:
 *                              type: int
 *                              example: 3
 *                          writer:
 *                              type: string
 *                              example: 철수
 *                          title:
 *                              type: string
 *                              example: 제목입니다~~~
 *                          contents:
 *                              type: string
 *                              example: 내용입니다!!!
 */

/**
 * @swagger
 * /boards:
 *   post:
 *     summary: 게시글 등록하기
 *     tags: [Board]
 *     responses:
 *          200:
 *              description: 성공
 */
```

> 매우 철저하게 들여쓰기 규칙을 지켜야함

​    

- 설정파일 만들어주기 (`config.js`)

```js
export const options = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'API명세서 작성', ✔️✔️ 
      version: '1.0.0',
    }, 
  },
  apis: ['./swagger/*.swagger.js'], // files containing annotations as above [✔️✔️ 경로 설정 필요]
};
```

​    

- `index.js` 파일 설정

```js
import swaggerUi from 'swagger-ui-express';
import swaggerJsdoc from 'swagger-jsdoc';
import { options } from './swagger/config.js'

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerJsdoc(options)));
```

​    

### Swagger 문법

> [공식사이트](https://swagger.io/docs/specification/basic-structure/)