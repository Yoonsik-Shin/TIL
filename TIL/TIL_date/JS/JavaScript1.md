# JavaScript 정리 (1)

   

## 0️⃣ JS 기본

> Primitive Types (기본 원시 타입)

1. Number
2. boolean
3. string
4. Null
5. undefined

​    

>  Read Evaluate Print Loop (REPL) 

- 하나의 입력을 받아서(Read single input), 처리하고(Evaluate), 결과를 반환하는(Print result) 환경으로 구현된 프로그램
- 커맨드라인 인터페이스를 가지는 프로그램이다. 
- js, python 같은 스크립트 언어

​    

> 주석 

```javascript
// 주석
/** 최신 주석 */ 
```

​    

> JavaScript 파일 활용

```html
<!DOCTYPE html>
<html>
  <head>
    <title>JS Demo</title>
  </head>
  <body>
    <script src="app.js"></script>
  </body>
</html>
```

​    

> NaN (Not a Number)

- 숫자로 간주하지만 숫자는 아닌 무언가를 나타냄

```javascript
0/0        // Nan
1 + NaN    // NaN
NaN * NaN  // NaN
200 + 0/0  // NaN
```

​    

> `typeof` 

- 값의 타입 체크

```javascript
typeof NaN
>> "number"
```

​    

---

## 1️⃣변수 (Variables) 

> 선언, 할당, 초기화

- 선언 (Declaration) : 변수를 생성하는 행위 or 시점
- 할당 (Assignment) : 선언된 변수에 값을 저장하는 행위 or 시점
- 초기화 (Initialization) : 선언된 변수에 처음으로 값을 저장하는 행위 or 시점

```javascript
let hello     // 선언
hello = 100   // 할당
let bye = 0   // 선언 + 할당

// 변수 동시에 여러개 만들기
var a = 1, b = 'c', d;

// window로 전역변수 만들기
window.변수 = '';
```

​    

> 호이스팅 (hoisting)

- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근시 `undefined`반환
- JS는 모든 선언을 호이스팅함
- `var`는 선언과 초기화가 동시에 발생하여, 일시적인 사각지대가 존재하지 않음 (의도치않은 오류 발생 가능성 O)
- let, const는 Hoisting시 undefined가 자동으로 할당 안됨 (에러발생)

```js
// 내가 쓴 코드
1  function 함수(){
2    var 변수 = '';
3  }
4
5  var 나이 = 30;

// 자바스크립트가 해석하는 코드
1  var 나이;
2
3  function 함수(){
4    var 변수 = '';
5  }
6  나이 = 30;
```

​    

1. `let`

- 블록 내부에서 선언된 변수까지도 지역변수로 인정하는 블록레벨 스코프
- 중괄호 내에서 유효

```javascript
let someName = value;
let c = a + b;

// 값 재할당 가능 
let a = 10;
a = 20;  🟢

// 중복선언 불가능
let b = 20;
let b = 30;  ⛔
```

```javascript
// 계산
let num = 1;
num--;
num++;
```

​    

2. `const`

- constant : 상수
- 항상 일정한 값
- 값 업데이트 불가
- 값 재할당 불가능
- 블록레벨 스코프

```javascript
const num = 4;
num = 10;  // ERROR 발생
num++;     // ERROR 발생
```

​    

3. `var`

- `let` 과 유사
- 현재에는 잘 안씀
- 함수레벨 스코프
  - 함수 내에서는 지역변수
  - 나머지는 전역변수


```javascript
var num = 10;
var num = 20;  // 중복선언 가능
num = 30;      // 재할당 가능
```

​    

> let, const, var 비교

| 키워드 | 재선언 | 재할당 | 스코프      | 비고 |
| ------ | ------ | ------ | ----------- | ---- |
| let    | X      | O      | 블록 스코프 | ES6  |
| const  | X      | X      | 블록 스코프 | ES6  |
| var    | O      | O      |             |      |



> 변수명 규칙

- 카멜 케이스
  - 첫 단어 소문자
  - 공백 불가능
  - `_` 사용은 가능하나 잘 안씀

```javascript
let currentDate = 1999;
```

- Boolean
  - `is` 사용

```javascript
let isGameOver = true;
```

​    

---

## 2️⃣ Primitive Types (기본 원시 타입)

1. Boolean

- 모두 소문자 (파이썬은 `True / False`)

```javascript
true    // 1
false   // 0
```

​    

2. String

```javascript
let username = 'Yoonsik';
```

- 인덱싱 : 변수[숫자]

```javascript
변수[3]
```

- 문자열의 길이

```javascript
변수.length;
```

​    

> 계산 타입

- 문자열 + 숫자 >> 문자열



> 문자열 메서드 (Methods)

```javascript
thing.method()      // arguments x
thing.method(arg)   // arguments o
```

> [메서드 mdn 문서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String)

- 메서드 사용시 원본 변화 x, 새 복사본을 만듬 
- 자주 사용하는 메서드

```javascript
// arguments x
.toUpperCase()     // 대문자 변경
.toLowerCase()     // 소문자 변경
.trim()            // 좌우 공백 제거
.trimStart()
.trimEnd()

// arguments o
.indexOf('')    // 문자열에서 인수가 나타나는 인덱스를 반환, ❗문자열에 인수 없는 경우 -1 반환❗
.slice(시작인덱스[, 끝인덱스])   // 1개 이상의 인수 가능, 시작인덱스만 있으면 시작인덱스부터 끝까지
.slice(-idx)    // 뒤에서부터 idx 글자
.replace('바꿔질 값','새로 바뀔값')   // 1개만 교체
.replaceAll('바꿔질 값','새로 바뀔값')  // 모두 교체
.includes(value) // 문자열에 value가 존재하는지 판별 후 true / false 반환
.split()         // value인자 없을 경우, 기존 문자열을 배열에 담아 반환
.split('')       // value인자가 빈 문자열일 경우, 각 문자로 나눈 배열을 반환
.split(value)    // value값으로 문자열을 나눈 배열을 반환
```

​    

### ❗템플릿 리터럴 (Template Literals)

- 백틱(back-tick) [``] 사용
-  `${계산식}`
- 파이썬 f-string과 유사

```javascript
`hello ${1+2+3}`
>> "hello 6"

`you bought ${변수명}`
>> "you bought 변수값"
```

​    

### ❗tagged Literal

- 문자 해체분석
- 첫번째 파라미터는 문자를 배열화 해줌
- 두번째 파라미터 이후부터는 변수들을 뜻함

```js
function 해체분석(문자, 변수1, 변수2){
  console.log(문자);
  console.log(변수1);
  console.log(변수2);
}

해체분석`문자1 ${변수1} 문자2 ${변수2}`
>> ['문자1', '문자2']
>> 변수1
>> 변수2
```

​    

3. Null

- 값이 없음을 명시
- 아무것도 없음
- 자주 사용 x

```javascript
let log = null;
```

​    

4. undefined

- 자주 사용함
- 정의되지 않은 것

​    

> Math Object

```javascript
Math               // 관련 메소드 출력
Math.PI            // 3.141592653589793 파이값
Math.round(4.9)    // 5    반올림
Math.abs(-456)     // 456  절대값
Math.pow(a, b)     // a의 b제곱
Math.floor(3.9999) // 3    내림
Math.ceil(34.999)  // 35   올림
Math.random()      // 0이상 1미만인 소수 (0 ~ 0.9999999999..) ✔️✔️
Math.floor(Math.random() * 10) + 1
```

​    

---

## 3️⃣ 비교연산자 (Comparisons)

- 알파벳도 비교 연산 가능 (유니코드 기준)

```javascript
'a' < 'b';  // true
'A' > 'a';  // false
```

​    

> 이중등호 vs 삼중등호

1. 이중등호 [`==`]  + [`!=`]

   - 타입에 관계없이 값이 같다면 같은 것으로 취급
   - 서로다른 타입이면 같아지도록 강제 반환
   - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
   - 원치 않는 결과가 나올수 있음

   ```javascript
   1 == 1      // true
   1 == '1'    // trues
   null == undifined;  // true
   0 == false  // true
   ```

2. 삼중등호 [`===`]  + [`!==`]

   - 값과 타입 모두 비교

   ```javascript
   0 === false  // false
   ```


​    

---

##  4️⃣ 논리연산자 (Logical Operators)

- 실행순서 : (1) AND >> (2) OR

1. AND : `&&`

```javascript
// 비밀번호 조건설정
const password = prompt("새로운 비밀번호를 입력해주세요.")

// 6자리 이상, 공백 포함 불가
if (password.length >= 6 && password.indexOf(' ') === -1) {
  	console.log("비밀번호가 정상적으로 입력되었습니다.")
} else {
  console.log("비밀번호가 너무 짧거나 공백이 포함되어있습니다. 6글자 이상으로 공백없이 입력해주세요.")
}
```

2. OR : `||`
3. NOT : `!`

```javascript
!null      // true
!(0 === 0) // false
!(3 <= 4)  // false 
```

​    

---

## 5️⃣ 삼항연산자 (Ternary Opeators)

- 세 개의 피연산자를 사용
- 변수에 할당 가능

```javascript
const 변수 = 조건 ? 조건이 true이면 반환되는 값 : 조건이 false이면 반환되는 값
```

```javascript
console.log(true ? 1 : 2) // 1
console.log(false ? 1 : 2) // 2
const result = Math.PI > 4 ? 'Yes' : 'No'
console.log(result) // No
```

​    

---

##  6️⃣ 출력 / 입력

1. console.log

- 파이썬의 print와 같은 기능

```javascript
console.log("hello world!")
>> "hello world!"

console.log(1+4, 'hi', true)
>> 5 "hi" true
```

​    

2. Alert

- 사용자에게 뭔가를 출력해 주지만 콘솔에는 출력 x
- 팝업 경고

```java
alert("팝업창 내용")
```

​    

3. prompt

- 인수를 받음
- 파이썬의 input

```javascript
prompt("팝업창 내용")

let userNumInput = prompt("이름을 입력해주세요.")
```

​    

4. parseInt

- 파이썬의 int와 유사

```javascript
parseInt("100")
>> 100
```

​    

5. toFixed

```js
let num = 1.23456

console.log(numObj.toFixed());    // '1'
console.log(numObj.toFixed(1));   // '1.2'
console.log(numObj.toFixed(2));   // '1.23'
console.log(numObj.toFixed(3));   // '1.235'
console.log(numObj.toFixed(10));  // 오류
```

​    

---

##  7️⃣ 조건문 (Conditional Statement)

```javascript
if (조건) {
  실행문;
} else if (조건2) {
  실행문2;
} else if (조건3) {
  실행문3;
} else {
  마지막 실행문;
}
```

​    

> Truthy / Falsy Value

- 모든 JS 값들은 Truthy나 Falsy 속성을 지님
- `Falsy 값`
  1. `false`
  2. 0
  3. "" (빈 문자열)
  4. null
  5. undefined
  6. NaN
- 위 6가지 Falsy값을 제외한 모든 값은 `Truthy`

```java
if (0) {
  console.log("TRUTHY")
} else {
  console.log("FALSY")
}

>> "FALSY"
```

​    

---

## 8️⃣ switch문

- ❗일치하는 case이후 실행문들은 `break`가 없다면 모두 실행됨

```javascript
switch (값) {
  case (값1):   // 값 = 값1 이면
    실행문1;
    break;
  case (값2):   // 값 = 값2 이면
    실행문2;
    break;
  case (값3):   // 값 = 값3 이면
    실행문3;
    break;
  default:      // 아무것도 일치하지 않을 때
    실행문;
}
```
