# React (3)



## 1️⃣ 컴포넌트 Lifecycle

- 생성, 장착 (mount)
- 재렌더링, 업데이트 (update)
- 삭제, 제거 (unmount)

​    

### class 문법 Lifecycle hook 

```jsx
class Detail extends React.Component {
	componentDidMount() {}  // 컴포넌트가 로드되고 실행할 코드
	componentDidUpdate() {}  // 컴포넌트가 업데이트 되고나서 실행할 코드
	componentWillUnmount() {}  // 컴포넌트가 삭제되기전에 실행할 코드
}
```

​    

### useEffect

- useEffect안에 적은 코드는 html 랜더링이 완료된 후에 동작
- 오래 걸리는 반복연산, 서버에서 데이터 가져오는 작업, 타이머등 사용시 활용하면 좋음

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



#### 실행조건

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

## 2️⃣ axios

```bash
$ npm install axios
$ yarn add axios
```

```jsx
// GET 요청
import axios from 'axios'

function App() {
  const onClickAxios = async () => {
    const result = await axios({
      method: 'get',
      url: 'https://..',
    })
    console.log(result)
  }
  
  return (
  	<button onClick={onClickAxios}>ajax 요청</button>
  )
}
```

```jsx
// POST 요청
import axios from 'axios'

function App() {
  const onClickAxios = async () => {
    const result = await axios({
      method: 'post',
      url: 'https://..',
      data: { 서버로 보내고싶은 데이터 }
    })
    console.log(result)
  }
  
  return (
  	<button onClick={onClickAxios}>ajax 요청</button>
  )
}
```

​    

### 동시에 여러 ajax 요청 보내기

```jsx
Promise.all([
  axios.get('url1'), 
  axios.get('url2')
]).then(() => {
  
})
```

​    

### fetch

```js
fetch('url').then(res => {
  res.json().then((result) => {  // JSON >> object/array로 자동변환을 안해줘서 바꿔줘야함
    console.log(result)
  })
})
```





redux

```bash
$ npm install @reduxjs/toolkit react-redux
```



- store.js 파일 생성후 (src폴더안에)

```js
import { configureStore, createSlice } from '@reduxjs/toolkit'

let 변수 = createSlice({
  name: 'state이름',
  initialState: { 변수a: "", 변수b: "" },
  reducers: {
  	함수(state, action){  // 파라미터 : 기존 state
  		state.변수a = "수정값"
      state.변수b += action.payload
		},
    함수2(){
      return
    }
	}	
})

export let {함수, 함수2} = 변수.actions;  // 만든 함수 내보내기

let user = createSlice({
  name: 'user',
  initialState: 'shin'
})

export default configureStore({
  reducer: {
    작명(변수): 변수.reducer 
    user: user.reducer
  }
}) 
```



- index.js 

```js
import store from './store.js'

root.render(
  // <React.StrictMode>
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>
  // </React.StrictMode>
);
```



- 꺼내쓰기

```json
import { 함수 } from
import { useDispatch, useSelector } from "react-redux"

function a(){
  let 변수 = useSelector((state)=> { return state })  // redux의 store 가져옴
  let 변수 = useSelector((state)=> { return state.user })  // redux의 store에서 user만 가져옴
  let dispatch = useDispatch()  // store.js으로 요청을 보내주는 함수
  
  return(
  	<>
    	<button onClick={()=>{
    		dispatch(함수())
  		}}
    </>
  )
}
```

- state 변경하기

- state 수정해주는 함수만들기
- 원할 때 그 함수를 실행해달라고 store.js에 요청
- 만든 함수 export



store.js 파일분할하기

