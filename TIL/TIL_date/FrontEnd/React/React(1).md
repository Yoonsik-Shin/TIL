# React 정리 (1)



## 왜 사용하는가

- 싱글페이지 어플리케이션 (Single Page Application)을 만들고 싶을 때 사용
- html 재사용 편리
- React Native에도 활용가능



## 설치법

1. node.js 설치
2. 프로젝트 폴더 만들기
3. 터미널에서 명령어 입력

```bash
npx create-react app <앱 이름>
```

> (윈도우) 설치 오류시

```bash
Set-ExecutionPolicy Unrestricted
```



src파일 > App.js

미리보기 : npm start

Create React App 라이브러리 사용



## React 파일정리

node_modules

- 라이브러리 코드 보관함
- 따로 수정 x

public 

- static 파일 보관함
- html, 이미지 파일등을 임시로 저장하고 싶을때

src

- 소스코드 보관함
- 직접 코드를 작성하는 곳
- App.js : 메인페이지

package.json

- 프로젝트 정보
- 따로 수정 x

​    

---

## JSX

- 자바스크립트 파일에서 HTML언어와 유사한 기능을 하는 언어

​     

### HTML과 다른점

1. 클래스

```jsx
<div className="클래스이름"></div>
```

2. 변수 (데이터 바인딩)

```jsx
let 변수명;
<h4>{ 변수명 }</h4>
```

3. 스타일

```jsx
<h1 style= { {스타일명:'값'} }></h1>
<h1 style= { {color:'red', fontSize: '16px'} }></h1>
```

> ❗ 변수명 카멜케이스 사용

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

​    

---

## State

- 자료 잠깐 보관하기
- 컴포넌트 전용 변수
- 변수는 자동으로 내용 변경시 html에 재렌더링 안됨
- state는 재렌더링이 자동으로 html에 반영
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
- array/object를 담은 변수엔 메모리값만 저장되어있음 (reference data type)

```jsx
let a = [1, 3, 5];
let b = a;
b[0] == 300;
console.log(a === b) // true
```

- `기존 state == 신규 state`의 경우 변경 안함

- state가 array나 object이면 독립적인 카피본(shallow copy)을 만들어 수정해야함

```jsx
<button onClick={ () => {
    let copy = [...state_1];   // 메모리값을 바꿔줌
    copy[바꿀 인덱스] = "바꿀값";
    state_2(copy);
  }};
```

​    

> warning 메시지 지우기

```jsx
/* eslint-disable */
```

​    

---

## Component (컴포넌트)

```jsx
// 1번 방법
function Modal(){    // 대문자 작명
  return(
    <>               // 의미없는 `<div>` 대신 `<></>` 사용가능 
  		<div className="modal">
      	<h4>제목</h4>
      	<p>날짜</p>
      	<p>상세내용</p>
    	</div>
    </>
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
3. <함수명></함수명>

```jsx
<Modal></Modal>
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

## 동적 UI 만들기

1. html, css로 미리 디자인 완성하기
2. UI의 현재 상태를 state로 저장

```jsx
function App (){
  
  let [modal, setModal] = useState(false);
  
  return (
    <button onClick={ () => {setModal(!modal)};
  )
}
```

3. state에 따라 UI가 어떻게 보일지 작성

```jsx
{modal === true ? <Modal /> : null}
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

---

## map

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
[1, 2, 3].map(function (a) {
  return "123456";
});

>> (3) ['123456', '123456', '123456']
```



> 같은 html 반복 생성

```jsx
let [a, b] = useState('')

{
  a.map(function(param, i){    // i : 인덱스
    return (
      <div key={i}>
        <h2>{ param }</h2>
        <h2>{ a[i] }</h2>
        <p></p>
      </div>
    )
  })
}
```

​    

---

## props

- 부모 component에서 자식 component로 state 전송하기
- 자식에서 부모, 형제끼리는 불가능 ❗

```jsx
<자식컴포넌트 작명={state이름}/>

function 자식컴포넌트(props){
  return (
    <p>props.작명</p>
  )
}
```
