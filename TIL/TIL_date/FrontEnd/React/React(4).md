# React (4)

​    

## 1️⃣ Context API

- props 없이 state를 공유하는 방법

```jsx
// App.js
import Detail from './Detail.js'

export const StockContext = React.createContext();  // state 보관함 ✔️✔️ 

function App() {
  const [stock, setStock] = useState([10, 20, 30])
  
  return (
  	<StockContext.provider value={{ stock }}>  ✔️✔️ 
      <Detail />
    <StockContext.provider>
  )
}
```

```jsx
// Detail.js
import { useState, useEffect, useContext } from 'react';
import { StockContext } from './App.js';

export default function Detail() {
  const { stock } = useContext(StockContext)  ✔️✔️ 
  
  return (
  	<div>{stock}</div>
  )
}
```

- 단점 : state 변경시 쓸데없는 컴포넌트까지 전부 재렌더링됨

​    

---

## 2️⃣ Redux Toolkit

### 설치

```bash
$ npm install @reduxjs/toolkit react-redux
$ yarn add @reduxjs/toolkit react-redux
```

​    

### 세팅

```jsx
// store.js
import { configureStore } from '@reduxjs/toolkit'

export default configureStore({
  reducer: {}
})
```

```jsx
// index.js
import { Provider } from 'react-redux'
import store from './store.js'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>  ✔️✔️
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>  ✔️✔️
  </React.StrictMode>
); 
```

​    

### State 보관

1. `createSlice()`로 state 생성
2. `configureStore()`안에 생성한 state 등록

```js
// store.js
import { configureStore, createSlice } from '@reduxjs/toolkit'

let state이름 = createSlice({  // 전역에서 사용할 state 생성하는 함수
  name: '',  // state이름
  initialState: ''  // state 초기값
})

export default configureStore({  // 전역 state를 등록하는 함수
  reducer: {
    state이름: state이름.reducer
  }
})
```

​    

### State 활용

- `useSelector`함수 활용

```js
// store.js에서 생성한 모든 global state를 불러옴
useSelector((state) => {
  return state
})
```

```js
// 전역 state를 활용할 컴포넌트 파일
import { useSelector } from 'react-redux'  ✔️✔️

function GlobalStatePage() {
  const allGlobalState = useSelector((state) => state)  ✔️✔️ 
  console.log(allGlobalState)
  
  return ()
}
```

​    

### State 변경

#### 일반변수일때

1. store.js에 state를 변경하는 함수를 만들어 export

- `reducers: {}` 안에 함수를 작성해야함

```js
// store.js
let user = createSlice({
  name: 'user',
  initialState: 'kim',
  reducers: {  ✔️✔️
    changeName(state) {  ✔️✔️
      return 'yoonsik ' + state
    }
  }
}) 

export let { changeName } = user.actions  ✔️✔️
```

​    

2.  함수를 import후 dispatch() 키워드를 사용하여 변경

```jsx
import { useDispatch, useSelector } from 'react-redux'
import { changeName } from './store.js'

function ChangePage() {
  const dispatch = useDispatch();
  const changeName = () => { dispatch(changeName('shin')) }
  
  return (
  	<button onClick={changeName}>이름변경버튼</button>
  )
}
```

​    

#### array / object일때