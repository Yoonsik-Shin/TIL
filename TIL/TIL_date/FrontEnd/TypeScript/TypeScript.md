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
    "target": "es5",
    "module": "commonjs",
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

- 타입 지정하기
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

- Union Type : OR 사용 (문자열이거나 숫자)

```tsx
let name :string | number = 'shin'; 
```

​     

- 함수에 타입지정

```tsx
function Func(x :number) :number {
  return x * 3
}
```

​    

- Type alias : 타입 따로 관리

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

- Class

```tsx
class User {
  name :string;
  constructor(name :string){
    this.name = name;
  }
}
```

