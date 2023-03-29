# TypeScript (2)

​    

## 1️⃣ Never type

- never 타입 조건
  1. 절대 return 값이 없어야함
  2. 함수 실행이 끝나지 않아야함 (endpoint가 없어야함)

```typescript
function Func(): never {
  while ( true ) {
    console.log('never')
  }
}
```

- 모든 JS 함수에는 return undefined라는 코드 숨겨져있음

```typescript
function Func(){
  console.log('')
  // return undefined가 숨겨져있음
  // never타입 사용불가
}
```

- 주로 에러를 던질때 사용

```typescript
function Func(): never {
  throw new Error('에러메세지')
}
```

- `void`타입을 더 많이 사용함
- 잘못된 narrowing을 했을 경우 파라미터의 타입이 never로 변하는 경우가 있음 (수정필요)
- 자동으로 never 타입을 가지는 경우

```typescript
// 함수 선언문 : 아무것도 return 하지 않고 끝나지도 않을 경우 void 타입이 자동으로 return 타입 할당
function Func() {  // void
  throw new Error()
}

// 함수 표현식 :  아무것도 return 하지 않고 끝나지도 않을 경우 never 타입이 자동으로 return 타입 할당
let Func = function () {  // never
  throw new Error()
}
```

- `tsconfig.json`에서 strict옵션이 true일경우 함부로 `any`타입을 지정해주지 않아 `never`타입을 가지는 경우

```typescript
const arr = []; // never[]
```

​    

---

##  2️⃣접근제한자

### public

- public이 붙은 속성은 자식 object에서 마음대로 사용하거나 수정가능
- 붙히나 안붙히나 똑같아서 사용 잘 안함

```typescript
class User {
  public name: string;
  
  constructor() {
    this.name = 'kim';
  }
}

const user = new User();
user.name = 'shin';  // 자식 object에서 수정가능
```

​    

### private

- 해당 class 중괄호 안에서만 수정 및 사용가능
- 자식 object내에서도 private 붙은 속성은 사용불가
- 상속받은 class내에서도 불가능

![image-20230324134736046](TypeScript(2).assets/image-20230324134736046.png)

```typescript
class User {
  private gender: string;
  public name: string;
  public NG;
  
  constructor() {
    this.gender = '남자';
    this.name = '이름';
    this.NG = this.gender + this.name;  // class
  }
}

const user = new User();
user.gender = 'test'  // 자식 object에서 수정불가
```



> private가 부여된 속성을 class 밖에서 수정하고 싶을때

- class 내에 메서드를 활용하여 수정

```typescript
class User {
  private _gender: string;
  
  constructor() {
    this._gender = '남자';
  }
  
  changePrivate(gender: string) {
    this._gender = gender
  }
}

const user = new User();
user.changePrivate('여자')  ✔️✔️ 
console.log(user)  // User { gender: '여자' }
```



> public, private 키워드 활용

```typescript
class Person {
  constructor (
  	public name: string,
    private gender: '남자' | '여자' = 'default value'
  ) {}
}

const people = new Person('shin', '남자')
console.log(people);  // Person { name: 'shin', gender: '남자' }

const people2 = new Person('shin')
console.log(people2)  // Person { name: 'shin', gender: 'default value' }

// default value없이 인자 빼먹으면 undefined 반환
console.log(people2) // Person { name: 'shin', gender: 'undefined' }
```

​     

### protected

- `private`에서 약간 보안을 해제하고 싶을때 사용
- 상속받은 class 안에서도 사용가능
- class끼리 공유할 수 있는 속성이 필요할 때 사용

```typescript
class User {
  protected age = 10;
}

class NewUser extends User {
  changeAge() {
    this.age = 20;
  }
}
```

​    

### static

- 부모 class만 속성을 사용할 수 있게 만들어줌
- 자식 object들은 속성을 사용할 수 없음
- 클래스안에 기본 설정값 입력이나 간단한 메모를 할 때 사용
- class에서 생성된 object가 사용할 필요없는 변수들을 만들고 싶을 때 사용

![image-20230324141645067](TypeScript(2).assets/image-20230324141645067.png)

```typescript
class User {
  static gender = '성별';
  info = User.skill + 'shin';
}

const user = new User();  // user=자식, User=부모
console.log(user.gender)  // 에러발생
console.log(User.gender)  // '성별'
console.log(user)  // User { info: '성별shin' }
```

​     

---

## 3️⃣ 타입 파일분리

### import / export

```typescript
// type.ts
export type Name = string | boolean;
export type Age = (a: number) => number;
```

```typescript
// server.ts
import { Name, Age } from './type'

const name: Name = 'shin';
const Func: Age = (a) => { return a - 5 } 
```

​    

### namespace

- import / export 이전 방식

```typescript
const 변수: 네임스페이스명.타입명 
```

```typescript
// type.ts
namespace MNS {
  export interface PersonInterface { age: number };
  export type NameType = number | string;
} 
```

```typescript
// server.ts
/// <reference path="./type.ts" />

const name: MNS.NameType = 'shin';
const Func: MNS.PersonInterface = (a) => { return a - 3 } 
```

​    

---

## 4️⃣ Generic type

- type을 직접 지정
- 내가 만든 기능을 다른 사람에게 제공하는 경우 사용

![image-20230324170913779](TypeScript(2).assets/image-20230324170913779.png)

```typescript
// generic 타입 - 1
export function getGeneric<MyType1, MyType2, MyType3>(
  arg1: MyType1,
  arg2: MyType2,
  arg3: MyType3
): [MyType3, MyType2, MyType1] {
  return [arg3, arg2, arg1];
}

const result = getGeneric('abc', 123, true) // 자동으로 타입추론 
```

- type명은 따로 의미없음

```typescript
// generic 타입 - 2
export const getGeneric2 = <T, U, V>(arg1: T, arg2: U, arg3: V): [V, U, T] => {
  return [arg3, arg2, arg1];
};

const result2 = getGeneric2("123", 123, true);
```

​    

> 나만의 useState 구현해보기

```typescript
export const useMyState<S>(inputVal: S): [S, () => void] {
	const myState = inputVal;
                                          
	const mySetState = (changeVal) => {
  	// 1. changeVal로 myState 변경
    // 2. 해당 컴포넌트를 리렌더링
  }                                       
	
	return [myState, mySetState]
}

const [count, setCount] = useMyState(10);  // 인자에 따라 자동으로 타입추론
```

​    

> HOF / HOC에서의 Generic

```typescript
// HOF - generic타입 (화살표함수)
export const first = <T>(arg1: T) => <U>(arg2: U): [T, U] => {
    return [arg1, arg2];
  };

const result4 = first("a")(8);


// HOC - generic타입 (컴포넌트에 응용)
export const withAuth = <C>(Component: C) => <P>(props: P): [C, P] => {
    return [Component, props];
  };

const result5 = withAuth("bbb")({ qqq: "철수" });
```

​    

### extends

- Generic의 타입을 제한함

```typescript
interface IObj1 {
  name: string;
  age: number;
}
interface IObj2 {
  city: string;
  phone: number;
}

function printKey<T extends object, U extends keyof T>(params: T, key: U) {
  // T는 object 타입만 가능
  // U는 keyof 키워드로 인해 T에 들어온 객체의 키값만 받음
  // extends 키워드로 인해 T안의 타입만 가능
  retrun params[key]
}

printKey<IObj1, keyof IObj1>({ name: 'yoonsik', age: 27}, "name")
printKey<IObj2, keyof IObj2>({ city: 'seoul', phone: 01011111111}, "phone")
```

​    

---

## 5️⃣ Utility Types

```typescript
export default function TypeScriptUtilityPage() {
  interface IProfile {
    name: string
    age: number
    school: string
    hobby?: string
  }

  // 1. Pick 타입 : 선택한 것들만으로 다시 타입 생성
  type PickType = Pick<IProfile, "name" | "age">

  // 2. Omit 타입 : 선택된 것을 제외한 나머지로 다시 타입 생성
  type OmitType = Omit<IProfile, "school">

  // 3. Partial 타입 : 모든 타입에 ? 넣어줌
  type PartialType = Partial<IProfile>

  // 4. Required 타입 : 모든 타입에서 ? 빼줌
  type RequiredType = Required<IProfile>

  // 5. Record 타입
  type RecordType = "특수" | "타입" | "만"  // Union 타입 : 적혀있는 글자만 들어갈 수 있음

  type EtcType = Record<eee, IProfile>  // key : value 형태로 타입 생성됨

  
  // type과 interface 차이 : 선언병합
  interface IProfile {
    candy: number   // 위에 선언한 타입과 합쳐짐
  }
  
  let profile: Partial<IProfile> = {}
  profile.candy = 10
}
```

​    

---

## 6️⃣ 타입조건식

- `extends`키워드와 삼항연산자를 이용하여 조건부로 타입만들기

```typescript
// T extends string : T라는 파라미터가 string 이면 true 
type People<T> = T extends string ? string : unknown;

const person1: People<string>  // 
```

​    

### infer

- 입력한 타입을 변수로 만들어줌
- 조건문 안에서만 사용가능
- 자주 안쓰임

```typescript
// array 내부의 타입만 뽑기
type Person<T> = T extends (infer R)[] ? R : unknown;  // T의 타입을 추출하여 R이라는 변수에 담아줌
type NewType = Person<string[]>  // T: string[], R: string

// 함수의 return 타입만 뽑기
type Person<T> = T extends () => infer R ? R : unknown; 
type NewType = Person<() =>  number>  // T: () => number, R: number
```

​     

### ReturnType

- 함수를 넣으면 함수의 return타입을 추출해줌

```typescript
type RT = ReturnType<() => void>  // RT: void
```

