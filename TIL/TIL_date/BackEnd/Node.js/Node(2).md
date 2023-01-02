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

### Swagger

-  백엔드 개발자가 미리 만들어 놓은 API 설명서

​    

---

## 3️⃣ Express

- 설치 및 등록

```bash
npm install express
yarn add express
```

```js
import express from 'express'  // 'module' 방식
const express = require('express')  // 'common.js'
```

