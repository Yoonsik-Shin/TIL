# JS클린코딩 (2)

​    

## 1️⃣ 배열 다루기

### 1. JS의 배열은 객체와 유사

 ```js
 cosnt arr = [1, 2, 3];
 
 arr[3] = 'test';
 arr['property'] = 'string';
 arr['obj'] = {};
 arr[{}] = [1, 2, 3];
 arr['func'] = function () {
   return 'hello';
 }
 
 for (let i = 0; i < arr.length; i++) {
   console.log(arr[i]);
 }
 // 1
 // 2
 // 3
 
 // 배열이 객체와 유사하게 생김
 console.log(arr)
 >> 
 [
 	1,
   2,
   3,
   'test',
   property: 'string',
   '[object Object]': [1, 2, 3],
   func: [lamba]
 ]
 ```

- 배열은 인덱스가 키인 객체로 볼수 있다.

```js
const arr = [1, 2, 3];

const obj = {
  0: 1,
  1: 2,
  2: 3,
}
```

- 배열 확인법

```js
const arr = [1, 2, 3]
const arr = '[1, 2, 3]'

// 이 방법으로는 배열인지 문자열인지 확인 못함
if (arr.length) {
  console.log('배열O') 
}
if (typeof arr === 'object') {}

// Old한 방법
if (arr in Array) {}
if (arr instanceof Array) {}

// 추천하는 방법 ✔️
Array.isArray(arr)  // true/false
```

​    

### 2. length

- JS의 length는 절대 배열의 길이를 보장하지는 못한다.

```js
const arr = [1, 2, 3];
console.log(arr.length);  // 3

// 강제로 값 할당 
arr.length = 10;
console.log(arr.length);  // 10
console.log(arr)
>> [1, 2, 3, , , , , , , ]  // 오류발생
```

- 마지막 요소의 인덱스가 length의 길이이다. 

```js
const arr = [1, 2, 3];
arr[9] = 10;
console.log(arr)
>> [1, 2, 3, , , , , , , 10]
console.log(arr.length);  // 10
```

- length를 배열 초기화에 이용하기

```js
cosnt arr = [1, 2, 3]

// 방법1
Array.prototype.clear = function () {
  this.length = 0;
}

arr.clear()
console.log(arr)
>> []

// 방법2
function clearArray(array) {
  array.length = 0;
  
  return array;
}

console.log(clearArray(arr));
>> []
```

​    

### 3. 배열 요소 접근

```js
// 기본
function clickGroupButton() {
  const confirmButton = document.querySelector('button')[0];
  const cancelButton = document.querySelector('button')[1];
  const resetButton = document.querySelector('button')[2];
}

// 리팩토링
function clickGroupButton() {
  const [confirmButton, cancelButton, resetButton] = document.querySelector('button');
}
```

- 배열에 하나의 요소만 있어도 구조분해할당을 할 수 있다.

```js
const date = a[0]
const [date] = a
```

- 간단한 유틸함수를 만들어서 명시적으로 표현해준다.

```js
function head(arr) {
  return arr[0] || ''
}

function day(targetDate) {
  const date = head(targetDate)
}
```

​    

### 4. 유사 배열 객체

- `Array.from()` : 내장 메서드, 객체들을 배열로 바꿔줌
- `arguments` : 유사 배열 객체 (배열아님)

```js
const arrayLikeObject = {
  0: 'HELLO',
  1: 'WORLD',
  length: 2,
}

const arr = Array.from(arrayLikeObject)
console.log(arr)  // ['HELLO', 'WORLD']
console.log(Array.isArray(arr));  // true
console.log(Array.isArray(arrayLikeObject));  // false
```

​    

> `arguments`

- 유사배열객체 (배열아님)
- for문 사용가능
- 고차함수 사용불가

```js
function generatePriceList() {
  
  for (let index = 0; index < array.length; index++) {
    const element = arguments[index];  ✔️✔️
    console.log(Array.isArray(arguments))  // false
    console.log(element)  // 100, 200, 300, 400, 500
  }
  
  return arguments.map((arg) => arg + '원');
}

generatePriceList(100, 200, 300, 400, 500)
```

​    

### 5. 불변성 (immutable)

- 불변성 지키기 : 원본배열 훼손 방지

```js
const originArray = ['a', 'b', 'c'];
const newArray = [...originArray];
```

1. 배열을 복사한다.
2. 새로운 배열을 반환하는 메서드들을 활용한다.
   1. filter()
   2. map()
   3. slice()

​    

### 6. for문 고차함수로 리팩토링

- 요구사항
  1. 원화표기
  2. 1000원 초과 리스트만 출력
  3. 가격순 정렬

```js
const price = ['2000', '5000', '1000', '3000', '4000']

// 리팩토링 전
function getWonPrice(priceList) {
  let temp = [];
  
  for (let i = 0; i < priceList.length; i++) {
    temp.push(priceList[i] + '원');
  }
  
  return temp;
}
```

```js
// 리팩토링(1) : 명시적이지 않은 for문 제거
function getWonPrice(priceList) {
  return priceList.map((price) => price + '원');
}
```

```js
// 리팩토링(2)
const suffixWon = (price) => price + '원'
const isOverOneThousand = (price) => Number(price) > 1000  // 2번 요구사항
const ascendingList = (a, b) = > a - b  // 3번 요구사항

function getWonPrice(priceList) {
  const isOverList = priceList.filter(isOverOneThousand);  // 2번 요구사항
  const sortList = isOverList.sort(ascendingList);  // 3번 요구사항
  
  return sortList.map(suffixWon);
}
```

​     

#### 메서드 체이닝

```js
// 리팩토링(3)
const suffixWon = (price) => price + '원'
const isOverOneThousand = (price) => Number(price) > 1000  // 2번 요구사항
const ascendingList = (a, b) = > a - b  // 3번 요구사항

function getWonPrice(priceList) {

  return priceList
    .filter(isOverOneThousand)  // 2번 요구사항
  	.sort(ascendingList)  // 3번 요구사항
  	.map(suffixWon);
}
```

​    

### 7. map과 forEach의 차이

1. 반환이 있는가

- `forEach` :  반환값 x, 요소가 루프될때마다 함수를 실행시켜줌
- `map` : 반환값 o, 새로운 배열을 만들때 사용

```js
const counts = ['100', '200', '300']

const newCountsForEach = counts.forEach((count) => {
  return count + '개';
})

const newCountsMap = counts.map((count) => {
  return count + '개';
})

console.log(newCountsForEach)  // undefined
console.log(newCountsMap)  // ['100개', '200개', '300개']  :  새로운 배열 생성
```

​    

#### Break, Continue

- 자주하는 실수 : 특정 배열까지만 반복하고 싶을 때 break or continue 문 사용

```js
const orders = ['first', 'second', 'third'];

orders.forEach[map]((order) => {
  if (order === 'second') {
    break[continue];
  }
})

>> SyntaxError: Unsyntactic break[continue]
```

- 해결법

  - `try-catch` 구문 이용하기 

  ```js
  const orders = ['first', 'second', 'third'];
  
  try {
    orders.forEach[map]((order) => {
    	if (order === 'second') {
      	throw
    	}
    	console.log(order);
    });
  } catch (e) {
     
  }
  ```

  - `for`문 사용하기
  - 특수 메서드 이용하기
    - `.every()` : &&
    - `.some()` : ||
    - `.find()`
    -  `.findIndex()`

​    

---

## 2️⃣ 객체 다루기

### Shorthand properties

```js
// 적용 x
const counterApp = combineReducers({
  counter: counter,
  extra: extra,
  counter2: counter2,
  ...
})

// 적용 o
const counterApp = combineReducers({
  counter,
  extra,
  counter2,
  ...
})
```

```js
const firstName = 'poco';
const lastName = 'jang';

// 적용 x
const person = {
  firstName: 'poco',
  lastName: 'jang',
  getFullName: function () {
    return this.firstName + ' ' + this.lastName;
  }
}

// 적용 o
const person = {
  firstName,
  lastName,
  // concise Method
  getFullName() {
    return this.firstName + ' ' + this.lastName;
  }
}
```

​    

### Computed Property Name

```js
const [state, setState] = useState({
  id: '',
  password: '',
})

const handleChange = (e) => {
  setstate({
    [e.target.name]: e.target.value,  ✔️✔️
  })
}

return (
	<>
  	<input value={state.id} onChange={handleChange} name='name' />
  	<input value={state.password} onChange={handleChange} name='name' />
  </>
)
```

​     

### Lookup Table

```js
// 리팩토링 전
function getUserType(type) {
  if (type === 'ADMIN') {
    return '관리자';
  } else if (type === 'INSTRUCTOR') {
    return '강사';
  } else if (type === 'STUDENT') {
    return '수강생';
  } else {
    return '해당없음';
  }
}

// 리팩토링(1) ✔️✔️
const USER_TYPE = {
    ADMIN: '관리자',
    INSTRUCTOR: '강사',
    STUDENT: '수강생',
    UNDEFINED: '해당없음',
  }

import USER_TYPE from './constants/..abc.js'

function getUserType(type) {
  
  return USER_TYPE[[type] ?? USER_TYPE[UNDEFINED]
}

// 리팩토링(2)
function getUserType(type) {
  return(
    {
      ADMIN: '관리자',
      INSTRUCTOR: '강사',
      STUDENT: '수강생',
    } [type] ?? '해당없음'
  )
}
```

> JS는 상수는 Snake Case로 작성하는 불문율이 있다.

​    

### Object Destructuring (객체구조 분해할당)

- 활용시 매개변수들의 순서를 지키지 않아도됨

```js
// 활용 x : 매개변수 순서 중요
function Person(name, age, location) {
  this.name = name;
  this.age = age;
  this.location = location;
}

const yoonsik = new Person('yoonsik', 27, 'korea')

// 활용 o
function Person({name, age, location}) { ✔️✔️
  this.name = name;
  this.age = age ?? 27;
  this.location = location ?? 'korea';
}

const yoonsik = new Person({
  name: 'yoonsik', 
  age: 27, 
  location: 'korea'
})
```

- 필수로 받아야하는 매개변수

```js
// name 매개변수는 필수
function Person(name, { age, location }) { ✔️✔️
  this.name = name;
  this.age = age ?? 27;
  this.location = location ?? 'korea';
}

const yoonsikOptions = {
  age: 27, 
  location: 'korea'  
}

const yoonsik = new Person('yoonsik', {
	age: 27, 
  location: 'korea'  
})
```

​     

- 또다른 활용법

```js
// 배열
const orders = ['First', 'Second', 'Third']
const { 0: st, 2: rd } = orders

console.log(st)  // First
console.log(rd)  // Third
```

```js
// 객체
const user = {
  name: 'shin',
  age: 27,
  createdAt: '2022-12-29',
}

const { name, age, createdAt } = user

console.log(name)  // shin
console.log(createdAt)  // 2022-12-29
```

​     

### Object freeze

- `Object.freeze()` : 객체값이 변하지 않도록 해줌

```js
const STATUS = Objects.freeze({
  PENDING: 'PENDING',
  SUCCESS: 'SUCCESS',
  FAIL: 'FAIL',
})

STATUS.PENDING = 'PPP'  // 변하지않음
STATUS.NEW_ONE = 'P'  // 새로운 프로퍼티도 추가되지않음
```

- `Object.isFrozen()` : 객체가 잘 동결되었는지 확인해줌

```js
Object.isFrozen(STATUS)  // true
Object.isFrozen(STATUS.SUCCESS)  // true
```

> 주의사항

- Deep freezing은 안됨

```js
const STATUS = Objects.freeze({
  PENDING: 'PENDING',
  SUCCESS: 'SUCCESS',
  FAIL: 'FAIL',
  OPTIONS: {
    GREEN: 'GREEN',
    YELLOW: 'YELLOW',
  }
})

Object.isFrozen(STATUS.OPTIONS)  // false

STATUS.OPTIONS.GREEN = 'G'  // 기존값 변함
STATUS.OPTIONS.WHITE = 'WHITE'  // 새로운 값 생성됨
```

- 해결법
  - TypeScript 사용 (readonly)
  - 직접 유틸함수 생성

```js
const STATUS = deepFreeze({
  PENDING: 'PENDING',
  SUCCESS: 'SUCCESS',
  FAIL: 'FAIL',
  OPTIONS: {
    GREEN: 'GREEN',
    YELLOW: 'YELLOW',
  }
})

function deepFreeze(targetObj) {
  // 1. 객체를 순회
  Object.keys(targetObj).forEach(key => {
    // 2. 값이 객체인지 확인
    // 3. 객체이면 재귀
    if (객체) {
      deepFreeze(targetObj)
    }
  })
  // 4. 그렇지않으면 Object.freeze
  return Object.freeze(targetObj);
}
```

​    

### hasOwnProperty

- 해당 프로퍼티가 있는지 없는지 확인

```js
const person = {
  name: 'yoonsik',
}

person.hasOwnProperty('name')  // true
person.hasOwnProperty('age')  // false
```

- 안전하게 사용하기 : `Object.prototype.hasOwnProperty.call(객체, 속성)`

```js
const wrong = {
  hasOwnProperty: function () {
    return 'hasOwnPropery';
  }
  wrongThing: 'string',
}

console.log(wrong.hasOwnProperty('wrongThing'))  // hasOwnPropery
console.log(Object.prototype.hasOwnProperty.call(wrong, 'wrongThing')  // true

// 함수활용
function hasOwnProp(targetObj, targetProp) {
  return Object.prototype.hasOwnProperty.call(
  	targetObj,
    targetProp,
  )
}

hasOwnProp(person, 'name')  // true
hasOwnProp(wrong, 'wrongThing')  // true
```

​     

### 직접 접근 지양하기

- 모델에는 직접 접근을 지양하고, 모델에 대신 접근해주는 함수나 메서드를 활용한다.

```js
// 리팩토링 전
const model = {
  isLogin: false,
  isValidToken: false,
}

function login() {
  model.isLogin = true;
  model.isValidToken = true;
}

function logout() {
  model.isLogin = false;
  model.isValidToken = false;
}

someElement.addEventListener('click', login);

// 리팩토링
// 모델에 대신 접근
function setLogin(bool) {
    model.isLogin = bool;
  	serverAPI.log(model.isLogin)
}

function setToken(bool) {
  	model.isValidToken = bool;
  	serverAPI.log(model.isisValidToken)
}

// 모델에 직접 접근할 수 없음
function login() { 
  setLogin(true);
  setToken(true);
}

function logout() {
  setLogin(false);
  setToken(false);
}
```



---

## 3️⃣ 함수 다루기

### 함수, 메서드, 생성자 이해하기

```js
// 함수
function func() {
  return this;
}

// 메서드
const obj = {
  method() {  // concise method
    return this;
  }
}

const obj = {
  conciseMethod: function () {  // 기본형
    return this;
  }
}

// 생성자 함수
function Func() {
  return this;
}
```



#### 함수

- 1급 객체
- 변수나, 데이터에 담길 수 있음
- 매개변수로 전달 가능 (콜백함수)
- 함수가 함수를 반환 (고차함수)
- `this` : 전역객체를 의미 (global)

#### 메서드

- 객체에 의존성이 있는 함
- `this` : 호출된 객체를 의미

#### 생성자함수

- 인스턴스를 생성하는 역할
- `this` : 생성될 인스턴스를 의미

​    

### argument ? parameter ?

#### Parameter (Formal Parameter)

- 형식을 갖춘, 매개변수

```js
function axios(url) {}
```

​    

#### Argument (Actual Parameter)

- 실제로 사용되는, 인자 / 인수

```js
axios('https://google.com')
```

​    

### 복잡한 인자 관리

```js
// 옛날방식
function createCar(options) {
  var name = options.name
  var brand = options.brand
  var type = options.type
  
  return {
    name: options.name,
    brand: options.brand,
    type: options.type,
  }
}

createCar({
  name: 'name',
  brand: 'brand',
  type = 'type'
})
```

```js
// 최신방식
function createCar({name, brand, type}) {

  return {
    name,
    brand,
    type,
  }
}

createCar({
  type = 'type'
})
```

​    

- 에러메시지를 사용하여 함수를 좀 더 안전하게 사용하기

```js
function createCar({ name, brand, color, type }) {
  if (!name) {
    throw new Error('name is required');
  }
  if (!brand) {
    throw new Error('brand is required');
  }
}

createCar({ name: 'CAR', type: 'SUV'})
>> 'brand is required'
```

​    

### default value 

```js
const required = (argName) => {
  throw new Error('required' + argName);
}

function createCarousel({
  item = required('items'),
  margin = 0,
  center = false,
  navElement = 'div',
} = {}) {  // options = options || {} 와 같은 의미
  
  return {
    margin,
    center,
    navElement,
  }
}

createCarousel() == createCarousel(undefined)
```

​    

### Rest Parameters

```js
function sumTotal(
	initValue,
 	bonusValue,
 	...args  // 나머지 매개변수는 인자중에 가장 마지막에 들어가야함
) {
    
  return args.reduce(
  	(acc, curr) => acc + curr, 
    	initValue,
    	bonusValue,
  )
}

sumTotal(200, 1, 2, 3, 4, 5, 6)
```

​    

### void & return

- ### `void` : 함수에 반환값이 없음

- 반환값이 없는 키워드에는 `return`을 사용하지 않기

- `return`이 없는 함수에 `return`을 사용하면 `undefined` 출력

```js
function handleClick() {
	setState(false);
}

function showAlert(message) {
  alert(message);
}
```

​    

### 화살표함수

- 화살표함수에서는 this의 의미가 달라짐 (lexical scope) => 상위의 문맥을 따름
- `arguments, call, apply, bind`등을 사용할 수 없음
- 생성자로 사용할 수 없음

```js
const Person = (name, city) => {
  this.name = name;
  this.city = city;
}

const person = new Person('shin', 'korea');
>> Person is not a constructor
```

- 클래스 내부의 메서드에는 사용하지 않는걸 추천 (상속시 문제발생 가능성 높음)

​    

### 콜백함수

```js
// 리팩토링 전
function register() {
  const isConfirm = confirm(
  	'회원가입 성공'
  )
  
  if (isConfirm) {
    redirectUserInfoPage();
  }
}

function register() {
  const isConfirm = confirm(
  	'로그인 성공'
  )
  
  if (isConfirm) {
    redirectUserIndexPage();
  }
}


// 리팩토링 후
function confirmModal(message, cbFunc) {
  const isConfirm = confirm(message);
  
  if (isConfirm && cbFunc) {
    cbFunc();
  }
}

function register() {
  confirmModal('회원가입에 성공했습니다.', redirectUserInfoPage)
}

function login() {
  confirmModal('로그인에 성공했습니다.', redirectUserIndexPage)
}
```



​    

### 순수함수 (pure)

```js
// 비순수함수 예시
let num1 = 10;
let num2 = 20;

function inpureSum1() {
  return num1 + num2;
}

inpureSum1()  // 30
inpureSum1()  // 30
num1 = 50  // 외부에서 값을 변경할 수 있음 ✔️✔️
inpureSum1()  // 70
```

- 동일한 값에 동일한 출력

```js
// 순수함수 예시
function pureSum(num1, num2) {
  return num1 + num2
}
```

- 객체, 배열은 새롭게 만들어서 반환하기

```js 
const obj = { one: 1 };

function changeObj(targetObj) {
  return { ...targetObj, one: 100 };
}

changeObj(obj);
obj  // { one: 1 }
```

​    

### Closure 이해하기

 ```js
 function add(num1) {
   return function sum(num2) {
     return num1 + num2;
   }
 }
 
 // 상태를 기억함
 const addOne = add(1); 
 addOne(3)  // 4
 
 const addOne = add(1)(3)  // 4
 ```

```js
function fetcher(endpoint) {
  return function (url, options) {
    return fetch(endpoint + url, options)
    	.then((res) => {
      	if (res.ok) {
          // some codes..
        }
    })
    .catch((err) => console.error(err));
  }
}

const naverApi = fetcher('http://naver.com/')
const daumApi = fetcher('http://daum.net/')

naverApi('/webtoon').then((res) => res);
daumApi('/webtoon').then((res) => res);
```

