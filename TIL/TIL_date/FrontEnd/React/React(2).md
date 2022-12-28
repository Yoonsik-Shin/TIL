# React 정리 (2)

​    

## [React-BootStrap](https://react-bootstrap.netlify.app/getting-started/introduction/)

- 시작하기

```bash
$ npm install react-bootstrap bootstrap
```

- 컴포넌트 import 해오기

```js
import { Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
```



- jsx 상에서 이미지 넣기

```jsx
import 작명 from '파일경로'
import bg from './img/img.png'

<div className="" style={{ backgroundImage : 'url(' + bg + ')'}}></div>
```



- html에서 __public__폴더 이미지 사용할 땐 `/img경로` 로 사용

```jsx
<img src={process.env.PUBLIC_URL + 'img/testImg.png'}
```



- export / import 하기

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





- 리액트 라우터

```ba
npm install react-router-dom@6
```

```js
// index.js
root.render(
	<React.StrictMode>
        <BrowserRouter>  // 새로 입력한 부분
            <App />
        </BrowserRouter>  // 새로 입력한 부분
    </React.StrictMode>,
)
```



> 외부 라이브러리 사용법

```js
import { Routes, Route, Link, useNavigate, Outlet } from "react-router-dom";
```

라우터로 페이지 나누는 법

페이지도 컴포넌트로 만들면 좋음

Nested Routes

여러 유사한 페이지가 필요할 때 사용

nested routes의 element를 보여주는 곳은 <Outlet>

페이지 여러개 만들고 싶을때 : `:URL 파라미터`

- URL파라미터는 여러개 사용가능 

```jsx
<Route path="/detail/:id/more/:pk"></Route>
```

유저가 URL파라미터에 입력한거 가져오기 : `useParams()`





외부라이브러리

- styled-components
- 장점
  - 스타일이 다른 js파일로 오염되지 않음
  - 페이지 로딩시간 단축
- props로 컴포넌트 재활용 가능
  - 간단한 프로그래밍 가능
  - 기존스타일 복사가능

```jsx
import styled from 'styled-componets'

let Btn = styled.button`
	background: ${ props => props.bg }
	color: ${ props =? props.bg == 'black' ? 'white' : 'black' };
` // 간단한 프로그래밍 가능

let NewBtn = styled.button(Btn)`
	
`  // 기존스타일 복사가능
```

- 단점
  - js파일이 매우 복잡해짐
  - 다른 컴포넌트에서 중복스타일이 필요하면 css와 다를바 없음



- 다른 js파일 오염 방지하려면
  - `컴포넌트.module.css`로 작명

 
