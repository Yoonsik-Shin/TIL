# React (2)

​    

## 1️⃣ Router 

- `react-router-dom` 라이브러리 사용

​    

### 설치 및 기본 세팅

```bash
$ npm install react-router-dom@6
$ yarn add react-router-dom@6
```

```js
// index.js
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
	<React.StrictMode>
  	<BrowserRouter>  // 새로 입력한 부분
    	<App />
    </BrowserRouter>  // 새로 입력한 부분
	</React.StrictMode>
)
```



### 페이지 나누기  (Routes, Route)

- 페이지도 컴포넌트로 만들면 좋음

```jsx
// App.js
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
    	<Route path="/url경로" element={ <보여줄 컴포넌트 /> } />
      <Route path="/" element={ <div>메인페이지에서 보여줄거</div> } /> 
      <Route path="/detail" element={ <div>상세페이지임</div> } />
    </Routes>
  )
}
```

​    

### 상세페이지 만들기  (useParams)

- 비슷한 페이지가 여러개 필요할때 url 파라미터 사용 (`:`)

```jsx
<Route path="/detail/:id" element={ <Detail shoes={shoes} /> }/>
```

```jsx
import { useParams } from 'react-router-dom'

function Detail() {
  let { id } = useParams()  ✔️✔️
  
  return ()
}
```

​    

> URL파라미터는 여러개 사용가능 

```jsx
<Route path="/detail/:id/more/:pk"></Route>
```

​    

### 페이지 이동 (Link, useNavigate)

1. Link

 ```jsx
import { Link } from "react-router-dom";

function pageLink() {
  return (
  	<Link to="/">홈</Link>
		<Link to="/detail">상세페이지</Link>
  )
}
 ```

​    

2. useNavigate

```jsx
import { useNavigate } from 'react-router-dom'

function pageNav() {
  let navigate = useNavigate()
  const onClickNav = () => { navigate('/') }  // 홈 페이지로 이동
  
  return (
  	<button onClick={onClickNav}>이동</button>
  )
}
```

> navigate에 숫자를 넣으면 앞으로가기, 뒤로가기 가능

```jsx
navigate(-1)  // 뒤로 한번 가기
navigate(2)   // 앞으로 두번 가기
```

​    

### nested routes (Outlet)

- 여러 유사한 페이지가 필요할 때 사용

```jsx
<Route path="/about" element={ <About/> } >  
  <Route path="member" element={ <div>멤버</div> } /> <!-- /about/member -->
  <Route path="location" element={ <div>위치</div> } /> <!-- /about/location -->
</Route>
```

- nested router안 element 위치 지정 (Outlet)

```jsx
function About(){
  return (
    <div>
      <h4>about페이지</h4>
      <Outlet></Outlet>  ✔️✔️ <!-- element의 요소를 보여줌 -->
    </div>
  )
}
```

​    

### 404 Page

```jsx
<Route path="*" element={ <404페이지 /> } />
```

​    

---

## 2️⃣ 컴포넌트 Lifecycle

- 생성, 장착 (mount)
- 재렌더링, 업데이트 (update)
- 삭제, 제거 (unmount)

​    

### useEffect

- useEffect안의 코드는 __html 랜더링이 완료된 후에 동작__
- 오래 걸리는 반복연산, 서버에서 데이터 가져오는 작업, 타이머등 사용시 활용하면 좋음
- useEffect안에서 setState의 사용은 지양해야함
- 불필요하게 리렌더링되거나 무한루프를 일으킬 수 있음

```jsx
import { useState, useEffect } from 'react';

function Detail() {
  useEffect(() => {
    // 컴포넌트 로드 and 업데이트시 실행되는 부분
    // html 랜더링이 완료된 후에 동작
  })
  
  return ()
}
```

​    

### 의존성배열

- 의존성 배열 (`[]`) 에 따라 렌더방식이 달라짐

​    

1. 재렌더링(update)마다 코드를 실행하고 싶으면

```jsx
useEffect(() => {
  // 실행할코드
})
```

2. 생성(mount)시 1회 코드 실행하고 싶으면

```jsx
useEffect(() => {
  // 실행할코드
}, [])
```

3. useEffect 안의 코드 실행 전에 항상 실행

> clean up function : `return () => {}`

```jsx
useEffect(() => {
  // 다음에 실행할코드
  return () => {
    // 먼저 실행할코드
  }
})
```

4. 제거(unmount)시 1회 코드 실행하고 싶으면

```jsx
useEffect(() => { 
  return () => {
    // 실행할코드
  }
}, [])
```

5. state가 변경될 때만 실행

```jsx
useEffect(() => { 
  실행할코드
}, [stateName])
```

​    

---

## 3️⃣ 커스텀 hook

- 그냥 함수와의 차이점 : 함수안에 다른 use로 시작하는 요소의 여부에 따라 구분됨

​    

---

## 4️⃣ Class

- 기존 리액트에서는 Class를 사용

​    

### 사용법

1. class명으로 컴포넌트명 작명
2. `constructor`, `super`, `render` 함수 넣기 (기본 템플릿)
3. `render`에 `jsx`값 사용

```jsx
class Modal extends React.Component {
  constructor() {
    super()
  }
  
  render() {
    return (
    	<div></div>
    )
  }
}
```

​    

### State

- state 설정시 `this.state = {}` 활용
- state 변경시 `this.setState({ 변경할state키 : 변경할값 })`
- props 사용시 `constructor(props)`, `super(props)`

```jsx
class TComponent extends React.Component { 
	constructor(props) {
    super(props);
    this.state = {  // 이 안에 state로 지정할 값들 나열
      name: 'shin',
      age: 27,
    }
  }
  
  // class내 함수
  onClickCountUp = () => {
    this.setState((prev) => {
      count: prev.count + 1
    })
  }
  
  render() {
    return (
      <>
        <div>{this.state.name}</div>
        <div>{this.state.age}</div>
      	<button onClick={() => { this.setState({ age: 28 }) }}>버튼</button> ✔️✔️
      	<button onClick={this.onClickCountUp}>카운트올리기</button> ✔️✔️
      	<div>{this.props.작명}</div>
      </>
    )
  }
}
```

​    

### class 문법 Lifecycle hook 

```jsx
class Detail extends React.Component {
	componentDidMount() {}  // 컴포넌트가 로드되고 실행할 코드
	componentDidUpdate() {}  // 컴포넌트가 업데이트 되고나서 실행할 코드
	componentWillUnmount() {}  // 컴포넌트가 삭제되기전에 실행할 코드
}
```
