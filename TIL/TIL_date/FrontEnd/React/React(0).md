# React (0)

​    

## 1️⃣ 이벤트루프

- 자바스크립트는 __싱글 스레드__ / __논블록킹__ 방식을 가짐
- 한 번에 하나의 태스크만 처리 가능
- 이러한 특성을 가졌지만 실제 브라우저 사용시 태스크가 동시에 처리되는 것 같이 느낌 (동시성)
- 동시성(concurrency)을 지원하기 위해 이벤트루프 방식 활용

​    

---

## 2️⃣ 동기 vs 비동기

### 비동기

- 서버에 요청(등록, 수정, 삭제 등)이 저장될 때까지 기다리지 않고 다른 작업을 진행
- 요청들 사이에 서로 기다려 줄 필요가 없을 경우, 여러 가지 요청을 동시에 처리해 줄 때에 사용
- 외부 라이브러리들은 대부분 비동기 방식으로 작동함

```js
// axios
const FetchDate = () => {
  const result = axios({
    method: '',
    url: '',
  })  // result = Promise 객체로 반환
}
```

​    

> Promise 객체

- js에서 비동기 처리에 사용되는 객체
- 서버에서 데이터를 받아오기 전에 화면에 표시하려고 하면 발생하는 문제를 해결하기 위해 사용
- 3가지 상태
  1. Pending (대기) : 비동기 처리 로직이 아직 완료되지 않음
  2. Fulfilled (이행) : 비동기 처리가 완료되어 프로미스가 결과값을 반환해준 상태
  3. Rejected (실패) : 비동기 처리가 실패하거나 오류가 발생

​    

### 동기

- 서버의 작업이 끝날 때까지 기다린 후에 다음 작업을 실행
- JS는 기본적으로 동기처리 방식을 사용

```js
// axios
const FetchDate = async () => {
  const result = await axios({
    method: '',
    url: '',
  }) // result = { 요청한 데이터 값 }
}
```

​    

### 비동기 발전과정

1. callback 형식 [`XMLHttpRequest`활용]

```jsx
const Callback = () => {
  const firstReq = new XMLHttpRequest()
  firstReq.open('get', 'URL주소')
  firstReq.send()
  firstReq.addEventListener('load', (res) => {
    const num = res.target.response.???  // 다음 API 요청에 사용할 숫자
    
    const secondReq = new XMLHttpRequest()
    secondReq.open('get', `URL주소/${num}`)
    secondReq.send()
    secondReq.addEventListener('load', (res) => {
      const id = res.target.response.???
      
      const thirdReq = new XMLHttpRequest()
      thirdReq.open('get', `URL주소/${id}`)
      thirdReq.send()
      thirdReq.addEventListener('load', (res) => {
      	const finalResult = res.target.response.???
      }
    }
  }) 
}
```

> 문제점 : 콜백함수가 중첩될수록 점점 함수의 깊이가 깊어짐 (콜백지옥)

​    

2. Promise 형식 [`new Promise`활용]

```jsx
new Promise((resolve, reject) => {
  try {
    const result = 시간이 걸리는 함수실행 (결과값: "취업")
    resolve(result)
  } catch(error) {
    reject("요청에 실패했습니다.") 
  }
}).then((res) => {
  console.log(res)  // 취업
}).catch((err) => {
  console.log(err)  // 요청에 실패했습니다.
})
```

- 개선된 Promise 형식 [`axios, fetch`활용]

```jsx
const PromiseTest = () => {
  axios.get('url1')
  	.then((res) => {
    	return axios.get('url2')
  	})
  	.then((res) => {
    	return axios.get('url3')
    .then((res) => {
    	console.log(res)     
    })
  })
}
```

> 문제점 : 실행순서를 예측하기 어려움

​    

4. async-await 형식

```jsx
const AsyncAwait = async () => {
  const result1 = await axios.get('url1')
  const result2 = await axios.get('url1')
  const result3 = await axios.get('url1')
} 
```

​    

> axios, fetch등을 기다리는 방법

1. `.then()` 활용
2. `async/await` 활용 



### 커스텀 AJAX 만들기

```jsx
const myAjax = {
  get: (url) => {
    return new Promise((resolve, reject) => {
      const req = new XMLHttpRequest()
      req.open('get', url)
      req.send()
      req.addEventListener('load', (res) => { resolve(res.target.response) })
    })
  },
  post: () => {}
}
  
const onClickAjax = async () => {
  const result = await myAjax.get('url')
}
```



---

## 3️⃣ 이벤트 전파

### 이벤트 버블링

- 특정화면요소에 이벤트가 발생했을 때, 이벤트가 더 상위 요소들에게도 영향을 주는 특성
- 자식에서 부모로 이벤트 전파

```html
<!-- p태그 클릭시 `p > div > form` 순으로 총 3개의 경고창 발생 -->
<form onclick="alert(form)">
	<div onclick="alert(div)">
		<p onclick="alert(p)">P</p>
	</div>
</form>
```

```jsx
// div태그(자식)를 클릭하면 S.Wrapper태그(부로)로 이벤트 전파(버블링) 됨
export default function CommentUI(props) {
	const onClickEvent = (e) => { alert(e.currentTarget) }
  
  return (
  	{props.data.map((el) => (
  		<S.Wrapper id={el._id} onClick={onClickEvent}>
      	<div>A</div>
      	<div>B</div>
      	<div>C</div>
    	</S.Wrapper>
  	))}
  )
}
```

- ` event.target` : 이벤트가 발생한 주체 (클릭된 주체 : `div`)
- `event.currentTarget` : 이벤트 버블링에 의해 이벤트가 발생한 주체



> event.stopPropagation

- 이벤트 버블링을 막아줌

```jsx
const onClickTop = (e) => {}
const onClickBottom = (e) => {
  event.stopPropagation()  // onClickTop까지 이벤트 버블링되는 것을 막아줌
}

<div onClick={onClickTop}>
	<div onClick={onClickBottom}>
    <div>여기를 클릭</div>
  </div>
</div>
```

​        

### 이벤트 캡처링

- 상위요소에서 하위요소로 이벤트가 전파되는 경우
- 부모에서 자식으로 이벤트 전파

​     

----

## 4️⃣ 복사

- 원시타입(Primitive)의 경우 변수에 값을 할당하면 `값 자체`가 저장됨
- 객체타입의 경우 값 자체가 아닌 `주소` 가 저장됨
- 객체타입에는 복사라는 개념이 없음
- 원본과 같은 값을 가진 객체를 새로 만드는 방식으로 사용해야함

​    

### 얕은 복사 (Shallow-copy)

- 스프레드 연산자(`...`)를 활용한 복사
- depth 1의 깊이를 가진 데이터는 복사가능하지만, depth 2부터는 복사하지 못함

```js
let obj = {
  aaa = "aaa",
  bbb = "bbb"
  ccc = {  
  	ddd: "ddd",  // depth 2 부터는 복사 안됨
  	eee: "eee"
	}
}

let newObj = {
  ...obj
}
```



### 깊은 복사 ( Deep-copy)

- depth 2 이상의 깊이를 가진 객체 복사시에 사용
- `JSON.stringify`와 `JSON.parse` 메소드를 사용
- 객체타입을 문자열로 변환 후, 다시 그 문자열을 객체로 바꿔 새로운 변수에 담음
- 깊은 복사를 도와주는 라이브러리인 [Lodash](https://www.npmjs.com/package/lodash)의 `_cloneDeep()` 메서드를 많이 씀

```js
let obj = {
  aaa = "aaa",
  bbb = "bbb"
  ccc = {  
  	ddd: "ddd",
  	eee: "eee"
	}
}

let newObj = JSON.parse(JSON.stringify(obj))  ✔️✔️
let newLodashObj = _.cloneDeep(newObj)  ✔️✔️
```

   

---

## 5️⃣ 구조분해할당 (비구조화할당)

### 배열

```js
const people = ['shin', 'yoon', 'sik']

// 기존방식
const person1 = people[0]
const person2 = people[1]
const person3 = people[2]

// 구조분해할당 활용
const [person1, person2, person3] = people
```

- 배열의 구조분해할당은 대괄호`[]`를 사용
- 변수명은 마음대로 설정가능
- 인덱스의 순서대로 값이 할당됨으로 순서가 중요함

​    

### 객체

```js
const person = {
  name: 'yoonsik',
  age: 27,
  address: 'seoul'
}

// 기존방식
const name = person.name
const age = person.age
const address = person.address

// 구조분해할당 활용
const { name, age, address } = person

// rest 파라미터 활용
const { name, ...rest } = person
console.log(rest)  // rest = { age: 27, address: 'seoul' } 
```

- 객체의 구조분해할당은 중괄화`{}`를 사용
- 객체의 key값을 변수명으로 사용해야함
- 할당 순서는 중요하지 않음
- 사용하지 않을 key값은 제외하고 할당 받을 수 있음

​    

---

## 6️⃣ import / export

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

## 7️⃣ export VS export default

### export

- 중괄호를 사용하여 import 
- 한 컴포넌트내에서 여러개를 내보낼 때 사용
- export한 이름 그대로 불러와야함
- 한번에 묶어서 import시에는 `import * as 별명 from '경로'`

```js
// export 방법1 - A.js
export const value1 = 'value1';
export const value2 = 'value2';

// export 방법2 - A.js
const value1 = 'value1';
const value2 = 'value2';

export { value1, value2 }

// import 방법1 - B.js
import { value1, value2 } from './A.js'

// import 방법2 - B.js
import * as 작명 from './A.js'
console.log(작명.value1)
console.log(작명.value2)
```

​    

### export default

- 중괄호 없이 import
- import시 export한 이름이 아니어도 됨

```js
// A.js
export default function ExportFunc() {}

// B.js
import ExportFunc from './B.js' 
import BBB from './B.js'  // import시 export한 이름이 아니어도 됨
```

​    

---

## 8️⃣ CRP (Critical Rendering Path)

[브라우저 동작](https://d2.naver.com/helloworld/59361)

[주소창에 google.com 입력했을 때](https://velog.io/@tnehd1998/%EC%A3%BC%EC%86%8C%EC%B0%BD%EC%97%90-www.google.com%EC%9D%84-%EC%9E%85%EB%A0%A5%ED%96%88%EC%9D%84-%EB%95%8C-%EC%9D%BC%EC%96%B4%EB%82%98%EB%8A%94-%EA%B3%BC%EC%A0%95)
