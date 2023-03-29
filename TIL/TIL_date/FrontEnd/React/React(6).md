# React (6)

​    

## 1️⃣ 폴더구조

### Container / Presentation 패턴

- 소스코드를 JS부분(기능)과 JSX부분(UI)으로 나누는 방법
- 파일은 나눠져 있지만 실행은 하나로 합쳐서 실행됨

```bash
프로젝트파일명
├── pages
│     ├── 페이지파일1
│     │      └── index.js
│     └── 페이지파일2
│            └── index.js
└── src  # 따로 생성해줘야함
     ├── commons  # 공통적으로 사용되는 파일들 (함수)
     │      ├── lib   # 공통 자체 라이브러리
     │      └── util  # 공통 함수
     └── components
             ├── commons  # 두번 이상 쓰이는 컴포넌트
             └── units    # 단위컴포넌트 (한번만 사용)
             			├── 기능1 
             			│     ├── 동작1
             			│     │      ├── 기능동작.container.js
             			│     │      ├── 기능동작.presenter.js
             			│     │      ├── 기능동작.queries.js
             			│     │      └── 기능동작.styles.js
             			│     └── 동작2
             			└── board
             			      ├── write
             			      │      ├── BoardWrite.container.js
             			      │      ├── BoardWrite.presenter.js
             			      │      ├── BoardWrite.queries.js
             			      │      └── BoardWrite.styles.js
             			      └── detail
```

​    

- 실행순서 (부모-자식 관계)

1. _app.js (최상단)
2. page/페이지파일/index.js 

```jsx
import BoardWrite from '../../components/units/board/write/BoardWrite.container.js'

export default function BoardWritePage() {
  return <BoardWrite />
}
```

​    

3. src/components/units/기능/동작/기능동작.container.js

```jsx
import { useState } from 'react'
import { useMutation } from '@apollo/client'
import BoardWriteUI from './BoardWrite.presenter.js'
import CREATE_BOARD from './BoardWrite.queries.js'

export default function BoardWrite() {
  const [value, setValue] = useState('')
  const [createBoard] = useMutation(CREATE_BOARD)
 
  const onClickSumbit = async () => {
    const result = await createBoard({ variables: {} })
  }
  const onChangeValue = (e) => { setValue(e.targe.value) }
  
  return 
  	<BoardWriteUI 
    	onClickSumbit={onClickSumbit} 
    	onChangeValue={onChangeValue} 
    />
}
```

> 3-1. graphql 요청파일 분리

```js
import { gql } from '@apollo/client'

export const CREATE_BOARD = gql`
	mutation createBoard($value: String) {
		createBoard(value: $value) {
	  	_id
	  	value
			message
		}
	}
`
```

​     

4. src/components/units/기능/동작/기능동작.presenter.js

```jsx
import { ValueInput, SendButton } from './BoardWrite.styles.js'

export default function BoardWriteUI(props) {
  const { onClickSumbit, onChangeValue } = props
  
  return (
    <>
    	<ValueInput type="text" onChange={onChangeValue} />
    	<SendButton onClick={onClickSubmit}>요청</SendButton>
    </>
  )
}
```

​    

5. css-in-js 파일

```js
import styled from '@emotion/styled'

export const ValueInput = styled.input`
	border-coler: red;
`
export const SendButton = styled.button`
	background-color: black;
`
```

​     

> utils 폴더

- 폴더경로`/src/commons/utils `
- 공통적으로 쓰이는 함수를 저장하는 폴더

```js
// getDate.js
// 날짜를 다루는 함수
export const getDate = (date) => {
  const curDate = new Date(date)
  const year = curDate.getFullYear()
  const month = curDate.getMonth() + 1
  const day = curDate.getDate()
  
  return `${year}-${month}-${day}`
}
```

​    

### atomic 패턴

- 컴포넌트의 중복을 최소화하기 위해 소스코드를 아주 작은 컴포넌트 단위로 쪼개는 방식
- 재사용성이 좋으나, 상위 코드 수정시 수정해야할 부분이 많아짐
- 총 5개의 폴더구조로 이루어짐
  1. Atoms
     - 버튼, 제목, 텍스트 입력 필드와 같은 가장 작은 구성 컴포넌트
     - 모든 컴포넌트들의 기초가 되는 블록
     - 더 이상 분해 될 수 없는 필수 요소
  2. Molecules : 2개 이상의 원자로 구성
  3. Organisms : Molecules의 모음
  4. Templates : Organisms을 모아 템플릿 생성
  5. Pages : 실제 페이지를 구성하는 단위

​    

---

## 2️⃣ export VS export default

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

## 3️⃣ refetchQueries

- 기존 데이터가 변경되었을 때 최신 데이터로 다시 fetch 해주기 위해 사용됨
- Apollo에서 제공하는 기본 기능
- 배열로 시작

```jsx
// 글 삭제하고 데이터 다시받아오기
export default function Page() {
  const [deleteBoard] = useMutation(DELETE_BOARD)
  const { data } = useQuery(FETCH_BOARDS)
  
  const onClickDelete = async () => {
    try {
      const result = await deleteBoard({ 
        variables: { number: Number(e.target.id) },
        refetchQueries: [{ 
          query: FETCH_BOARDS,
          variables: { 기존 fetch때 보낸내용 }  // 기존 fetch에 variables가 있었다면 작성
        }]
      }),
    } catch (error) {}
	}
    
  return (
   <>
    {data?.fetchBoards.map(el => (
    	<Fragment key={el.number}>
    		<div>{el.number}</div>
  			<button id={el.number} onClick={onClickDelete}>삭제</button>
  		</Fragment>	
  	))}
   </>
  )
}
```

​    

---

## 4️⃣ 컴포넌트 재사용

- 수정 / 등록 페이지는 몇몇 요소를 제외하면 동일한 부분이 많아 컴포넌트 재활용을 할 수 있음
- __props__와 __삼항연산자__ 활용

```jsx
// 등록페이지
import BoardComponent from '../../src/components/units/board/..'

export default function BoardNewPage() {
  return <BoardComponent isEdit={false}>
}
```

```jsx
// 수정페이지
import BoardComponent from '../../src/components/units/board/..'

export default function BoardEditPage() {
  return <BoardComponent isEdit={true}
}
```

```jsx
export default function BoardComponent(props) {
  return (
    // 삼항연산자 활용
  	<h1>{props.isEdit ? "수정" : "등록"}</h1>
  	<button onClick={props.isEdit > props.onClickUpdate : props.onClickCreate}>
      {props.isEdit ? "수정" : "등록"}하기
    </button>
  )
}
```

​        

> props drilling

- props가 자식에게 넘겨주는 단계가 두번 이상일 경우를 props drilling이 일어났다라고 함
- 과도하지 않으면 괜찮지만, 과도하면 가독성과 유지보수면에서 좋지 않음
- 이를 방지하기 위해서 global state를 활용함



### 수정한 값만 요청보내기

- 문제점 : 전송 객체가 state의 초기값으로 계속 초기화되어 defaultValue 속성을 부여해도 빈 값이 들어감 
- 해결책 : 변경된 객체만 백엔드에 전송해서 수정하기 (PUT요청)

```jsx
export default function DefaultValue(props) {
  const router = useRouter()
  const [value1, setValue1] = useState('')
	const [value2, setValue2] = useState('')
  
  const onClickSumbit = async () => {
  	const variables = { id: Number(router.query.mynumber) }
    // 변경한 값만 객체에 값 추가
    if (value1) { variables[value1] = value1 }
    if (value2) { variables[value2] = value2 }
	}
  
  // 변경된 객체로 API요청
}

```

​    

>  defaultValue

- input태그의 속성
- 초기값 설정

```jsx
<input 
  type="text" 
  onChange={props.onChangeTitle} 
  defaultValue={props.data?.fetchBoard.title}  ✔️✔️
/>
```