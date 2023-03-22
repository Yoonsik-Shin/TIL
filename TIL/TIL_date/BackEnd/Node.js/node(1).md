# Node (1)

​      

## 1️⃣ 기초

### Node.js?

- JavaScript는 브라우저에서만 실행 가능했었음
- node.js를 통해 로컬 환경에서 JavaScript를 실행할 수 있게 해줌
- 크롬의 V8 엔진으로 만들어진 자바스크립트 런타임
- Non-blocking I/O : 모든 요청을 접수받고 빨리 완료되는 것부터 처리
- SNS, 채팅서비스등에 많이 사용
- 수학연산, 이미지 처리등의 라이브러리가 부족하고 처리속도가 떨어지는 단점이 있음



### npm? 

- Node Package Manager
- 노드 기반에서 실행될 수 있는 모듈을 관리
- [npmjs.com](https://www.npmjs.com/)



### yarn?

- npm 개량판
- 페이스북이 개발



> [CLI 정리](../BackEnd/Terminal.md)



### node 파일실행

- 실행하는 파일의 상위폴더에서 입력해야함

```bash
node 파일명.js
```



> 실무규칙1 : 하나의 함수는 하나의 기능만

```js
// 간단한 6자리 토큰 만들기
function getToken(digit) {
  // 검증추가
  if (digit === undefined || digit === null) {
    console.error('유효한 개수를 입력해주세요.')
    return
  }  
  if (digit <= 0) {
    console.error('1보다 큰 수를 입력해주세요.')
    return
  }
  if (digit > 10) {
    console.error('10보다 작은 수를 입력해주세요.')
    return
  }
    
  const result = String(Math.floor(Math.random() * (10**digit))).padStart(digit, '0')
  console.log(result)
}

getToken(6)
```



### 퍼사드 패턴 (Facade)

>  휴대폰으로 토큰 전송하기

```js
// index.js
import {checkValidationPhone, getToken, sendTokenToSMS} from './phone.js'

function createTokenOfPhone(phoneNumber, digit) {
  // 1. 핸드폰번호 자릿수 맞는지 확인하기
  if (!checkValidationPhone(phoneNumber)) {
    return
  }

  // 2. 핸드폰 토큰 6자리 만들기
  const token = getToken(digit)
  
  // 3. 핸드폰으로 토큰 전송하기
  sendTokenToSMS(phoneNumber, token)
} 

createTokenOfPhone('01012345678', 5)
```

```js
// phone.js
// 검증
export function checkValidationPhone(phoneNumber) {
  if (phoneNumber.length !== 10 && phoneNumber.length !== 11) {
    console.error('핸드폰 번호를 제대로 입력해주세요.')
    return false
  } else {
    return true
  }
}

// 간단한 6자리 토큰 만들기
export function getToken(digit) {
  if (digit === undefined || digit === null) {
    console.error('유효한 개수를 입력해주세요.')
    return
  }  
  if (digit <= 0) {
    console.error('0보다 큰 수를 입력해주세요.')
    return
  }
  if (digit > 10) {
    console.error('10보다 작은 수를 입력해주세요.')
    return
  }

  const result = String(Math.floor(Math.random() * (10**digit))).padStart(digit, '0')
  return result
}

// 전송
export function sendTokenToSMS(phoneNumber, token) {
  console.log(phoneNumber + ' 번호로 인증번호 ' + token + '을 전송합니다')
}
```

​    

### export / import 사용하기 (설정)

```bash
$ yarn init
```

```js
{
  "name": "파일명",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "type": "module" ✔️✔️ // 입력해주기
}
```

​    

## 2️⃣ 이메일 템플릿 생성함수 만들기

>  매개변수와 인수

- Argument(인수) : 함수 사용을 위해 실제로 대입되는 값
- Parameter(매개변수) : argument를 함수 내부에서 사용 가능하게 해주는 것

​     

> [구조분해할당](../../FrontEnd/JS/JS클린코딩(2).md)

```js
// 기본
function getWelcomTemplate(user) {
  const result = `
  	<html>
  		<body>
  			<h1>${user.name}님 가입을 환영합니다.</h1>
         <hr />
         <div>이름 : ${user.name}</div>
         <div>나이 : ${user.age}세</div>
         <div>가입일 : ${user.createdAt}</div>
  		</body>
  	</html>
  `
}

const MY_USER = {
  name: 'name',
  age: 12
  createAt: '2023-01-01'
}

getWelcomeTemplate(MY_USER)
```

```js
// 구조분해할당 (1)
function getWelcomTemplate({name, age, createAt}) {
  const result = `
  	<html>
  		<body>
  			<h1>${name}님 가입을 환영합니다.</h1>
         <hr />
         <div>이름 : ${name}</div>
         <div>나이 : ${age}세</div>
         <div>가입일 : ${createdAt}</div>
  		</body>
  	</html>
  `
}

const name = 'name'
const age = 12
const createAt = '2023-01-01'

getWelcomeTemplate({name, createAt, age})
```

```js
// 구조분해할당 (2)
function getWelcomTemplate({name, age, createAt}) {
  const result = `
  	<html>
  		<body>
  			<h1>${name}님 가입을 환영합니다.</h1>
         <hr />
         <div>이름 : ${name}</div>
         <div>나이 : ${age}세</div>
         <div>가입일 : ${createdAt}</div>
  		</body>
  	</html>
  `
}

const MY_USER = {
  name: 'name',
  age: 12,
  createAt: '2023-01-01'
}

getWelcomeTemplate(MY_USER)
```

​    

> [Shorthand Property](../../FrontEnd/JS/JS클린코딩(2).md)

- key와 value가 동일한 이름을 가질때 생략가능

```js
// 기본
const name = '이름'
const age = 12
const createAt = '2023-01-01'

const MY_USER = {
  name: name,
  age: age
  createAt: createAt
}

// Shorthand propery
const MY_USER = {
  name,
  age,
  createAt
}
```

​    

### Date 객체활용

```js
const date = new Date()

date.getFullYear(); // 연도
date.getMonth();    // 월
date.getDate();     // 일
date.getDay();      // 요일 (일요일: 0 ~ 토요일: 6)
date.getHours();    // 시
date.getMinutes();  // 분
date.getSeconds();  // 초
date.getMilliseconds();  // 밀리초
```

```js
// utils.js
export function getToday() {
    const date = new Date()
    const yyyy = date.getFullYear()
    const mm = date.getMonth() + 1
    const dd = date.getDate()

    return `${yyyy}-${mm}-${dd}`
}
```

​     

### 유효성검사

```js
// index.js
import { checkValidationEmail, getWelcomeTemplate, sendTemplateToEmail } from "./email.js";

function createUser(user) {
  // 1. 이메일이 정상인지 확인 (1-존재여부, 2-'@'포함여부)
  const isValid = checkValidationEmail(user.email)
  if (isValid) {
    // 2. 가입환영 템플릿 만들기
    const mytemplate = getWelcomeTemplate(user)

    // 3. 이메일에 가입환영 템플릿 전송
    sendTemplateToEmail(user.email, mytemplate)
    console.log('전송이 완료되었습니다')
  }
}
```

```js
// email.js
import { getToday } from "./utils.js"

// 1. 이메일이 정상인지 확인 (1-존재여부, 2-'@'포함여부)
export function checkValidationEmail(email) {
  if (email === undefined || !email.includes('@')) {
    console.log('이메일을 제대로 입력해 주세요.')
    return false
  }
  return true
}

// 2. 가입환영 템플릿 만들기
export function getWelcomeTemplate({name, age}) {
  const result = `
    <html>
      <body>
        <h1>${name}님 가입을 환영합니다.</h1>
        <hr />
        <div>이름 : ${name}</div>
        <div>나이 : ${age}세</div>
        <div>가입일 : ${getToday()}</div>
      </body>
    </html>
  `
  return result
}

// 3. 이메일에 가입환영 템플릿 전송
export function sendTemplateToEmail(email, mytemplate) {
  console.log(`${email}이메일주소로 ${mytemplate}를 전송합니다.`)
}
```

