#  JavaScript 정리 (3)

​    

## 1️⃣ 배열 메서드

### 1-1. forEach

- 배열 안의 아이템 각각에 대해 함수와 코드를 한번씩 실행
- 반환값 X
- for-of문을 더 자주 사용

```javascript
array.forEach((element[, index[, array]]) => {
  // do something
})
```

- element : 배열의 요소
- index : 배열 요소의 인덱스
- array : 배열 자체

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8]

// 방법1
function print(element) {
  console.log(element);
}
numbers.forEach(print)
>> 1 ~ 8

// 방법2
numbers.forEach(function (el) {
  console.log(el)
})
>> 1 ~ 8
```

​    

### 1-2. Map ✔️✔️

- 배열 안의 아이템들 각각에 함수를 적용해서 새로운 배열에 저장
- 기존 배열 전체를 다른 형태로 바꿀 때 유용

```javascript
array.map(callback(element[, index[, array]]))
```

```javascript
const numbers = [1, 2, 3, 4, 5]

const doubleNums = numbers.map((num) => {
  return num * 2
})

console.log(doubleNums)  //  [2, 4, 6, 8, 10]
```

```javascript
const movies = [
  {
    title: 'abc',
    score: 99
  },
  {
    title: 'def',
    score: 85
  };
]

const titles = movies.map(function (movie) {
  return movie.title;
})
```

​    

### 1-3.  Arrow ❗

- function이라는 키워드 없이도 함수 입력 가능

```javascript
// 기본
const square = (매개변수) => {
  return x ** 2;
}

// return 대신 () 사용  ✔️✔️ 가장 많이 사용
const square = (매개변수) => (
	x ** 2;
)

// 한줄로 표현
const square = (매개변수) => x ** 2;
```

> 다양한 표현 비교

```javascript
// 기본
const isEven = function (num) {
  return num % 2 === 0;
}
// 화살표 기본
const isEven = (num) => {
  return num % 2 === 0;
}
// 인수 소괄호 제외
const isEven = num => {
  return num % 2 === 0;
}
// 실행에 리턴 없애고 중괄호 대신 소괄호 사용 ❗ 조건 하나일때만
const isEven = num => (
  num % 2 === 0;
);
// 한줄로 표현
const isEven = num => num % 2 === 0;
```

```javascript
// map함수
const newMovies = movies.map(movie => (
	`${movie.title} - ${movie.score / 10}`
))
```

​    

> this와 화살표함수

- `this` 키워드는 화살표 함수에서 다르게 동작
- 화살표 함수안에 있는 `this` 키워드는 함수가 만든 범위에 상속되는 `this` 키워드와 같음

​    

### 1-4.  setTimeout

```javascript
setTimeout(함수, x밀리초후 함수 1회 실행)

setTimeout(() => {
  console.log('... are you still there?')
}, 3000)
```

​    

### 1-5. setInterval / clearInterval

```javascript
setInterval(함수, x밀리초 마다 함수 실행)

const id = setInterval(() => {
  console.log(Math.random())
}, 2000;

clearInterval(id);  // 반복 멈춤
```

​    

### 1-6. Filter ✔️✔️

- 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
- 기존 배열의 요소들을 필터링할 때 유용
- 원본은 보존됨

```javascript
array.filter(callback(element[, index[, array]]))
```

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const filter = numbers.filter(n => {
  return n < 5
})

>> [1, 2, 3, 4]
```

​    

### 1-7. Every / Some

- 불리언 메서드 (true / false 반환)

```javascript
array.some(callback(element[, index[, array]]))   // 빈 배열은 항상 거짓 반환
array.every(callback(element[, index[, array]]))  // 빈 배열은 항상 참 반환
```

```javascript
const exams = [80, 98, 92, 78, 77, 90, 89, 84, 81, 77]

// [every] 조건에 안맞는 것이 하나라도 있으면 false반환
exams.every(score => score >= 75)  // 모든 수가 75점보다 높은지 확인
>> true
exams.every(score => score >= 80) 
>> false

// [some] 적어도 하나 이상 참이면 참 반환
exams.some(score => score >= 75)  // 75점보다 높은 점수가 최소 한 개 이상인지 여부
>> true
```

​    

### 1-8. Reduce  ✍️✍️ 

- 배열을 점차 줄여나가면서 마지막에는 결국 하나의 값만 남김

```javascript
[].reduce((리턴연산값,개별요소) => {
  return 리턴연산값과 개별요소 연산
})

[].reduce((acuumulator, currentValue) => {
  return calculation between accumulator and currentValue;
})
```

```java
// 예시 : 총합
[3, 5, 7, 9, 11].reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
})
```

| 콜백함수 | accumulator | currentValue | 리턴값 |
| -------- | ----------- | ------------ | ------ |
| 1        | 3           | 5            | 8      |
| 2        | 8           | 7            | 15     |
| 3        | 15          | 9            | 24     |
| 4        | 24          | 11           | 35     |

```javascript
// 예시 : 최소값
[].reduce((min, current) => {
  if (price < min){
    return price;
  }
  return ;
})
```

​    

### 1-9. find

- 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 `undefined` 반환

```javascript
array.find(callback(element[, index[, array]]))
```

```javascript
const fruits = [
  { name: 'apple', color:'red' },
  { name: 'banana', color:'yellow' },
  { name: 'blueberry', color:'violet' },
]

const result = fruits.find((fruit) => {
  return fruit.name === 'banana';
})

console.log(result)  // { name: 'banana', color:'yellow' } 
```

​    

### 1-10. apply / call

- a 함수의 메서드를 b함수에 적용하고 싶을 때 사용

```js
var person_a = {
   인사 : function(){
     console.log(this.name + '반가워요')
   }
}

var person_b = {
  name: '윤식',
}

person_a.인사.apply(person_b)
>> 윤식반가워요 
person_a.인사.apply(person_b, [1,2])  // == person.인사(1), 인자에 배열만 가능
person_a.인사.call(person_b, 1,2)     // == person.인사(1), 인자에 숫자 가능
```

​    

---

## 2️⃣ JS 최신기능

### 2-1. 디폴트 매개변수 (Default Params)

- 매개변수에 아무 값을 주지않았을 때 자동으로 들어가는 값
- 디폴트 매개변수는 순서가 중요하기 때문에 첫번째에 넣어서는 안됨
- 함수도 가능

```javascript
function multiply(a, ✔️b=1✔️) {
  return a * b;
}

multiply(4)     //  4
multiply(4, 5)  //  20
```

​    

### 2-2. 전개 (Spread)

- 소괄호, 중괄호, 대괄호 안에서만 사용 가능

```javascript
// 숫자
Math.max(1, 2, 3, 4, 5, 6)
>> 6

const nums = [1, 2, 3, 4, 5, 6]
Math.max(nums)  // 배열은 적용이 안됨
>> NaN
Math.max(...nums)  // ... 을 사용하여 배열의 인수가 따로 들어갈 수 있게 만들어줌 (대괄호 삭제)
```

```javascript
// 문자열
console.log('hello')
>> hello

consol.log(...'hello')
>> 'h' 'e' 'l' 'l' 'o'
```

```javascript
// 배열
const cats = ['a', 'b', 'c']
const dogs = ['A', 'B']

const copy = [...cats]  // 컨텐츠 복사 > 메모리 다름
copy
>> ['a', 'b', 'c']
cats
>> ['a', 'b', 'c']

const allPets = [...cats, ...dogs]
allPets
>> ['a', 'b', 'c', 'A', 'B']

const addTurtle = [...cats, ...dogs, '1']
addTurtle
>> ['a', 'b', 'c', 'A', 'B', '1']

// 배열 속 문자열
[...'hello']
>> ["h", "e", "l", "l", "o"] 
```

```javascript
// 객체 리터럴
const dataForm = {
  email: 'abc123@gmail.com'.
  password: 'qwer5678~',
  username: 'yoonsik'
}

// 새로운 객체에 전송받은 객체정보와 추가정보를 하나로 만들어 저장
const newUser = {...dataFrom, id: 1004, isAdmin: false}

newUser
>> {
  email: 'abc123@gmail.com'.
  password: 'qwer5678~',
  username: 'yoonsik',
  id: 1004,
  isAdmin: false
}
```

```javascript
{...[2, 4, 6, 8]} 
>> {0: 2, // 인덱스: 값
    1: 4, 
    2: 6,
   	3: 8
   }

{..."HIII"}
>> {0 "H"  // 인덱스: 값
    1: "I"
    2: "I"
    3: "I"
   }
```

> 카피시에 값 중복이 일어나면? : 가장 뒤에 있는 값을 적용

​    

### 2-3. 나머지 (Rest)

- 매개변수에 `...` 키워드 사용
- 함수의 파라미터에서만 사용
- 매개변수를 배열처럼 묶어줌
- 항상 가장 뒤에 써야함
- 여러번 사용 불가
- 파이썬의 `*arg`

```javascript
function arr(...nums){  // 매개변수가 몇 개가 되던 상관없음
  console.log(nums)
}

arr(34)  >>  [34]
arr(34, 56, 31)  >>  [34, 56, 31]
arr(1, 2, 3, 4, 5, 6)  >>  [1, 2, 3, 4, 5, 6]

// 합계
function sum(...nums) {
  return nums.reduce((total, el) => total + el);
}

sum(1, 2, 3, 4, 5, 6)  >>  21

// ⛔오류발생
function sum(nums) {
  return nums.reduce((total, el) => total + el);
}
sum(1, 2, 3, 4, 5, 6)  >> ⛔오류발생⛔

//
function raceResults(gold, silver, ...everyoneElse) {
  console.log(gold)
  console.log(silver)
  console.log(everyoneElse)            
}

raceResults('a', 'b', 'c', 'd', 'e', 'h')
>> a
>> b
>> ['c', 'd', 'e', 'h']
```

​        

> arguments

- 모든 파라미터를 한번에 다루고 싶을 때 사용
- 배열같은 역할을 해줌
- 모든 파라미터를 `[]`안에 넣은 변수

```js
function 함수(a, b, c){
  console.log(arguments[0]);
  console.log(arguments[1]);
  console.log(arguments[2]);
}
```

​    

### 2-4. 분해 (Destructuring)

- 배열이나 객체의 값을 해체하고 꺼내고 선정하는 방식

```javascript
// 배열
const scores = [100, 98, 90, 86, 81, 75]
const [gold, silver, bronze, ...everyoneElse] = scores;  ✔️✔️

gold  >>  100
silver  >>  98
bronze  >> 90
everyoneElse  >>  [86, 81, 75]
```

```javascript
// 객체
const newUser = {
  email: 'abc123@gmail.com'.
  password: 'qwer5678~',
  username: 'yoonsik',
  id: 1004,
  isAdmin: false
}

const { email } = newUser;   // const email = user.email; 과 같은 구문  ✔️✔️
const { email, password, id } = newUser;  ✔️✔️
email  >>  'abc123@gmail.com'
password  >>  'qwer5678~'
id  >>  1004 

// 다른 이름으로 저장하기
const { username: nickname, isAdmin: ad = '디폴트값' } = user;  ✔️✔️
nickname  >>  'yoonsik'
ad  >>  false
```

```javascript
// 매개변수
const newUser = {
  email: 'abc123@gmail.com'.
  password: 'qwer5678~',
  username: 'yoonsik',
  id: 1004,
  isAdmin: false
}

function userId({newUsername, newId = '디폴트값'}) { ✔️✔️
  return `${newUsername} ${newId}`
}

userId(newUser)
>> yoonsik 1004
```

​    

---

## 3️⃣ JS 라이브러리

> [lodash](https://lodash.com/)

