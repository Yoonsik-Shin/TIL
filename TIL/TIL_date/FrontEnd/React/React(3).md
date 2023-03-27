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

​    

---

## 3️⃣ 전환 애니메이션

### Fade In

1. 애니메이션 동작 전/후 스타일을 담을 className만들기

```css
.start {
  opacity: 0;  /* 동작전 투명도 0 */
}
.end {
  opacity: 1;  /* 동작후 투명도 1 */
}
```

2. `transition`속성 추가

```css
.start {
  opacity: 0;
}
.end {
  opacity: 1;
  transition : opacity 0.5s;  /* 투명도 변화가 0.5초 동안 일어나도록 설정 */ ✔️✔️ 
}
```

3. 동작 후 className을 조작하여 전환효과 부여

```jsx
function TabContent(props) {
  const [fade, setFade] = useState('')
  
  useEffect(() => {
    let time = setTimeout(() => { setFade('end') }, 100)	
    
    return () => {
      clearTimeout(time)
      setFade('') 
    }
  }, [props])
  
  return (
  	<div className={`start ${fade}`}>
    </div>
  )
}
```

​    

---

## 4️⃣ IF문 작성패턴

### Component

```jsx
function Component() {
  if () {
    return <div>참일 때 보여줄 HTML</div>
  }
  return null
}
```

​    

### JSX

- 중첩사용도 가능

```jsx
function Component() {
  return (
    <div>
      {
        1 === 1  // 조건
        ? <p>참일 때 보여줄 HTMLL</p>  // 참
        : null  // 거짓
      }
    </div>
  )
} 
```

​    

### `&&` 

- 처음으로 만나는 Falsy값 반환
- 모두 Truthy라면 마지막 피연산자값 반환

```jsx
function Component() {
  return (
    <div>
       <!-- 모두 참이므로 마지막 피연산자값 반환 -->
      { 1 === 1 && <p>참일 때 보여줄 HTML</p> }
    </div>
  )
}
```

​     

### switch / case

```jsx
function Component2(){
  const user = 'seller';
  
  switch (user){
    case 'seller':
      return <h4>판매자 로그인</h4>
    case 'customer':
      return <h4>구매자 로그인</h4>
    default: 
      return <h4>로그인</h4>
  }
}
```

​    

### object / array 응용

```jsx
const TabUI = {
  info: <p>상품정보</p>,
  shipping: <p>배송정보</p>,
  refund: <p>환불정보</p>,
}

function Component() {
  const [state, setState] = '';
  
  return <div>{ TabUI[state] }</div>  ✔️✔️
}
```

​    

---

## 5️⃣ localStorage

```js
// 값 추가
localStorage.setItem('저장할 데이터명', '저장할 데이터값')

// 값 읽기
localStorage.getItem('읽어올 데이터명')

// 값 삭제
localStorage.removeItem('삭제할 데이터명')
```



> array / object 다루기

- JSON으로 변환후 저장 및 읽기

```js
// 값 추가
localStorage.setItem('obj', JSON.stringify({ name: 'shin' })) // obj: "{"name": "shin"}"

// 값 읽기
let obj = localStorage.getItem('obj')
obj = JSON.parse(obj)
```

​    

> 최근 본 상품

```jsx
useEffect(() => {
  let watched = localStorage.getItem('watched')
  watched = JSON.parse(watched)
  watched.push(product.id)
  
  // Set으로 중복제거한 후 다시 array로
  watched = new Set(watched)
  watched = Array.from(watched)
  localStorage.setItem('watched', JSON.stringify(watched))
}, [])
```

