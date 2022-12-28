# Node (1)

​      

### Node.js?

- JavaScript는 브라우저에서만 실행 가능했었음
- node.js를 통해 로컬 환경에서 JavaScript를 실행할 수 있게 해줌
- 크롬의 V8 엔진으로 만들어진 자바스크립트 런타임



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

- 

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



