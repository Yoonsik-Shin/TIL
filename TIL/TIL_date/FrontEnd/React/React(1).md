# React (1)

​     

## 1️⃣ React 

### 사용 이유

- 싱글페이지 어플리케이션 (SPA: Single Page Application)을 만들고 싶을 때 사용
- html 재사용 편리
- React Native에도 활용가능

​    

### 설치법

1. node.js 설치
2. 프로젝트 폴더 만들기
3. 터미널에서 명령어 입력 (`CRA` : Create React App 라이브러리 사용) 

```bash
$ npx create-react-app <앱 이름>
```

> vite 이용 react 세팅

```bash
$ npm create vite@latest
```



> (윈도우) 설치 오류시

```bash
Set-ExecutionPolicy Unrestricted
```

​    

----

## 2️⃣ 보일러 플레이트

- 초기 폴더구조

​    

### node_modules

- 라이브러리 / 프레임워크 보관함

### public 

- static 파일 보관함
- html, 이미지 파일등을 임시로 저장하고 싶을때

### src

- 소스코드 보관함
- 직접 코드를 작성하는 곳
- App.js : 메인페이지

### package.json

- 프로젝트 정보

​     

---

## 2️⃣ JSX

- 자바스크립트 파일에서 HTML언어와 유사한 기능을 하는 언어

​     

### HTML과 다른점

1. 클래스 [`className`]

```jsx
<div className="클래스이름"></div>
```

2. 변수 (데이터 바인딩) [`{ 변수 }`]

```jsx
let 변수명;
<h4>{ 변수명 }</h4>
```

3. 스타일 [`style={{ attribute1: value2, attribute2: value2 }}`]

```jsx
<h1 style= { {스타일명:'값'} }></h1>
<h1 style= { {color:'red', fontSize: '16px'} }></h1>
```

4. return () 안에는 병렬로 태그 2개이상 기입 금지

```jsx
return (
	<div>1번</div>
	<div>2번</div>  // 불가능
)
```

```jsx
return (
	<div>  // 무조건 하나에 들어있어야함 (컨테이너 같은 느낌)
  	<div>1번</div>
		<div>2번</div>  // 불가능
  </div>
)
```

5. 변수명 카멜케이스 사용

```jsx
<div onClick={실행할함수}></div>
```

​    

---

## 3️⃣ State

- 자료 잠깐 보관하기
- 컴포넌트 전용 변수
- 변수는 자동으로 내용 변경시 html에 재렌더링 안되지만, state는 재렌더링이 자동으로 html에 반영
- 자주 변경될거같은 html 부분은 state로 만들기

```javascript
import { useState } from "react";

let [변수, set변수] = useState('보관할 자료')
let [글제목, set글제목] = useState('남자 코트 추천')
```

- `변수` : state에 보관했던 자료
- `set변수` : state변경을 도와주는 함수

​    

### State 수정

- array, object를 다룰 때 원본은 보존하는게 좋음
- 비동기적으로 동작, 코드를 끝까지 읽고 한번에 바꿔서 렌더링
- array / object를 담은 변수엔 메모리값만 저장되어있음 (__reference data type__)

```jsx
let a = [1, 3, 5];
let b = a;
b[0] == 300;
console.log(a === b) // true
```

- `기존 state == 신규 state`의 경우 변경 안됨

- ❗state가 array / object이면 독립적인 카피본(__shallow copy__)을 만들어 수정해야함

```jsx
const [objState, setObjState] = useState({ default: 'value' })
const [arrState, setArrState] = useState([1, 2, 3])

// object
<button onClick={() => {
	let copy = { ...objState };   // 메모리값을 바꿔줌
  copy[default] = '바꿀값';
  setObjState(copy);
}};

// array
<button onClick={() => {
	let copy = [ ...arrState ];   // 메모리값을 바꿔줌
  copy[default] = '바꿀값';
  setArrState(copy);
}};
```

​    

### PrevState

- automatic batch에 의해 state 변경함수들이 연달아 여러개 처리되야하면 다 처리 후 __마지막 한 번만 재렌더링됨__
- 그 전에 state의 값이 변하기 전에 저장해놓는 임시 저장공간
- 임시 저장공간이 비워져있다면 state의 값을 가져와 임시공간에 저장
- 보통 `prev` 매개변수를 쓰지만 이름은 의미없음

```js
// 예시1
import { useState } from 'react'

export default function CounterStatePage() {
  const [count, setCount] = useState(0)
  const onClickCountUp = () => {  // 임시저장공간 = 0
    setCount((prev) => prev + 1)  // 임시저장공간 = 1
    setCount((prev) => prev + 1)  // 임시저장공간 = 2
    setCount((prev) => prev + 1)	// 임시저장공간 = 3
  }  // count = 임시저장공간 = 3
}

// 예시2
const [isOpen, setIsOpen] = useState(false);
const onToggleModal = () => {
  setIsOpen((prev) => !prev)
}
```

> automatic batch : React (4) 문서 참고

​    

> 리렌더링 되는 상황

1. 새로운 props가 들어올 때
2. 부모 컴포넌트가 렌더링될 때
3. 강제 업데이트가 실행될 때
4. state가 변경될 때

​    

> warning 메시지 지우기

```jsx
/* eslint-disable */
```

​    

---

## 4️⃣ Component

> fragment : 의미없는 `<div>` 대신 `<></>` 사용가능 

```jsx
// 1번 방법
function Modal(){    // 대문자 작명
	return(
  		<div className="modal">
      	<h4>제목</h4>
      	<p>날짜</p>
      	<p>상세내용</p>
    	</div>
  )
}

// 2번 방법
const Modal = () => {
  return (
  	<>
    </>
  )
}
```

- 다른 함수 밖에 작성해야함

1. function 만들기
2. return ( ) 안에 html 담기
3. <컴포넌트></컴포넌트> or <컴포넌트 />

```jsx
<Modal></Modal>
<Modal />  // 넣을 값 없으면 사용
```

​    

> 컴포넌트로 만들기 좋은 요소들

1. 반복적인 html 축약시
2. 큰 페이지
3. 자주 변경되는 요소들

​    

> 컴포넌트 단점

- state 가져다 쓸 때 문제 발생
- 다른 함수에 있는 변수들을 마음대로 가져다 사용할 수 없음

​    

---

## 5️⃣ props

- 부모 component에서 자식 component로 state 전송하기
- 자식에서 부모, 형제끼리는 불가능 ❗
- 단방향 전달 방식
- 컴포넌트들 중 최고로 높은 부모에게 만들어놔야함

```jsx
const 부모컴포넌트 = () => {
  const [pass, setPass] = useState('')
  
  return (
    // 보통 작명은 '{}'안에 값과 동일하게 함
  	<자식컴포넌트 작명={state값/함수/일반변수} 작명2="일반문자"/>  
    <자식컴포넌트 pass={pass} setPass={setPass} />
  )
}

const 자식컴포넌트 = (props) => {
  return (
    <>
    	<p>{props.작명}</p>
    	<p>{props.pass}</p>
    </>
  )
}
```

​    

### props children

- 컴포넌트 태그사이에 들어가는 요소들은 자동으로 `prop[children] `에 들어감

```jsx
<Container isEdit={true}>
	<div>1</div>  ✔️✔️  <!-- props의 children에 들어감 -->
  <div>2</div>  ✔️✔️	<!-- props의 children에 들어감 -->
  <div>3</div>  ✔️✔️	<!-- props의 children에 들어감 -->
</Container>
```

```jsx
export default function Page(props) {
  return (
  	{props.childern}  // <div>1</div>; <div>2</div>; <div>3</div>;
  )
}
```

​    

### props drilling

- props가 자식에게 넘겨주는 단계가 두번 이상일 경우를 props drilling이 일어났다라고 함
- 과도하지 않으면 괜찮지만, 과도하면 가독성과 유지보수면에서 좋지 않음
- 이를 방지하기 위해서 global state를 활용함

​    

---

## 6️⃣ 컴포넌트 재사용

- 수정 / 등록 페이지는 몇몇 요소를 제외하면 동일한 부분이 많아 컴포넌트 재활용을 할 수 있음
- __props__와 __삼항연산자__ 활용

```jsx
// 등록페이지
import BoardComponent from '../../src/components/units/board/..'

export default function BoardNewPage() {
  return <BoardComponent isEdit={false}>
}
```

```jsx
// 수정페이지
import BoardComponent from '../../src/components/units/board/..'

export default function BoardEditPage() {
  return <BoardComponent isEdit={true}
}
```

```jsx
export default function BoardComponent(props) {
  return (
    // 삼항연산자 활용
  	<h1>{props.isEdit ? "수정" : "등록"}</h1>
  	<button onClick={props.isEdit > props.onClickUpdate : props.onClickCreate}>
      {props.isEdit ? "수정" : "등록"}하기
    </button>
  )
}
```

​        

### defaultValue

- input태그의 속성
- 초기값 설정

```jsx
<input 
  type="text" 
  onChange={props.onChangeTitle} 
  defaultValue={props.data?.fetchBoard.title}  ✔️✔️
/>
```

​    

### 수정한 값만 요청보내기

- 문제점 : 전송 객체가 state의 초기값으로 계속 초기화되어 defaultValue 속성을 부여해도 빈 값이 들어감 
- 해결책 : 변경된 객체만 백엔드에 전송해서 수정하기 (PUT요청)

```jsx
export default function DefaultValue(props) {
  const router = useRouter()
  const [value1, setValue1] = useState('')
	const [value2, setValue2] = useState('')
  
  const onClickSumbit = async () => {
  	const variables = { id: Number(router.query.mynumber) }
    // 변경한 값만 객체에 값 추가
    if (value1) { variables[value1] = value1 }
    if (value2) { variables[value2] = value2 }
	}
  
  // 변경된 객체로 API요청
}

```
