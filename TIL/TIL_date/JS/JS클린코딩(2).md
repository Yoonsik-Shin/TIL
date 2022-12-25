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
const orders = ['First', 'Second', 'Third']
const { 0: st, 2: rd } = orders

console.log(st)  // First
console.log(rd)  // Third
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

