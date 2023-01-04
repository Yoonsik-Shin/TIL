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

// A schema is a collection of type definitions (hence "typeDefs")
// that together define the "shape" of queries that are executed against
// your data.
const typeDefs = `#graphql
  # Comments in GraphQL strings (such as this one) start with the hash (#) symbol.

  # This "Book" type defines the queryable fields for every book in our data source.
  type Book {
    title: String
    author: String
  }

  # The "Query" type is special: it lists all of the available queries that
  # clients can execute, along with the return type for each. In this
  # case, the "books" query returns an array of zero or more Books (defined above).
  type Query {
    books: [Book]
  }
`;
```

​    

### resolver 정의

```js
// Resolvers define how to fetch the types defined in your schema.
// This resolver retrieves books from the "books" array above.
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
// The ApolloServer constructor requires two parameters: your schema
// definition and your set of resolvers.
const server = new ApolloServer({
  typeDefs,
  resolvers,
});

// Passing an ApolloServer instance to the `startStandaloneServer` function:
//  1. creates an Express app
//  2. installs your ApolloServer instance as middleware
//  3. prepares your app to handle incoming requests
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

