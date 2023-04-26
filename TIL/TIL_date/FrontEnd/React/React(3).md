# React (3)



## 1️⃣ CSS-IN-JS

- CSS를 JS 상수에 저장하여 사용하는 방법

```js
// styles/emotion.js
import styled from '@emotion/styled'

export const Box = styled.div`
	width: 100px;
	height: 200px;
`
```

- HTML 태그처럼 사용할 수 있음
- 태그에 의미를 부여할 수 있어 결과물을 예상할 수 있음
- 코드의 길이가 짧아져 읽기 쉬워지고, 코드 재사용성이 좋아짐

```jsx
// 화면페이지
import { Box } from '../../styles/emotion.js'

export default function EmotionPage() {
  
  return(
  	// 너비 100px, 높이 200px을 가진 div 태그
		<Box>박스</Box>  
  )
}
```

- 라이브러리로는 `emotion`과 `styled-components`를 많이 씀

```bash
$ yarn add @emotion/react
$ yarn add @emotion/styled
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

​    

### styled-components

- 설치

```bash
$ npm install styled-components
$ yarn add styled-components
```

​    

- 사용법

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

### emotion의 props

- emotion으로 만들어진 태그에도 props 전달가능
- 특정 태그에 동작이 행해지면, props를 활용하여 css 변경 가능

```jsx
import * as S from './Board.styles.js'

export default function BoardUI(props) {
  return (
  	<>
    	<BlackButton
      	color="black"  ✔️✔️
        fontSize="16"
        
      >
    		버튼
    	</BlackButton>
    </>
  )
}
```

```js
export const BlackButton = styled.button`
	background: ${props => props.color}; 
	font-size: ${props => props.fontSize + "px"};
`
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

##  3️⃣ 동적 UI

### 기본원리

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
  if () { return <div>참일 때 보여줄 HTML</div> }
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
      {1 === 1  // 조건
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
  const [state, setState] = useState('');
  
  return <div>{ TabUI[state] }</div>  ✔️✔️
}
```

​    

## 5️⃣ 기타

### 이미지 넣기

```jsx
import 작명 from '파일경로'
import bg from './img/img.png'

<div className="" style={{ backgroundImage : 'url(' + bg + ')'}}></div>
<img src={bg}></img>
```

​      

> public 폴더

- build시 public 폴더에 있는 것들은 그대로 보존
- html에서 __public__폴더 이미지 사용할 땐 `/이미지경로` 로 사용

```jsx
<img src={process.env.PUBLIC_URL + '/img/testImg.png'}
```

​    

### map

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

   

### filter

- 조건에 맞는 값만 골라내서 배열로 반환해줌

```js
const stock = [1, 2, 3, 4, 5, 6]
const filter = stock.filter(item => item >= 3)

// filter = [3, 4, 5]
```

​    

###  axios

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

### input

- 사용자 입력값 저장

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

- 가장 일반적인 회원가입 구현

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

