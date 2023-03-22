# node.js (1)

​    

## 1️⃣ 기본개념 

### Node.js

- JavaScript는 브라우저에서만 실행 가능했었음
- node.js를 통해 로컬 환경에서 JavaScript를 실행할 수 있게 해줌
- 크롬의 V8 엔진으로 만들어진 자바스크립트 런타임
- Non-blocking I/O : 모든 요청을 접수받고 빨리 완료되는 것부터 처리
- SNS, 채팅서비스등에 많이 사용
- 수학연산, 이미지 처리등의 라이브러리가 부족하고 처리속도가 떨어지는 단점이 있음



### npm

- Node Package Manager  ([npmjs.com](https://www.npmjs.com/))
- 노드 기반에서 실행될 수 있는 모듈을 관리

    ```bash
    $ npm init # package.json 자동생성
    $ npm install  # node_modules 파일이 없을 때 다시 설치
    ```



### package.json

- 어떤 라이브러리를 설치했는지 기록 

<img src="Node JS1.assets/image-20230322225458374.png" alt="image-20230322225458374" style="zoom:50%;" />

- `dependencies` : 실행에 필요한 라이브러리 모음
- `devDependencies` : 개발시에만 적용되는 라이브러리 모음



### export / import 사용하기 (설정)

```js
{
  "name": "파일명",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "type": "module" ✔️✔️ // 입력해주기
}
```



###  node_modules

- 라이브러리에 필요한 자료들을 담는 공간

​    

### yarn

- npm 개량판
- 페이스북이 개발

```bash
$ npm install yarn  # yarn 설치
$ yarn init  # package.json 자동생성
$ yarn install  # node_modules 파일이 없을 때 다시 설치
```



### node 파일실행

- 실행하는 파일의 상위폴더에서 입력해야함

```bash
$ node 파일명.js
$ node index.js
```



### Nodemon

- 서버를 자동으로 재시작해줌

```bash
# 설치
$ npm install -g nodemon
$ yarn add global nodemon

# 실행
$ nodemon server.js
```

​    

---

## 2️⃣ Express

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
import express from 'express
const app = express();

// listen(서버를 띄울 포트번호, 띄운 후 실행할 코드)
app.listen(8080, () => {
  
});
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


​         

> JSON 활용하기

```js
import express from 'express'

const app = express()

app.use(express.json())  ✔️✔️
```

​    

### GET 요청

```js
app.get('/URL', (req, res) => {
  // 1. 데이터를 조회하는 로직 => DB에 접속해서 데이터 꺼내오기
  // 2. 꺼내온 결과 응답 주기
  res.send()
})

app.listen(3000, () => {}) // 서버실행

// 예시1
app.get('경로', (요청내용, 응답방법) => {
  응답.send(); 
  응답.sendFile(보낼 파일의 경로);  // 파일보내기
})

// 예시2
app.get('/hi', (request, response) => {
  response.send();
  response.sendFile(__dirname + '/index.html')
})
```

> __dirname : 현재 파일의 경로

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



> body-parser

- input에 적은 정보 추출 
- body-parser 라이브러리가 express에 기본 포함이라 따로 설치 x

```js
// js파일 기본세팅
app.use(express.urlencoded({extended : true}));
```

- form 데이터의 input태그에 name 속성 추가

```html
<input type="" name=""> 
```
