# JS 클린코드 (1)

​    

## 0️⃣ 몽키패치 (안티패턴)

- 런타임중인 프로그램의 내용이 변경되는 행동
- 생각대로 출력이 안되는 경우

​    

## 1️⃣ 변수 다루기

### 1. var를 지양하자

- 코드가 길어질때 var 사용시 의도치않게 변수가 변질될 수 있음

```js
var name = '이름1'
var name = '이름2'
var name = '이름3'
name = '이름3'

console.log(name)
>> 이름3
```

```js
console.log(name)
>> undefined  // 에러 안남

var name = '이름1'
var name = '이름2'
var name = '이름3'
var name = '이름3'
name = '이름2'
```

​    

> let 사용시 선언 오류 발생하여 의도치않은 중복 방지 

```js
let name = '이름'
let name = '이름'
let name = '이름'
>> SyntaxError: Identifier 'name' has already been declared
```

​    

> let과 const의 차이

```js
// let : 먼저 선언하고 언제든지 재할당 가능
let name;
name = '이름'
name = '이름1'

// const : 한번만 선언가능하고 재할당 불가능
const name;  // 선언만 하는건 불가능
>> Assignment to constant variable.

const name = '이름' // (O)
```

​    

>  function scope / block scope

- var는 함수단위 스코프
- if는 함수가 아니므로 if문 내에서 선언된 var는 전역에 영향을 미침

```js
var global = '전역변수';

if (global === '전역변수') {
  var global = '지역변수';
  console.log(global);  // 지역변수
}

console.log(global)  // 지역변수 (원하는 값은 전역변수였지만 오염됨)
```

```js
let global = '전역변수';

{
  let global = '지역변수';
  console.log(global);  // 지역변수
}

console.log(global)  // 전역변수
```

​     

---

### 2. 전역공간 사용 최소화

- 어디서나 접근가능
- 분리되었다고 생각하지만 런타임 환경에서는 분리가 되어있지 않음

​    

> 전역이란?

window : 브라우저에서의 최상위

```js
console.log(window)
```

global : node.js에서의 최상위

```js
console.log(global)
```



> 해결법

1. 전역변수를 될 수 있으면 사용하지 않는다
2. 지역변수를 사용한다.
3. window나 global을 조작하지 않는다.
4. let, const를 사용한다.
5. IIFE, Module, Closure를 활용하여 스코프를 나눈다.

​    

### 3. 임시변수 제거하기

> 이유

1. 명령형으로 가득한 로직
2. 디버깅이 힘듬
3. 추가적인 코드를 작성하고 싶은 유혹 발생 (함수는 하나의 역할만 해야함)

> 해결책

- 함수 나누기

```js
function getDateTime(target) {
  const month = target.getMonth();
  const day = target.getDate();
  const hour = target.Hours();
  
  return {
    month: month >= 10 ? month : '0' + month,
    day: day >= 10 ? day : '0' + day,
    hour: hour >= 10 ? hour : '0' + hour,
  }
}

function getDateTime() {
  const currentDateTime = getDateTime(new Date())
  
  return {
    month: currentDateTime.month + '분 전',
    day: currentDateTime.day + '분 전',
    hour: currentDateTime.hour + '분 전',
  }
}
```

- 바로 반환

```js
function getElements() {
  return {
    a: document.querySelector('a'),
    b: document.querySelector('b'),
    c: document.querySelector('c'),
  }
}
```

- 고차함수 (map, filter, reduce)
- 선언형 코드 사용

```js
// 명령형 코드 (안좋은 사례)
function getSomeValue(params) {
  let val = ''
  if () {
    val++
  } else if () {
   	val-- 
  }
  
  return val
}
```



​    

### 4. 호이스팅 주의하기

- 호이스팅 : 런타임시 선언이 최상단으로 끌어올려지는 것

```js
// 호이스팅 동작 사례
var global = 0;

function outer() {
  console.log(global);  // undefined (WHY?)
  var global = 5;
  
  function inner() {
    var global = 10;
    console.log(global);  // 10
  }
  
  inner();
  
  global = 1;
  console.log(global);  // 1 
}
```

```js
// 이런식으로 작동함
function outer() {
  var global;
  console.log(global);  // undefined
  global = 5;
}
```



> 함수도 호이스팅 된다

```js
var sum;

console.log(typeof sum);  // function
console.log(sum());  // a+b+c

function sum() {
  return a+b;
}

function sum() {
  return a+b+c;
}
```

- 변수 선언 > 할당 > 초기화 완료시 정확한 분리가 됨

```js
var sum = 10;

console.log(sum());  // sum is not a function
function sum() {
  return a+b;
}

function sum() {
  return a+b+c;
}
```

​    

---

## 2️⃣ 타입 다루기

### 1. typeof의 맹점

- PRIMITIVE 타입은 대부분 잘 나타내지만, REFERENCE 타입은 감별하기 어려움

```js
typeof '문자열'  // 'string'
typeof undefined // 'undefined'

function Function() {}
typeof Function  // function
class Class {}
typeof Class // function

const str = new String('문자열')
typeof str // 'object'

typeof 
typeof null // 'object' << 자바스크립트 자체의 오류
```



> instanceof 연산자

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

const yoonsik = new Person('yoonsik', 27)
const y = {
  name : 'yoonsik',
  age : 27
}

yoonsik instanceof Person  // true
y instanceof Person  // false
```

```js
const arr = []
const func = function() {}
const date = new Date()

arr instanceof Array  // true
func instanceof Function  // true
date instanceof Date  // true

// 함정
arr instanceof Object  // true
func instanceof Object  // true
date instanceof Object  // true
```

​    

> REFERENCE 객체까지 감지 가능

```js
const arr = []
const func = function() {}
const date = new Date()

Object.prototype.toString.call(new String(''))  // '[object String]'
Object.prototype.toString.call(arr)  // '[object Array]'
Object.prototype.toString.call(func))  // '[object Function]'
Object.prototype.toString.call(date)  // '[object Date]'
```

​    

### 2. undefined / null

#### null

```js
!null  // true
!!null  // false >> `!!` 사용시 값을 Boolean으로 형변환 

null === false  // false
!null === true  // true
```

```js
// null은 숫자와의 연산에서 0으로 취급됨
null + 123  // 123
```

​    

#### undefined

- 변수는 선언했지만, 값은 정의되지 않고 할당도 되지 않은 상태

```js
let a;
typeof a  // 'undefined'
```

- undefined는 `NaN`로 표현됨

```js
undefined + 10  // NaN
!undefined  // true
```



> 비교

```js
undefined == null  // true
undefined === null  // false
!undefined === !null // true
```

| undefined        | null         |
| ---------------- | ------------ |
| NaN              | 0            |
| type : undefined | type : objec |

​    

### 3.  eqeq 줄이기 (동등연산자 `==`)

```js
'1' == 1  // true
1 == true  // true

'1' === 1  // false
1 === true  // false
```

​    

### 4. 형변환 주의하기

- 암묵적 형변환 지양하기

```js
27 + ' 세'  // '27 세'
!!'문자'  // true
!!''  // false

// Refer 객체 활용하여 사용
String(27 + ' 세')
Boolean('문자')
Boolean('')
Number('27')
```



- `parseInt` 사용시 주의사항

```js
// 10진수를 사용할 것을 지정해줘야함 (10진수가 기본값 아님)
parseInt('1.00', 10)
```



### 5. isNaN

- is Not A Number : 숫자가 아니다.
- `isNaN` 사용 지양하고,  `Number.isNaN` 사용하기

```js
// isNaN은 느슨한 검사
isNaN(123)  // false : 숫자가 숫자가 아니다 == 숫자가 맞다

// Number.isNaN은 엄격한 검사
isNaN(123 + 'a')  // true
Number.isNaN(123 + 'a')  // false
```

​    

> JS에서 가장 많이 표기할 수 있는 정수의 범위

```js
Number.MAX_SAFE_INTEGER  // 9007199254740991
```

> 정수인지 확인

```js
Number.isInteger
```

​    

---

## 3️⃣ 경계 다루기

### 1. min-max

- 포함 여부를 결정해야함 (이상 - 초과 / 이하 - 미만)
- 네이밍에 최솟값과 최댓값 포함 여부를 표현한다. 

```js
const MAX_IN_VALUE = 1;   // 이상
const MIN_IN_VALUE = 45;  // 이하

const MAX_NUMBER_LIMIT = 1  // 초과
const MIN_NUMBER_LIMIT = 45  // 미만
```

​    

### 2. begin-end / first-last

```js
function reservationDate(beginDate, endDate) {}
function getLists(first, last) {}
```



### 3. 매개변수의 순서는 경계

- 호출하는 함수의 네이밍과 인자의 순서의 연관성을 고려한다.

1. 매개변수를 2개가 넘지 않도록 만든다.
2. arguments, res parameter 이용
3. 매개변수를 객체에 담아서 넘긴다.

```js
function aFunc( {arg1, arg2, arg3, arg4} )
```

4. 랩핑하는 함수 사용

 ```js
 function getFunc(arg1, arg3) {
   aFunc(arg1, undefined, arg3)
 }
 ```

​    

---

## 4️⃣ 분기 다루기

### 0. 값식문

```jsx
// JSX
<div id={if (condition) { 'msg' }}>내용</div> // 불가능한 문법

// transformed to JS
React.createElement('div', {id: if (condition) { 'msg' }}), '내용');  // 해석불가
```

- JSX에서 바벨을 통해 트랜스파일링되면 객체로 바뀜, 이때 그 내부에는 값과 식만 넣을 수 있음
- ( ) : 함수 / { } : 값, 식만
- if, for, switch문 사용불가

```jsx
// if문 대신 사용
{condition1 && <div>1</div>}
{condition2 && <div>2</div>}
{!condition2 && <div>3</div>}
```

​    

### 1. 삼항연산자

```js
조건 ? 참[식] : 거짓[식]
```

- 3개의 피연산자
- 값으로 귀결됨

```js
cosnt a = condition
	? (b === 0 ? 'ok' : 'no')  // 괄호로 명시적으로 나눠줌
	: 'negative';
```

- 빈값이 가능한 상황에 사용

```js
cosnt welcomeMessage = (isLogin) => {
  conse name = isLogin ? getName() : '이름없음';
  
  return `반가워요 ${name}`;
}
```

- 반환이 있는 것들만 사용한다.

```js
// Bad
function alertMessage(isAdult) {
  isAdult
  	? alert('o');  // alert는 반환값이 없음
    : alert('x');
}

// Good
function alertMessage(isAdult) {
	return isAdult ? 'o' : 'x';
}
```

​    

### 2. Truthy, Falsy

```js
function printName(name) {
  if (!name) {
    return '사람이 없네요';
  }
  
  return '안녕하세요' + name + '님';
}

console.log(printName());  // 사람이 없네요
```

​    

### 3. 단축평가 (short-circuit-evaluation)

- AND 연산자 : 모두가 참인 것을 확인

```js
true && true && '도달O'[v]  // '도달O'
true && false[v] && '도달X'  // false
```

- OR 연산자 : 하나라도 참이면 참

```js
false || false || '도달O'[v]  // '도달O'
true[v] || false || '도달X'  // true
```

​    

### 4. else if / else 피하기

- 많이 길어지면 switch문 사용

```js
// 기본
if (x >= 0) {
  console.log('x는 0과 같거나 크다');
} else if (x > 0) {
  console.log('x는 0보다 크다');
}

// 추천하는 코드
if (x >= 0) {
  console.log('x는 0과 같거나 크다');
} else {
  if (x > 0) {
  console.log('x는 0보다 크다');
	}
}
```

```js
// 기본
function getActiveUserName(user) {
  if (user.name) {
    return user.name;
  }
  
  return '이름 없음'
}

// Good
function getActiveUserName(user) {
  if (user.name) {
    return user.name;
  }
  
  return '이름 없음'
}
```

​    

### 5. Early Return

- 함수를 미리 종료
- 사고하기 편함

```js
// 기본
function loginService(isLogin, user) {
  if (!isLogin) {  // 로그인 여부
    if (checkToken()) {  // 토큰 존재
      if (!user.nickname) {  // 기가입 유저 확인
        return registerUser(user);
      } else {
        refreshToken();
        
        return '로그인 성공';
      }
    } else {
      throw new Error('No Token');
    }
  }
}

// Good
function login() {
  refreshToken();
  
  return '로그인 성공';
}
 
function loginService(isLogin, user) {
  if (isLogin) {
    return
  }
  
  if (!checkToken()) {
    throw new Error('No Token');
  }
  
  if (!user.nickName) {
    return registerUser(user);
  }
  
	login();
}
```

​     

### 6. 부정조건문 지양하기

```js
// 나쁜 예시
if (!isCondition) {
  console.log('거짓인 경우에만 실행')
}

// 좋은 예시
function isNumber(num) {
  return !Number.isNaN(num) && typeof num === 'number'
}

if (isNumber(5)) {
  console.log('숫자 O')
}
```

- 생각을 여러번 해야할 수 있다.
- 프로그래밍 언어자체로 if문이 처음오고 true부터 실행됨
- 부정 조전 예외
  - Early Return, Form Validation (유효성검증), 보안, 계속 검사하는 로직

​     

### 7. Default Case 고려하기

- 함수에서 값이 없을때 사용되는 경우도 고려하여 default 처리를 해주는게 좋음

```js
function sum(x, y) {
  x = x || 1  ✔️
  y = y || 1  ✔️
  
  return x + y;
}

sum();  // 1
```

- 자주 사용하는 값들은 논의를 통해 지정해 놓으면 편함

```js
function createElement(type, height, width) {
  const element = document.createElement(type || 'div');  ✔️
  
  element.style.height = height || 100;  ✔️
  element.style.height = width || 100;  ✔️
  
  return element;
}

createElement();  
```

- 유저의 Input 값을 받을 때, 오타를 염두해야함

```js
function registerDay(userInputDay) {
  switch (userInputDay) {
    case '월'
    case '화'
    case '수'
    case '목'
    case '금'
    case '토'
    case '일'
    default:
      throw Error('입력값이 유효하지 않습니다.')
  }
}
```

```js
function safeParseInt(number, radix) {
  return parseInt(number, radix || 10);
}
```

​    

### 8. 명시적 연산자사용 

```js
function increment() {
  number++;  // 지양
  number = number - 1  // 지향
  ( ( (a+b) * 2) && 3 )
}
```

- 예측 가능하고 디버깅 하기 쉬움
- 연산자 우선순위는 `( )`로 구분

​    

### 9. NULL 병합연산자  (`??`)

- null과 undefined를 평가할때만 사용해야함 (모든 falsy에 적용 x)

```js
fucntion createElement(type, height, width) {
  const element = document.createElement(type ?? 'div');
  
  element.style.height = String(height ?? 10) + 'px';
  element.style.width = String(width ?? 10) + 'px';
  
  return element;
}

const el = createElement('div', 0, 0);
el.style.height  // '0px'
el.style.height  // '0px'
```

​     

### 10. 드모르간의 법칙 활용하기

```js
if (!(A || B)) {}
== if (!A && !B) {}
```



