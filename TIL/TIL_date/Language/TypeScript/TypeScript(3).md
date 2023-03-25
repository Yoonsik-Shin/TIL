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



### JSX 타입지정

```jsx
const div: JSX.Element = <div></div>
const button: JSX.Element = <button></button>
```

​    

### Component 타입지정

```tsx
interface IProps = {
  a: string;
}

function App(props: IProps): JSX.Element {  // JSX.Element는 생략가능
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



---

## 8️⃣ interface 하나로 합쳐 관리하기

```typescript
interface IUser {
  name: string;
  age: number;
}
interface IBook {
  title: string;
  price: number;
}

// 카트서비스에 대한 타입 모아놓기
interface IUserCartService { 
  user: IUser;
  book: IBook;
}

const login = (user: IUserCartService['user']) {}  // 카트 서비스의 유저정보 ✔️✔️
login({ name: 'yoonsik', age: 27 })

const searchBook = (user: IUserCartService['book']) {}  // 카트 서비스의 책정보 ✔️✔️
searchBook({ title: 'bookbook', price: 27000 })
```

