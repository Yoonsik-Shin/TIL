# TypeScript (1)

​    

## 0️⃣ 사용이유

- 타입을 엄격하게 검사해줌
- 에러메시지 퀄리티가 좋아짐

​    

---

## 1️⃣ 기본 설치

```bash
$ npm install -g typescript
$ yarn add global typescript
```

- `파일명.ts` 생성
- `tsconfig.json` 생성 : 컴파일시 옵션 설정

```bash
# tsconfig.json 자동생성
$ tsc --init
```

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "target": "es5",  // JS버젼
    "module": "commonjs",
    "allowJs": true, // js 파일들 ts에서 import해서 쓸 수 있는지 
    "checkJs": true, // 일반 js 파일에서도 에러체크 여부 
    "jsx": "preserve", // tsx 파일을 jsx로 어떻게 컴파일할 것인지 'preserve', 'react-native', 'react'
    "declaration": true, //컴파일시 .d.ts 파일도 자동으로 함께생성 (현재쓰는 모든 타입이 정의된 파일)
    "outFile": "./", //모든 ts파일을 js파일 하나로 컴파일해줌 (module이 none, amd, system일 때만 가능)
    "outDir": "./", //js파일 아웃풋 경로바꾸기
    "rootDir": "./", //루트경로 바꾸기 (js 파일 아웃풋 경로에 영향줌)
    "removeComments": true, //컴파일시 주석제거 

    "strict": true, //strict 관련, noimplicit 어쩌구 관련 모드 전부 켜기
    "noImplicitAny": true, //any타입 금지 여부
    "strictNullChecks": true, //null, undefined 타입에 이상한 짓 할시 에러내기 
    "strictFunctionTypes": true, //함수파라미터 타입체크 강하게 
    "strictPropertyInitialization": true, //class constructor 작성시 타입체크 강하게
    "noImplicitThis": true, //this 키워드가 any 타입일 경우 에러내기
    "alwaysStrict": true, //자바스크립트 "use strict" 모드 켜기

    "noUnusedLocals": true, //쓰지않는 지역변수 있으면 에러내기
    "noUnusedParameters": true, //쓰지않는 파라미터 있으면 에러내기
    "noImplicitReturns": true, //함수에서 return 빼먹으면 에러내기 
    "noFallthroughCasesInSwitch": true, //switch문 이상하면 에러내기 
  }
}
```

- `tsconfig.build.json`

```json
{
  "extends": "./tsconfig.json",  // tsconfig 파일과 연결
  "include": ["**/*.ts"],  // 모든폴더의 모든 ts파일
  "exclude": ["node_modules", "test", "dist", "**/*spec.ts"]  // ts 변환 안할 파일설정
}
```



- 타입스크립트 코드를 자동으로 JS 코드로 컴파일하기 

```bash
$ tsc -w
```



### React에서 사용하기

1. 이미 있는 프로젝트

```bash
$ npm install --save typescript @types/node @types/react @types/react-dom @types/jest
```

2. 새로운 프로젝트

```bas 
npx create-react-app 프로젝트명 --template typescript
```

​    

---

## 2️⃣ 기본 문법

### 1. 타입 지정하기

- `string, number, boolean, null, undefined, bigint, [ ], { }`
- 모든 변수에 타입지정 x
- 대부분 타입스크립트가 타입추론을 통해 자동으로 타입 부여

```typescript
let name: string = 'shin';
name = 123;  // 에러발생

// string이 담긴 변수만 array에 넣을 수 있음
let namesArray: string[] = ['shin', 'yoon']

// Object
let namesObject: { name?: string } = { name: 'kim' }
let namesObject: { name?: string } = { }  // 에러 미발생
```

> Object형에서는 `?`로 속성이 옵션임을 알려줌 (없어도 에러x)

​    

#### rest parameter

```typescript
function addAll(...arr: number[]) {
  console.log(arr)  // [1, 2, 3, 4, 5]
}

addAll(1, 2, 3, 4, 5);
```

​    

#### spread 연산자

```typescript
type RestArr = [number, number, ...number[]];

let arr: number[] = [1, 2, 3]
let arr2: RestArr = [4, 5, ...arr]

arr2 = [4, 5, 6, 7, 8, 9, 10]  // 갯수 상관없이 사용가능
```

​    

#### tuple type

- 무조건 타입에 맞는 값만 할당가능

```typescript
type TupleType = [string, boolean]

const tupleT: TupleType = ['abc', true]
```

- tuple 안에도 옵션가능하지만 배열 중간에 있는 자료는 불가능

```typescript
type Num1 = [number, number?, number?]  // 가능
type Num2 = [number, number?, number]  // 불가능
```

​    

### 2. 타입 애매할 때

#### Union Type

-  OR 사용 (문자열이거나 숫자)

```tsx
let name: string | number = 'shin'; 
```

- 타입 합치기

```typescript
type Name = string;
type Age = number;

type Person = Name | Age;
```

​     

#### Intersection Type

- AND 사용

```typescript
interface IName {
  name: string;
}
interface IAge {
  age: number;
}

const nameAndAge: IName & IAge = {
  name: 'shin',
  age: 27,
}
```

​    

#### any

- 아무 값이나 넣을 수 있는 타입
- 에러 방지 효과가 아예 없어 버그 추적이 어려워짐

```typescript
let a: any  // 그냥 JS와 같아짐
```

​    

####  unknown

- 모든 값을 다 집어넣을 수 있음
- 값을 넣어도 타입은 그대로 unknown
- unknown에 다른 타입 넣거나 연산시 에러 발생

```typescript
let b: unknown  // any보다 안전, 제일 최근의 형식 반영
```

​    

> 간단한 수학 연산도 타입이 맞아야함

```typescript
let age: string | number;
age + 1;  // Error 발생 : Union 타입과 number타입 연산 불가
```

​    

### 3. 함수에 타입지정

- 함수는 `파라미터`와 `return` 값에 타입지정가능
- 어디서 몇번이든 호출 가능하므로, 타입추론 할 수 없음
- __타입이 지정된 파라미터__는 __필수요소__가 됨


```tsx
function Func(x: number): number {
  return x * 3
}

Func()  // 오류발생
Func(3)  // 9
```

- type alias 활용

```typescript
type FuncType = (a: string) => number;

let Func: FuncType = function (a) {
  return 10
}
```

​    

> 파라미터 필수요소 해제 (`?`)

- `변수?: 타입` == `변수: number | undefined`
- Object형에서는 `?`로 속성이 옵션임을 알려줌 (없어도 에러x)

```typescript
function Func(x?: number): number {
  return x * 3
}
```

​    

#### void

- 실수로 뭔가를 return하는 것을 막을 수 있음

```typescript
function Func(x:number):void {
  1 + 1
  return 1 + 1  // 에러발생
}
```

​    

### 4. 클래스에 타입지정

- constructor에서 this키워드 사용시 미리 변수를 선언해줘야함
- constructor 함수에는 return 타입지정 x

```tsx
class User {
  name;  ✔️✔️
  
  constructor(k: string){
    this.name = k;
  }
}
```

​    

### 5. 타입 확정하기

#### Type Narrowing

- 타입이 아직 하나로 확정되지 않았을 경우 사용

- 어떤 변수의 타입이 아직 불확실할 경우 if문 등으로 Narrowing 해줘야함

- Narrowing 판정 문법
  1. `typeof 변수`

  ```typescript
  function MyFunc(x: number | string) {
    if (strs && typeof x === 'string') { // null이나 undefined 필터링
      return
    } else {
      return
    }
  }
  
  ```

  > `&&` 연산자

  - 처음 등장하는 falsy값을 찾아줌
  - falsy값이 없다면 마지막값을 넘겨줌

  ​    

  2. `속성명 in 객체(object)`

  ```typescript
  type Fruit = { apple: sting }
  type Vegetable = { potato: string }
  
  function func(food: Fruit | Vegetable) {
    if ('apple' in food) {
      return food.apple
    }
    return food.potato
  ```

  ​    

  3. `인스턴스 instanceof 부모(Class)`

  ```typescript
  let date = new Date();
  
  if (data instanceof Date) {
    
  }
  ```

- if문 사용했으면 else. else if문으로 끝맺어줘야 에러가 발생할 가능성 낮아짐

​     

#### **Type Assertion**

- 타입 덮어쓰기 
- Narrowing 할 때만 사용
- 무슨 타입이 들어올지 확실할 때만 사용 (컴파일러 에러가 발생할 때)
- 왜 타입에러가 나는지 정말 모르겠는 상황에 임시로 에러해결용으로 사용

```typescript
// 변수명 as 타입
function MyFunc(x: number | string) {
	let array: number[] = []
  array[0]  = x as number ✔️✔️
}
```

​        

### 6. 타입 별명 (Type alias)

####  type

- 타입 따로 관리
- 첫글자 대문자로 작성
- 재정의 불가능

```tsx
type MyType = string | number;  // 첫글자는 주로 대문자

let name: myType = 123;
```

```tsx
// 배열의 첫번째는 number만 가능, 두번쨰는 boolean만 가능
type Member = [number, boolean];

let john: Member = [123, true]
```

​    

> object 타입 합치기 (extend)

```typescript
type PositionX = { x: number };
type PositionY = { y: number };

type NewType = PositionX & PositionY 

let position: NewType = { x: 10, y: 20 }
```

​      

#### interface

- `type`키워드와 거의 유사
- 파스칼 케이스로 이름지음

```typescript
interface ISquare {
  color: string,
  width: number,
}

let box: ISquare = {
  color: 'red',
  width: 100.
}
```

​    

#### extends

- 다른 interface의 값을 추가해줄 수 있음

```typescript
interface Student {
  name: string;
}
interface Teacher extends Students {
  age: number;
}
// Teacher 타입은 name과 age 속성을 갖게됨
```

- object 안의 속성이 중복될 경우 에러 발생

```typescript
interface Animal { 
  name: string 
} 
interface Dog extends Animal { 
  name: number 
}
```

​    

> `type`과의 차이점

- extends 문법이 약간 다름 (type은 `&` 사용)
- 타입이름 중복선언시
  - `interface` : 중복선언 허용, extends한 것과 동일하게 동작, 외부 라이브러리 사용시 override 가능
  - `type` : 중복선언 불가, 에러발생
- 다른 사람이 내 코드를 이용하는 상황이 많으면 `interface`가 좋음

​    

#### readonly

- object 자료 수정을 막을때 사용
- ❗타입스크립트의 에러는 에디터/터미널 상에서만 존재함

```typescript
type Friend = {
  readonly name: string  ✔️✔️ 
}

const 친구: Friend = {
  name: "shin"
}
```

​    

#### index signatures

- object에 타입지정 속성이 많을 때

```tsx
type Member = {
  [key: string] : string,  ✔️✔️ // 모든 object 속성
}

let john: Member = { name: 'kim' } // { 모든속성 : string }
```

```typescript
// 에러발생
interface StringOnly {
  age: number,
  [key: string]: string,
}

// 정상작동
interface StringOnly {
  age : string, 
  [key: string]: string,
}

// 정상작동
interface StringOnly {
  age : number,
  [key: string]: string | number,
}
```

​    

### 7. Literal Types

- 특정 글자나 숫자만 가질 수 있게 제한을 두는 타입

```typescript
let name: 'yoonsik' | 'shin';
name = 'yoosik'
name = 'kim' // 에러발생

function Func(a: 'hi'): 1 | 0 {
  // 0과 1만 return 가능
}  
```

​    

### 8. Enum

```typescript
enum authEnum {
  ADMIN = "admin",
  MANAGER = "manager",
  USER = "user",
}

const authInfo: authEnum = authEnum.ADMIN
console.log(authInfo) // admin
```

> js에는 enum이 없기때문에 컴파일되면 enum은 함수형태로 변환됨

```js
// js
var authEnum;
(function (authEnum) {
  authEnum["ADMIN"] = "admin",
  authEnum["MANAGER"] = "manager",
  authEnum["USER"] = "user",
})(authEnum || (authEnum = {}));

var authInfo = authEnum.ADMIN;
```

​    

> 따로 값 설정하지 않으면 0부터 자동으로 값 부여

```typescript
enum testEnum {
  A,
  B,
  C,
}


const testA: testEnum = testEnum.A
const testB: testEnum = testEnum.B
const testC: testEnum = testEnum.C

console.log(testA)  // 0
console.log(testB)  // 1
console.log(testC)  // 2
```

​    

### 9. as const

- object를 잠그고 싶을 때 활용
- object value의 값을 그대로 타입으로 지정해줌
- object 속성들에 모두 readonly를 붙여줌

```typescript
let data = {
  name: 'shin'
} as const
```

​    
