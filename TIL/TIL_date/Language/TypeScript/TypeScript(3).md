# TypeScript (3)

​    

## 1️⃣ React

### 설치

- typescript가 설치된 react 프로젝트 설치

```bash
$ npx create-react-app 프로젝트명 --template typescript 
```

- 기존 프로젝트에 타입스크립트 추가

```bash
$ npm install typescript @types/node @types/react @types/react-dom @types/jest -D
$ yarn add --dev typescript @types/node @types/react @types/react-dom @types/jest
```

​    

### 파일 확장자

- `tsx` : JSX를 return하는 컴포넌트
- `ts` : 자바스크립트만 사용하는 컴포넌트

​    

### JSX 타입지정

```jsx
const div: JSX.Element = <div></div>
const button: JSX.Element = <button></button>
```

​    

### Component 타입지정

#### props 

- 객체타입
- 주는 입장과 받는 입장이 있음, 타입지정은 받는 입장에서 지정해줘야함

```tsx
// A 페이지
interface IPrint = (a: string) => string

function APage(props: IProps): JSX.Element {
  const print: IPrint = (a) => { return a } 
  const value: number;
  
  return (
  	<Component 
      print={print}
      value={value}
    />
  )
}

// B 페이지
interface IProps = {
  print: IPrint
  value: number
}

function BPage(props: IProps): JSX.Element {  // JSX.Element는 생략가능
  return (
  	<></>
  )
}
```

​    

### State 타입지정

- 자동으로 타입할당됨
- 미리 지정하려면 Generic 사용

```jsx
const [user, setUser] = useState<string | null>('');
```

​       

### Redux

- `initialState`값 타입지정
- reducer 함수의 `action` 파라미터 타입지정
- useSelector에 사용할 store타입 미리 export

```typescript
// store.ts
import { createStore } from 'redux';

interface Counter {
  count: number;
}

const initialState: Counter = { count: 0 };  ✔️✔️

// state에는 초기값 타입이 지정되고, action은 dipatch의 파라미터와 같아야함
function reducer(state=initialState, action: 타입지정필요): Counter {
  if (action.type === 'up') { return { ...state, count: state.count + 1 } } 
  if (action.type === 'down') { return { ...state, count: state.count - 1 } } 
  return initialState
}

const store = createStore(reducer);

// store의 타입 미리 export 해두기 
export type RootState = ReturnType<typeof store.getState>  ✔️✔️
```

```jsx
// App.tsx
import { Provider } from 'react-redux';

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>  
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
) 
```

- `useSelctor` 의 state 타입지정
- redux가 제공하는 `Dispatch`타입사용

```jsx
import React from 'react';
import { useDispatch, useSelector } from 'react-redux'
import { Dispatch } from 'redux'  ✔️✔️
import { RootState } from './store.js'

function App() {
  const reduxValue = useSelector((state: RootState) => state);  ✔️✔️ // store.js에서 정의해놓은 타입
  const dispatch: Dispatch = useDispatch();  ✔️✔️ // redux에서 제공해주는 타입

  return (
    <div className="App">
      { reduxValue.count }
      <button onClick={() => { dispatch({ type : 'up' }) }}>버튼</button>
      <Profile name="kim"></Profile>
    </div>
  )
}
```

​    

### Redux-tookit 

- `initialState`값 타입지정
- reducers 함수의 `action` 파라미터 타입지정, redux-toolkit에서 제공하는 `PayloadAction `타입 사용

```typescript
import { createSlice, configureStore, PayloadAction } from '@reduxjs/toolkit';
import { Provider } from 'react-redux';

interface Counter {
  count: number;
  user: string;
}

const initVal: Counter = { count: 0, user : 'kim' };  ✔️✔️

const counterSlice = createSlice({
  name: 'counter',
  initialState: initVal,
  reducers: {
    increment(state) {
      state.count += 1
    },
    decrement(state) {
      state.count -= 1
    },
    incrementByAmount(state, action: PayloadAction<number>) {  ✔️✔️
      state.count += action.payload
    }
  }
})

let store = configureStore({
  reducer: {
    counter: counterSlice.reducer
  }
})

// state 타입을 export
export type RootState = ReturnType<typeof store.getState>
                                   
export let {increment, decrement, incrementByAmount} = counterSlice.actions
```

​    

---

## 2️⃣ declare

- 이미 정의된 변수, 함수, 타입을 재정의할 수 있음
- .js에 있는 변수를 .ts에서 이용하고 싶을때
- 일반 js 파일에 있던 변수를 쓸 때 에러가 나지 않도록 재정의
- declare가 붙은 코드들은 js로 변환되지 않음

```typescript
// A.js
let a = 1

// b.ts
// 어딘가에 변수 a가 정의되어 있지만, 에러를 발생시키지 말아라
declare let a: number; // 변수를 이 파일에서 잠깐 정의

console.log(a + 1);
```

​    

---

## 3️⃣ Ambient Module

- 타입스크립트에서는 import, export 없이도 타입들을 다른 파일에서 가져다 쓸 수 있음 (__글로벌모듈__)
- import / export 키워드가 쓰이면 그 파일은 __로컬모듈__이 됨

​    

> 로컬모듈에서 전역변수 만들기 (declare global)

```typescript
declare global { 
	type a = string;
}
```

​    

---

## 4️⃣ d.ts 파일

- 타입만 저장할 수 있는 파일형식 (d = definition)
- 자바스크립트로 컴파일 안됨
- 타입정의만 따로 저장해놓고 import 해서 사용
- 프로젝트에서 사용하는 타입을 쭉 정리해놓을 레퍼런스용으로 사용
- ambient module이 아님으로 export 꼭 추가해줘야함 (__로컬모듈__)

```typescript
// ??.d.ts
export type Age = number;
export type multiply = (a: number, b: number) => number // 함수에 { } 중괄호 붙이기는 불가능
export interface Person { name : string }
```

​    

> d.ts 파일 레퍼런스용으로 사용하기

- `tsconfig.json`의 `declaration` 옵션을 설정하면 저장시 자동으로 ts파일마다 d.ts 파일 생성

```json
// tsconfig.json
{
    "compilerOptions": {
        "target": "es5",
        "module": "es6",
        "declaration": true, ✔️✔️
    }
}
```

```typescript
// index.ts
let firstName: string = 'shin';
let age = 27;
interface Person { name: string } 
let people: Person = { name: 'park' }
```

```typescript
// index.d.ts 자동생성됨
declare let firstName: string;
declare let age: number;
interface Person {
    name: string;
}
declare let people: Person;
```

​    

---

## 5️⃣ implements

- interface에 들어있는 속성을 가지고 있는지나 타입을 확인하는 문법 (에러발생시킴)
- ❗타입을 할당하고 변형시키는 키워드 아님

```typescript
interface PhoneType {
  model: string,
  price: number,
}

// Phone 클래스가 PhoneType에 부합하면 정상작동
// 부합하지 않으면 에러발생
class Phone implements PhoneType {  
  model: string;
  price: number = 1000;
  
  constructor(model: string){
    this.model = model
  }
}

const myPhone = new Phone('flip');
```

​    

---

## 6️⃣ Recursive Index Signatures

- 중첩된 object들을 한번에 타입지정하는 방법
- 활용도 낮음

```typescript
// 예시1
interface MyType {
  'font-size': MyType | number  ✔️✔️ 
}

let obj :MyType = {
  'font-size' : {
    'font-size' : {
      'font-size' : 14
    }
  }
}
```

```typescript
// 예시2
interface MyType {
  'font-size': number,  ✔️✔️ 
  [key: string]: number | MyType,  ✔️✔️ 
}

let obj = {
  'font-size' : 10,
  'secondary' : {
    'font-size' : 12,
    'third' : {
      'font-size' : 14
    }
  }
}
```

​    

---

## 7️⃣ keyof

- object의 key를 뽑아 새로운 타입을 만들고 싶을때 사용
- object타입이 가지고 있는 모든 __key값__을 __literal type화__ 한 후, __union type__으로 합쳐서 내보내줌

```typescript
interface Person {
  age: number;
  name: string;
}

type PersonKeys = keyof Person;  // "age" | "name" 타입

let a: PersonKeys = 'age';  // 가능
let b: PersonKeys = 'ageeee';  // 불가능
```

- index signatures 활용 예시

```typescript
interface Person {
  [key: string]: number;
}
interface Animal {
  [key: number]: number;
}

type PersonKeys = keyof Person;  // string | number 타입
type AnimalKeys = keyof Animal  // number 타입

let a: PersonKeys = 'age';  // 가능
let b: PersonKeys = 'ageeee';  // 가능
```

> number 타입도 추가되는 이유

- object의 key값에는 숫자를 넣어도 문자로 치환됨

​    

---

## 8️⃣ Mapped Types

- object 안의 모든 속성들을 한번에 변환하고 싶을 때 사용 (타입변환기)

```typescript
type TypeChanger<T> = {
  [key in keyof T]: 원하는 타입;
}
```

```typescript
// 예시
type Person = {
  name: boolean,
  address: boolean,
  gender: boolean | number,
}

type TypeChanger<T> = {
  [key in keyof T]: string;  // 모든 속성을 string으로 바꾸기
}

type NewType = TypeChanger<Person>

let obj: NewType = {
  name: 'shin',
  address: 'seoul',
  gender: 'male',
}
```

