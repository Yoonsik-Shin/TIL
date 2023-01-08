# TypeScript

​    

## 사용이유

- 타입을 엄격하게 검사해줌
- 에러메시지 퀄리티가 좋아짐



## 기본 설치

```bash
$ npm install -g typescript
```

- `파일명.ts` 생성
- `tsconfig.json` 생성 : 컴파일시 옵션 설정

```typescript
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
npx create-react-app my-app --template typescript
```

​    

## 기본 문법

### 타입 지정하기

- `string, number, boolean, null, undefined, bigint, [ ], { }`

```typescript
let name :string = 'shin';
name = 123;  // 에러발생

// string이 담긴 변수만 array에 넣을 수 있음
let namesArray :string[] = ['shin', 'yoon']

// Object
let namesObject :{ name?: string } = { name: 'kim' }
let namesObject :{ name?: string } = { }  // 에러 미발생
```

> Object형에서는 `?`로 속성이 옵션임을 알려줌

​    

### Union Type

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

### 함수에 타입지정

- 타입이 지정된 파라미터는 필수요소가 됨


```tsx
function Func(x :number) :number {
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

- `변수? :타입` == `변수 :number | undefined`

```typescript
function Func(x? :number) :number {a
  return x * 3
}
```

​    

### void

- 실수로 뭔가를 return하는 것을 막을 수 있음

```typescript
function Func(x:number):void {
  1 + 1
  return 1 + 1  // 에러발생
}
```

​    

### Type alias 

- 타입 따로 관리
- 첫글자 대문자로 작성
- 재정의 불가능

```tsx
type MyType = string | number;  // 첫글자는 주로 대문자

let name :myType = 123;
```

```tsx
// 배열의 첫번째는 number만 가능, 두번쨰는 boolean만 가능
type Member = [number, boolean];

let john:Member = [123, true]
```

- object에 타입지정 속성이 많을 때

```tsx
type Member = {
  [key :string] : string,  ✔️✔️ // 모든 object 속성
}

let john :Member = { name: 'kim' }
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

> readonly

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

- Class

```tsx
class User {
  name :string;
  constructor(name :string){
    this.name = name;
  }
}
```

​    

- any / unknown

```typescript
let a: any  // 그냥 JS와 같아짐
let b: unknown  // any보다 안전, 제일 최근의 형식 반영
```



> 간단한 수학 연산도 타입이 맞아야함

```typescript
let age: string | number;
age + 1;  // Error 발생 : Union 타입과 number타입 연산 불가
```

​    

### Type Narrowing

- 타입이 아직 하나로 확정되지 않았을 경우 사용
- 어떤 변수의 타입이 아직 불확실할 경우 if문 등으로 Narrowing 해줘야함
- Narrowing 판정 문법
  1. `typeof 변수`
  2. `속성명 in 객체`
  3. `인스턴스 instanceof 부모`

```typescript
function MyFunc(x: number | string) {
  if (typeof x === 'string') {
    return
  } else {
    return
  }
}
```

- if문 사용했으면 else. else if문으로 끝맺어줘야 에러가 발생할 가능성 낮아짐

​     

> assertion

- 타입 덮어쓰기 
- Narrowing 할 때만 사용
- 무슨 타입이 들어올지 확실할 때만 사용

```typescript
function MyFunc(x: number | string) {
	let array: number[] = []
  array[0]  = x as number ✔️✔️
}
```

​        

### Literal type

- 특정 글자나 숫자만 가질 수 있게 제한을 두는 타입

```typescript
function Func(a: 'hi'): 1 | 0 { }  // 0과 1만 return 가능
```

> `as const`

- object value의 값을 그대로 타입으로 지정해줌
- object 속성들에 모두 readonly를 붙여줌

```typescript
let data = {
  name: 'shin'
} as const
```

​    

