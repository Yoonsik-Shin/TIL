# React (2)

​    

## 1️⃣ Class

- 기존 리액트에서는 Class를 사용



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

---

## 2️⃣ [React-BootStrap](https://react-bootstrap.netlify.app/getting-started/introduction/)

- 설치

```bash
$ npm install react-bootstrap bootstrap
$ yarn add react-bootstrap bootstrap
```

​    

- 컴포넌트 import 해오기

```js
// App.js
import { Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
```

​    

---

## 3️⃣ 이미지 넣기

### JSX

```jsx
import 작명 from '파일경로'
import bg from './img/img.png'

<div className="" style={{ backgroundImage : 'url(' + bg + ')'}}></div>
<img src={bg}></img>
```



### public 폴더

- build시 public 폴더에 있는 것들은 그대로 보존
- html에서 __public__폴더 이미지 사용할 땐 `/이미지경로` 로 사용

```jsx
<img src={process.env.PUBLIC_URL + '/img/testImg.png'}
```

​    

---

## 4️⃣ import / export

- `./` : 현재경로
- `export default` 키워드는 파일마다 오직 하나씩만 사용가능
- 변수, 함수, 자료형 모두 export 가능

```js
// data1.js (변수 하나)
let data = []

export default data;

// data2.js (변수 두개 이상)
let a = 10;
let b = 100;

export {a, b};
```

```js
// App.js
import 작명 from './data1.js';
import { a, b } from './data2.js';
```

​    

---

## 5️⃣ Router 

- react-router-dom 라이브러리 사용



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

## 6️⃣ styled-components

### 설치

```bash
$ npm install styled-components
$ yarn add styled-components
```

​    

### 사용법

```jsx
import styled from 'styled-componets'

let 작명 = styled.태그명`
	css작성;
	color: black;
	padding: 10px;
`
let Box = styled.div`
	padding: 20px;
	color: grey;
`

function Styled() {
  return (
  	<작명 />
    <Box></Box>
  )
}
```

​    

### 사용 이유

| 장점                                 | 단점                                                      |
| ------------------------------------ | --------------------------------------------------------- |
| 스타일이 다른 js파일로 오염되지 않음 | js파일이 매우 복잡해짐                                    |
| 페이지 로딩시간 단축                 | 다른 컴포넌트에서 중복스타일이 필요하면 css와 다를바 없음 |
| props로 컴포넌트 재활용 가능         |                                                           |
| 간단한 프로그래밍 가능               |                                                           |
| 기존스타일 복사가능                  |                                                           |

```jsx
import styled from 'styled-componets'

// 간단한 프로그래밍 가능 / props로 컴포넌트 재활용 가능
let Btn = styled.button`
	background: ${ props => props.bg }  ✔️✔️
	color: ${ props => props.bg == 'black' ? 'white' : 'black' };
`

// 기존스타일 복사가능
let NewBtn = styled.button(Btn)`
` 
```

​    

> ❗다른 js파일 오염 방지하려면 `컴포넌트.module.css`로 작명후 import 해서 사용

```jsx
// 컴포넌트.module.css
import styled from 'styled-componets'

export let Btn = styled.button`
	background: ${ props => props.bg }
	color: ${ props =? props.bg == 'black' ? 'white' : 'black' };
`
```

```jsx
import { Btn } from './컴포넌트.module.css'

function TestPage() {
  return (
  	<Btn>styled-component로 만든 버튼</Btn>
  )
}
```
