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

> 자바스크립트 Destructuring

```javascript
let num = [1, 2, 3]

// 기본
let a = num[0]
let b = num[1]
let c = num[2]

// Destructuring
let [a, b, c] = [1, 2, 3]
```

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

> props drilling

- props가 자식에게 넘겨주는 단계가 두번 이상일 경우를 props drilling이 일어났다라고 함
- 과도하지 않으면 괜찮지만, 과도하면 가독성과 유지보수면에서 좋지 않음
- 이를 방지하기 위해서 global state를 활용함

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

   

---

## 6️⃣ 커스텀 hook

- 그냥 함수와의 차이점 : 함수안에 다른 use로 시작하는 요소의 여부에 따라 구분됨

​     

---

## 7️⃣ 기타

### map함수

1. array의 자료수만큼 내부코드 반복 실행

```javascript
[1, 2, 3].map(()=>{
  console.log('실행')
})

>> 실행
>> 실행
>> 실행
```

2. 파라미터 사용시 array의 값들 순서대로 받아옴

```javascript
[1, 2, 3].map( (a) => { 
  console.log(a)
})

>> 1
>> 2
>> 3
```

3. return문 내용을 array로 담아줌

```javascript
[1, 2, 3].map((a) => {
  return "123456";
});

>> (3) ['123456', '123456', '123456']
```



> 같은 html 반복 생성

- 동일한 HTML 코드가 반복될 시 `key`값으로 구분해줘야함
- index를 키로 사용하면 안됨, 아예 중복되지 않는 값을 key로 지정해줘야함

```jsx
let [test, setTest] = useState(['1', '2', '3'])

{
  test.map((el, idx) => {    // el: 값, idx: 인덱스
    return (
      <div key={중복되지않는값}>
        <h2>{ el }</h2>
        <h2>{ test[idx] }</h2>
        <p></p>
      </div>
    )
  })
}
```

​    

> Fragment

- 빈 <>에는 태그 속성을 사용할 수 없음
- 이때는 `<Fragment`> 태그를 사용해야함

```jsx
{
  arr.map((el, idx) => (
    <Fragment key={idx}>
    </Fragment>
  )
}
```

   

### filter함수

- 조건에 맞는 값만 골라내서 배열로 반환해줌

```js
const stock = [1, 2, 3, 4, 5, 6]
const filter = stock.filter(item => item >= 3)

// filter = [3, 4, 5]
```

​    

###  동적 UI

1. html, css로 미리 디자인 완성하기
2. UI의 현재 상태를 state로 저장

```jsx
function App (){
  let [modal, setModal] = useState(false);
  
  return (
    <button onClick={() => {
        setModal(!modal)
     };
  )
}
```

3. state에 따라 UI가 어떻게 보일지 작성

```jsx
{modal ? <Modal /> : null}
```

​    

> JSX 조건문 활용

```jsx
// 삼항 연산자
{
  조건식 ? 참일 때 실행할 코드 : 거짓일때 실행할 코드
}
```

​    

### input

> 사용자 입력값 저장

```jsx
function App() {
  const [inputVal, setInputVal] = useState('')
  const onChangeEvent = (e) => {
    setInputVal(e.target.value)
  }
  
  return (
  	<input onChange={onChangeEvent} />
  )
}
```

​    

#### 회원가입

```jsx
import { useState } from 'react'

export default function SignupStatePage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [emailError, setEmailError] = useState('')

  const onChangeEmail = (e) => { setEmail(e.target.value) }
  const onChangePassword = (e) => { setPassword(e.target.value) }
  const onClickSignup() => {
    if (!email.includes("@")) {
      setEmailError('이메일이 올바르지 않습니다.')
      return
    }
    // API 요청
    alert('회원가입을 축하합니다.')
  }

  return (
    <>
      이메일: <input type='text' onChange={onChangeEmail}/>
      <div>{emailError}</div>
      비밀번호: <input type='password' onChange={onChangePassword} />
      <button onClick={onClickSignup}>회원가입</button>
    </>
  )
}
```

