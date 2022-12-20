# React 정리 (3)



컴포넌트의 Lifecycle

- 장착 (mount)
- 업데이트 (update)
- 제거 (unmount)



컴포넌트에 갈고리 다는법

`useEffect()` : mount, update시 코드 실행

쓰는 이유

- html 랜더링이 완료된 후에 동작

```jsx
useEffect(() => {}, []) // [] : useEffect의 실행조건을 넣을 수 있는 곳
// 비어있으면 mount에만 실행됨

useEffect(() => {}, [count]) // count라는 state가 변할때만 실행됨

useEffect(() => {
  let a = setTimeout(() => { })
  
  return () => {
    clearTimeout(a)  // 타이머 제거해주는 함수
  }
})  // return문은 useEffect 동작전에 실행됨
```



1. 재렌더링마다 코드를 실행하고 싶으면

```jsx
useEffect(() => { })
```

2. mount시 1회 코드 실행하고 싶으면

```jsx
useEffect(() => { }, [])
```

3. useEffect 안의 코드 실행 전에 항상 실행

```jsx
useEffect(() => {
  return () => {}
})
```

4. unmount시 1회 코드 실행하고 싶으면

```jsx
useEffect(()=>{ 
  return ()=>{}
}, [])
```

5. state가 변경될 때만 실행

```jsx
useEffect(()=>{ 
  실행할코드
}, [stateName])
```







axios



동시에 ajax 요청 여러개하기

```jsx
Promise.all([ axios.get(''), axios.get('')] )
.then(() => {})
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

