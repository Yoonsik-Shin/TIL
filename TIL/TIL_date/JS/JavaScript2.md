# JavaScript 정리 (2)

​    

## 1️⃣ 배열 (Arrays)

- 키와 속성들을 담고 있는 참조 타입의 객체(object)
- 대괄호 `[]`
- 순서 존재
- 인덱스 0부터

```javascript
let 배열명 = [];
let 배열명 = [숫자, 문자열, true, NaN, Null, ...];  // 배열 내에 서로 다른 타입 배열 가능

배열명.length              // 배열의 길이 
배열명[idx] = 값;          // 배열 수정
배열명[overIdx] = 값;      // 원래 배열과 새로운 배열 사이에 empty[undefined]가 생기고 overIdx에 값 추가
배열명[배열명.length - 1]  // 배열의 마지막 원소 접근
```

​    

> 내장 메서드

### 1-1.`push / pop`

- 배열의 제일 마지막 값을 넣거나 뺄 떄 사용
- 파이썬의 `append() / pop()` 과 같은 기능

```javascript
배열명.push(마지막에 넣고싶은 항목)
배열명.push(항목1, 항목2)   // 여러 항목을 한번에 넣기도 가능
let 변수 = 배열명.pop()
```

​    

### 1-2.`shift / Unshift`

- 배열의 첫 값을 제거 / 추가

```javascript
let fruits = ['apple', 'banana', 'grape']
let firstFruit = fruits.shift() // 맨 앞에 값 제거
firstFruit  >>  "apple"         // pop된 값 변수지정가능
fruits = ['banana', 'grape']  

fruits.unshift('peach')          // 맨 앞에 값 추가
fruits = ['peach', 'banana', 'grape']
```

​    

### 1-3.`concat`

- 2개의 배열 끼리 접합

```java
const array1 = ['a', 'b', 'c'];
const array2 = ['d', 'e', 'f'];
const array3 = array1.concat(array2);
>> array3 = ['a', 'b'. 'c', 'd', 'e', 'f']
```

​    

### 1-4.`includes`

- 불리언 메소드로 true / false 반환

```javascript
const array1 = [1, 2, 3];
array1.includes(2)  >>  true

const fruits = ['apple', 'banana', 'grape'];
fruits.includes('apple')   >>  true
fruits.includes('nana')    >>  false
```

​    

### 1-5.`indexOf`

- 배열의 인덱스 반환
- 어떤 요소가 배열에 있는지 없는지 알아볼 때 사용

```javascript
const fruits = ['apple', 'banana', 'grape', 'apple'];
fruits.indexOf('apple');     >>  1
fruits.indexOf('cake');      >>  -1
fruits.indexOf('apple', 2)   >>  3    // 일치하는 배열값중에 두번째로 나오는 값의 인덱스 반환
```

​    

### 1-6.`reverse`

- 배열을 뒤집어줌
- 원본을 바꿈 ❗❗

```javascript
const fruits = ['apple', 'banana', 'grape'];
fruits.reverse()  >>  fruits = ['grape', 'banana', 'apple']
```

​    

### 1-7.`slice`

- 배열의 일부를 복사
- 하나의 인수값 : 인수값의 인덱스부터 끝까지
- 두개의 인수값 : 인수값의 인덱스부터 두번째 인수값 인덱스의 -1 값 까지

```javascript
let fruits = ['apple', 'banana', 'grape', 'peach', 'pineapple']
fruits.slice(start[, end])
let 새배열 = fruits.slice(2)     >>  ['grape', 'peach', 'pineapple']  // index : 2 ~ 
let 새배열 = fruits.slice(2, 4)  >>  ['grape', 'peach']    // index : 2 ~ 3
let 새배열 = fruits.slice(-2)    >>  ['peach', 'pineapple']  // index : -1 , -2
```

​    

### 1-8.`splice`

- 삽입, 결합
- 기존 요소들을 제거하거나 대체하거나 새로운 요소들을 추가해 배열 내용 변경
- 원래 배열을 변경 ❗❗

```javascript
months.splice(start[, deleteCount, insert]);

// 삭제
const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
colors.splice(5, 2)  >>  ['indigo', 'violet']   // 변수,배열 지정 가능
colors = ['red', 'orange', 'yellow', 'green', 'blue']

// 삽입
colors.splice(1, 0, "red-orange")
colors = ['red', 'red-orange', 'orange', 'yellow', 'green', 'blue']
```

​    

### 1-9.`sort`

- 배열을 줄이는 메서드
- 원본이 변형됨
- 다른 언어와 기능 다름 ❗❗

```javascript
const months = ['Jan', 'March', 'April', 'June']
months.sort();  >>  ["Dec", "Feb", "Jan", "March"] // UTF16 코드 유닛값을 비교
  
let scores = [1, 70, 100, 2500, 9, -12, 0, 34]
scores.sort()  >>  [-12, 0, 1, 100, 2500, 34, 70, 9] // 첫번째 자리 숫자만 계산하여 정렬
```

```javascript
// 숫자 오름차순 정렬
let scores = [3, 1, 5, 9 , 40]
scores.sort((a,b)=>{
  return a-b
  // return값 양수 : a를 오른쪽
	// return값 음수 : b를 오른쪽  
})

// 숫자 내림차순 정렬
let scores = [3, 1, 5, 9 , 40]
scores.sort((b,a)=>{
  return b-a
  // return값 양수 : a를 오른쪽
	// return값 음수 : b를 오른쪽  
})

// 문자 내림차순 정렬
var arr = ['가', '다', '나']
arr.sort((a,b){
	if (a < b) {  // 
  	return 1
	} else if {   // 
    return -1
  } else {      // 같은 문자일 경우
    return 0 
  }
})
```

​    

### 1-10. join

- 배열의 모든 요소 연결

```javascript
const numbers = [1, 2, 3, 4, 5]

result = numbers.join()     // 1,2,3,4,5
result = numbers.join('')   // 12345
result = numbers.join(' ')  // 1 2 3 4 5
result = numbers.join('-')  // 1-2-3-4-5
```

​    

> 배열과 const의 관계

```javascript
const nums = [컨텐츠];   // 배열이 메모리에 할당, 컨텐츠 내용은 마음대로 변경가능
nums = [New컨텐츠];      // ⛔ const 사용시 배열 재선언은 안됨 ⛔ 
```

​    

---

## 2️⃣ 객체 (objects)

- 프로퍼티 (Property) : 두개의 정보가 모인 것 / 키-값 (Key-Value)으로 구성
- 이 프로퍼티들이 모인것이 객체 (Objects)
- 파이썬의 딕셔너리와 유사
- 키는 어떠한 속성이든 저장될 떄는 문자열로 저장됨

```javascript
const fitBitDate = {
  totalSteps : 308727,
  totalMiles : 211.7,
  avgCalorieBurn : 5755,
  workoutsThisWeek : `5 of 7`,
  avgGoodSleep : `2:13`
};
```

- 객체에서 값 추출

```javascript
1. 객체명["키"]  >>  값
2. 객체명.키  >>  값    // 키는 저장될 때 문자열로 변환되어 저장됨
```

- 객체 수정 / 추가

```javascript
1. 객체명["기존키/새키"] = 바꿀값/넣을값
2. 객체명.기존키/새키 = 바꿀값/넣을값
```

​    

---

## 3️⃣ 루프 (Loops)

### 3-1. for문

```javascript
// 기본
for (initialExpression; condition; incrementExpression;) {
  statement;
}

// of문 사용
for (vaiable of iterable) {
  statement;
}
```

```javascript
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```

​    

> 배열 루프 ✔️

```javascript
for (initialization; condition; expression) {
  // do something;
}
```

- initialization : 최초 반복문 진입 시 1회만 실행되는 부분
- condition : 매 반복 시행 전 평가되는 부분
- expression : 매 반복 시행 이후 평가되는 부분

```javascript
// 기본
const fruits = ['apple', 'banana', 'grape'];

for (let i = 0; i < fruits.length; i++) {
  console,log(i, fruits[i]);
}

>> 0 'apple'
>> 1 'banana'
>> 2 'grape'

// 자주 사용 [ of ]
for (let fruit of fruits) {
  console.log(fruit)
}
```

```javascript
// 중첩 for문
const AlphabetChart = [
  ['a', 'b', 'c'],
  ['d', 'e', 'f'],
  ['g', 'h', 'i']
]

for (let i = 0; i < AlphabetChart.length: i++) {
  const row = AlphabetChart[i];   // 놓치기 쉬운 부분 ❗
  for (let j = 0; j < row.length; j++) {
    console.log(row[j])
  }
}

// of 사용
for (let row of AlphabetChart) {
  for (let col of row) {
    console.log(col);
  }
}
```

​    

>객체 반복

```javascript
Object.keys(객체)    // 키 반환
Object.values(객체)  // 값 반환
Object.entries(객체) // [키, 값] 반환

const testScores = {
  a : 100;
  b : 90;
  c : 35;
}

let total = 0;
let scores = Object.values(testScores);
// 평균 구하기
for (let score of scores) {
  total += score;
}
console.log(total / scores.length);
```

​    

### 3-2. While문

```javascript
let num = 0;
while (num < 10) {
  num++
  console.log(num);
}
>> 1 ~ 10
```

​    

---

## 4️⃣ 함수 선언식 (Fuction)

- 함수정의 및 실행

```javascript
// 정의
function 함수명() {
  실행문;
  return 반환;
}

// 실행
함수명()
```

​    

>범위

함수 범위 (Function Scope)

블록 범위 (Block scope)

- if, for, 함수등의 중괄호 [`{}`] 내부
- 블록 바깥에서 접근 불가능

렉시컬 범위 

- 중첩된 함수나 내부함수는 상위 몇 레벨위에 있든 상관없이 부모함수의 항목 접근 가능

​    

---

## 5️⃣ 함수 표현식 (Function Expressions)

- 파이썬의 람다함수
- 선언식보다 표현식을 더 자주 씀

```javascript
const 변수 = function () {    // 함수명 x 
  return ;
}

// 호출
변수(인수);
```

​    

> 함수 선언식, 표현식 비교 정리

|        | 함수 선언식 (declaration) | 함수 표현식 (expression) |
| ------ | ------------------------- | ------------------------ |
| 차이점 | 익명함수X, 호이스팅 O     | 익명함수O, 호이스팅 X    |

​    

---

## 6️⃣ 고차함수 (Higer Order Functions)

- 다른 함수를 인수로 받아 사용

```javascript
function callTwice(func) {
  func();
  func();
}

function rollDie() {
  return a;
}

callTwice(rollDie)
>> a
>> a
```

```javascript
// 팩토리 함수
function makeBetweenFunc(min, max) {
  return function (num) {
    return num >= min && num <= max;
  }
}
```

​    

---

## 7️⃣ 메서드 만들기

- 메서드 = 객체에 속성으로 추가된 함수

```javascript
// 기본
const myMath = {
  PI: 3.14159,
  square: function(num){
    return num ** 2;
  },
  cube: function (){
   	console.log('cube');
  }
}

myMath.PI
>> 3.14159
myMath.square(2)
>> 4
myMath.cube()
>> "cube"


// 최신 문법
const myMath = {
  PI: 3.14159,
  add(x, y) {
    return x + y;
  },
  multiply(x, y){
    return x * y;
  }
}

math.add(50, 60)
```

​    

---

## 8️⃣ this

- 메서드에 있는 객체를 가리킬 때 사용

```javascript
const person = {
  name: 'Yoonsik-Shin',
  height: 178,
  weight: 80,
  selfIntro() {
    console.log(`${this.name} is ${this.height}cm and ${this.weight}kg`)
  }
}

person.selfIntro()
>> Yoonsik-Shin is 178cm and 80kg
```

​    

---

## 9️⃣ Try - Catch문

```javascript
try {
  실행문;
} catch () {
  실행문 에러시 실행되는 문장;
}
```
