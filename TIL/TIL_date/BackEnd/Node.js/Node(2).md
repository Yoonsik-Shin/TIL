# Node (2)

​    

## 1️⃣ 데이터 복사

### 1-1. 얕은복사 (Shallow Copy)

- 실제값이 아닌 주소값을 복사하는 방식
- `spread` 연산자 사용

```js
const profileCopy = {...profile}
```

​    

### 1-2. 깊은복사 (Deep Copy)

- JSON 활용
- `JSON.stringify()` : 인자를 문자열로 변환
- `JSON.parse()` : 문자열을 JSON방식으로 변환

```js
const object = {
  name: 'shin',
  age: '27',
  hobby: {
    one: 'computer',
    two: 'weightlifting',
  }
}

const objectToString = JSON.stringify(object)
const copiedObject = JSON.parse(objectToString)
```

​    

> Rest 파라미터 활용

```js
const { name, age, ...rest } = object;

name;  // shin
age;   // 27
rest;  // { hobby: { one: 'computer', two: 'weightlifting' } }
```

​    

---

## 2️⃣ Rest-API vs GraphQL-API

| Rest-API                     | GraphQL-API                  |
| ---------------------------- | ---------------------------- |
| 모든 데이터를 받아야함       | 필요한 데이터만 받을 수 있음 |
| https://google.com/profile/1 | profile(1)                   |
| axios 사용                   | apollo-client 사용           |



### CRUD

|      | axios  | apollo-client |
| ---- | ------ | ------------- |
| 생성 | POST   | MUTATION      |
| 수정 | PUT    | MUTATION      |
| 삭제 | DELETE | MUTATION      |
| 조회 | GET    | QUERY         |

```js
// axios
import axios from 'axios'

const result = axios({
  method: 'post',
  url: API_URL
})

// apollo-client
import { useMutation, useQuery } from '@apollo/client'

const result = useMutation()
const result = useQuery()
```

​    

---

## 3️⃣ Express

- Node에서 웹서버를 개발할 수 있도록 도와주는 프레임워크

- 설치 및 등록

```bash
npm install express
yarn add express
```

```js
import express from 'express'  // 'module' 방식
const express = require('express')  // 'common.js'
```

- 활용

```js
import express from 'express'

const app = express()

// GET 요청
app.get('/URL', (req, res) => {
  // 1. 데이터를 조회하는 로직 => DB에 접속해서 데이터 꺼내오기
  
  // 2. 꺼내온 결과 응답 주기
  res.send()
})

// 서버실행
app.listen(3000, () => {})
```

- 서버 실행

```bash
$ node 파일명
$ node index.js
```

> `node_modules` 파일이 없을 때

```bash
$ yarn install
```

​    

> req, res?

- `req`
  - `Request`를 줄여서 사용하는 변수명
  - 클라이언트에서 보낸 HTTP 요청이 들어있음 (브라우저 주소, 쿠키, 바디, 쿼리등)

- `res`

  - `Response`를 줄여서 사용하는 변수명
  - 서버에서 다시 클라이언트로 응답을 보낼때 사용
  - 쿠키, HTTP 상태코드, JSON 등의 내용을 담아 보낼 수 있음

  ​     

> JSON 활용하기

```js
import express from 'express'

const app = express()

app.use(express.json())  ✔️✔️
```

​    

### POST 요청

```js
app.post('/', (req, res) => {
  console.log(req.body) // 객체가 잘들어오는지 확인
  // 1. 데이터를 등록하는 로직 => DB에 접속해 데이터 저장하기
  // 2. 꺼내온 결과 응답 주기
})
```

​    

## 4️⃣ [Swagger](https://practice.codebootcamp.co.kr/api-docs/)

-  REST API를 쉽게 문서화하고 테스트할 수 있도록 도와주는 도구

- 설치 및 등록

```bash
$ yarn add swagger-ui-express swagger-jsdoc
```

> [swagger-ui-express](https://www.npmjs.com/package/swagger-ui-express?activeTab=readme)
>
> [swagger-jsdoc](https://www.npmjs.com/package/swagger-jsdoc)

- `swagger` 폴더 만들기

![image-20230103173621720](Node(2).assets/image-20230103173621720.png)

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
