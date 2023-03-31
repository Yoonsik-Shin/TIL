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
│     │      └── index.ts
│     └── 페이지파일2
│            └── index.ts
└── src  # 따로 생성해줘야함
     ├── commons  # 공통적으로 사용되는 파일들
     │      ├── lib   # 공통 자체 라이브러리
     │      ├── util  # 공통 함수
     │      └── styles  # 공통 CSS
     └── components
             ├── commons  # 두번 이상 쓰이는 컴포넌트
             │      └── layout  # 레이아웃 컴포넌트
             │						├── banner
             │						├── footer
             │						├── header
             │						├── navigation
             │						├── sidebar
             │						└── index.js  # 모든 레이아웃들을 합쳐주는 파일
             └── units    # 단위컴포넌트 (한번만 사용)
             			├── 기능1 
             			│     ├── 동작1
             			│     │      ├── 기능동작.container.tsx
             			│     │      ├── 기능동작.presenter.tsx
             			│     │      ├── 기능동작.queries.ts
             			│     │      ├── 기능동작.styles.ts
             			│     │      └── 기능동작.types.ts
             			│     └── 동작2
             			└── board
             			      ├── write
             			      │      ├── BoardWrite.container.tsx
             			      │      ├── BoardWrite.presenter.tsx
             			      │      ├── BoardWrite.queries.ts
             			      │      ├── BoardWrite.styles.ts
             			      │      └── BoardWrite.types.ts
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

## 2️⃣ 레이아웃 컴포넌트

![image-20230330152806087](React(6).assets/image-20230330152806087.png)

```jsx
// src/components/commons/layout/header/index.tsx
import styled from "@emotion/styled";

const Wrapper = styled.div`
  height: 50px;
  background-color: lightcoral;
`;

export default function LayoutHeader() {
  return <Wrapper>여기는 헤더입니다.</Wrapper>;
}
```

```jsx
// src/components/commons/layout/index.tsx
export default function Layout(props) {
  return (
  	<>
    	<LayoutHeader />
      <LayoutBanner />
      <LayoutNavigation />
    	<LayoutBodyWrapper>
    		<LayoutSidebar />
      	<LayoutBody>{props.children}</LayoutBody>
    	</LayoutBodyWrapper>
    	<LayoutFooter />
    </>
  )
}
```

```jsx
// _app.js
export default function App({ Component, pageProps }) {
  return (
  	<Layout>
      <Component {...pageProps} />
    </Layout>
  )
}
```

​    

### 레이아웃 미적용 영역설정

- 특정 페이지에는 특정 레이아웃이 보이지 않았으면 할 때
- `include`메서드로 배열내 값과 현재페이지의 asPath값을 비교하여 동일하면 레이아웃 제외

```js
// src/components/commons/layout/index.tsx
const HIDDEN_HEADERS = [
  '/레이아웃 제외 페이지주소',
  '/login'
]  ✔️✔️

export default function Layout(props) {
  const router = useRouter()
  const isHiddenHeader = HIDDEN_HEADERS.includes(router.asPath)  ✔️✔️
  
  return (
  	{!isHiddenHeader && <Header />}  // 해당 페이지에서 제외할 레이아웃
  )
}
```

​    

---

## 3️⃣ 글로벌 스타일 적용

- 모든 컴포넌트에 기본적으로 적용시켜주는 스타일
- `_app.tsx`에 적용해줘야함

```jsx
// _app.tsx
import { Global } from '@emotion/react'
import { globalStyles } from "../src/commons/styles/globalStyles";

export default function App({ Component, pageProps }) {
  return (
    <Global styles={globalStyles} />
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}
```

![image-20230330193448275](React(6).assets/image-20230330193448275.png)

```js
// global css 적용파일
import { css } from '@emotion/react'

export const globalStyles = css`
	* {
		margin: 0;
		box-sizing: 0px;
		font-family: myfont;  ✔️✔️
	}
	
	@font-face {
		font-family: "myfont";  ✔️✔️
		src: url("/fonts/폰트파일")  
	}
`
```

​    

### 폰트 적용

![image-20230331004717224](React(6).assets/image-20230331004717224.png)

- `@font-face` 선택자를 이용해 폰트 호출 이름과 경로를 선언
- `font-family` : 폰트를 호출할 이름을 정의해주는 속성
- `src` : 폰타파일의 경로
- font를 적용할 css에 `font-family`
- 압축률이 가장 높은 폰트 확장자 : `woff2`

​    

>FOIT (Flash of Invisible Text)

- 브라우저가 웹 폰트를 다운로드하기 전에 텍스트가 보이지 않는 현상
- 대부분의 웹사이트는 FOIT 현상이 기본값

​    

> FOUT (Flash of Unstyled Text)

- 브라우저가 웹 폰트를 다운로드하기 전에 텍스트가 대체 글꼴로 렌더링되는 현상

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

​    

---

## 5️⃣ export VS export default

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

## 6️⃣ refetchQueries

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

## 7️⃣ [graphql-codegen](https://www.graphql-code-generator.com/)

- graphql API에서 docs를 기준으로 타입파일을 자동으로 추출해줌

​    

### 설치

```bash
$ yarn add -D @graphql-codegen/cli
$ yarn add -D @graphql-codegen/typescript 
```

​    

### 설정

- `schema` : graphql url주소를 넣어줌 (_app.tsx의 주소와 동일)

```yaml
# codegen.yaml
schema: 백엔드주소
generates:
	./src/commons/types/generated/types.ts:
		plugins:
			- typescript
		config:
			typesPrefix: I
```



### 실행

- graphql-API에서 데이터를 받아 자동으로 TS파일을 `./src/commons/types/generated/types.ts` 위치에 만들어줌

```json
// package.json
"scripts": {
	"generate": "graphql-codegen"
}
```

```bash
$ yarn generate
```

​    

### 적용

#### Mutation

```typescript
const [함수] = useMutation<응답타입, variables타입>()
const [createBoard] = useMutation<Pick<Mutation,"createBoard">,MutationCreateBoardArgs>(CREATE_BOARD)
```

​    

#### Query

```typescript
const { data } = useQuery<Pick<Query,"fetchBoard">,QueryFetchBoardArgs>(FETCH_BOARD, {
  variables: { number: Number(router.query.number )}
})
```

