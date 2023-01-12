# Node (3)

​    

## 1️⃣ CORS

- `Cross-Origin-Resource-Sharing`
- 서로 다른 출처(origin)를 가진 주소로 요청이 들어왔을 때 발생

- 해결법

```bash
$ yarn add cors
```

```js
import cors from 'cors'

const app = express()

app.use(cors()) ✔️✔️
```

> 특정 origin만 사용하기

```js
app.use(cors({
  origin: 특정 origin
}))
```

​    

---

## 2️⃣ nodemon

- 코드가 수정되면 서버를 알아서 다시 실행해줌

```bash
# package.json이 있는 파일에서 실행
$ yarn add nodemon
```

```json
// package.json에 아래 내용 추가
{
  ...
  "scripts": {  
    "dev": "nodemon index.js"
  }
  ...
}
```

```bash
# 서버 실행
$ yarn dev
```

​    

---

## 3️⃣ GraphQl

### apollos-server 설치

```bash
$ yarn add @apollo/server graphql
```

​    

### 스키마 정의

- rest-api의 swagger와 유사

```js
import { ApolloServer } from '@apollo/server';
import { startStandaloneServer } from '@apollo/server/standalone';

const typeDefs = `
  type Book {
    title: String
    author: String
  }
  
  type Query {
    books: [Book]
  }
`;
```

​    

### resolver 정의

```js
const resolvers = {
  Query: {
    books: () => 'hello',
  },
};
```

- express와 비교

```js
app.get('/', (req, res) => {
  res.send()
})
```

​    

### Apollo Server 인스턴스 만들기

```js
const server = new ApolloServer({
  typeDefs,
  resolvers,
});

const { url } = await startStandaloneServer(server, {
  listen: { port: 4000 },
});

console.log(`🚀  Server ready at: ${url}`);
```

> package.json에 `"type":"module"` 추가하기

- express와 비교

```js
app.listen(4000)
```

​    

### API 만들기 정리

```js
const resolvers = {
  Mutation: {
    createBoard: (parent, args, context, info) => {}
  }
}
```

- `parent` : 부모의 type resolver에서 반환된 결과를 가진 객체
- `args` : 쿼리 요청시 전달된 parameter를 가진 객체
- `context` : GraphQL의 모든 resolver가 공유하는 객체, 로그인 인증 / DB 접근권한 등에 사용
- `info` : 명령 실행 상태 정보를 가진 객체

> 사용하지 않는 매개변수는 `_`(언더바)로 선언



```js
import { ApolloServer } from "@apollo/server";
import { startStandaloneServer } from "@apollo/server/standalone";

// 타입 정의
const typeDefs = gql`
	
	type Query {
		
	}

	type Mutation {
	
	}
`

const resolvers = {
  Query: {
    fetchBoards: () => {}
  }
  
  Mutation: {
  	createBoard: (_, args) => {
			// 1. 데이터를 등록하는 로직 => DB에 접속해서 데이터 저장하기
      // 2. 저장 결과 응답 주기
      return '성공'
    }
	}
}
```

​    

---

## 4️⃣ SMS 전송

### [Coolsms](https://console.coolsms.co.kr/dashboard) 활용 

```bash
$ yarn add coolsms-node-sdk
```

```js
import coolsms from'coolsms-node-sdk'

export async function  sendTokenToSMS(phoneNumber, token) {
  const MySms = coolsms.default
  const messageService = new MySms(process.env.SMS_KEY, process.env.SMS_SECRET)
  const result = await messageService.sendOne({
    to: phoneNumber,
    from: process.env.SMS_SENDER,
    text: `[문자메시지 전송 테스트중] 인증번호는 ${token} 입니다.`
  })
}
```



> 환경변수 분리하기

- 
