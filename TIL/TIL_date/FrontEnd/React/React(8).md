# React (8)

​    

## 1️⃣ 라이브러리

- 라이브러리 : 특정기능, 도구 1개, React
- 프레임워크 : 도구모음, Next
- 사용이유
  - 시간절약
  - 버그 최소화
  - 다양한 환경에서 적용되야함

- 주의점
  - 적은 다운로드수, 유명하지 않은 라이브러리는 사용 지양




### 1. 컴포넌트 디자인 라이브러리

#### [Ant-Design](https://ant.design/)

```bash
$ yarn add antd
$ yarn add @ant-design/icons
```



##### 아이콘 적용

- emotion과 같이 사용하는 방법

```jsx
import { MenuUnfoldOutlined } from "@ant-design/icons"
import styled from "@emotion/styled"

const MyIcon = styled(MenuUnfoldOutlined)`  ✔️✔️
  font-size: 50px;
  color: red;
`;

export default function LibraryIconPage() {
  return (
   	<div id='myIcon'> <!-- 다른태그로 감싸줘서 id값을 줘야함 -->
    	<MyIcon />  <!-- 이모션태그에는 id값을 줄 수 없음 -->
    </div>
  )
}
```

​    

##### 별점 적용

- 라이브러리가 제공하는 css를 적용해줘야함

```js
// 전체 페이지에 적용하거나, 라이브러리를 사용하는 페이지에만 적용
import "antd/dist/antd.css"
```

```jsx
import styled from "@emotion/styled"
import { Rate } from "antd"

const MyStar = styled(MenuUnfoldOutlined)`  ✔️✔️
  font-size: 50px;
  color: red;
`;

export default function LibraryStarPage() {
  const [value, setValue] = useState(3)
  
  return <MyStar onChange={setValue}/>
}
```

- 라이브러리에서 만든 태그에는 기존에 사용하던 속성과 이름만 같고 기능은 다른 경우가 있을 수 있음

```jsx
// 같은 onChange같지만, 사용법 다름
<input onChange={} />  
<MyStar onChange={} />
```

​    

##### Modal 적용

```jsx
// 기본 모달
import { Modal } from 'antd'

const success = () => { Modal.success({ content: "등록 성공" }) }
const error = () => { Modal.error({ content: "등록 실패" }) }

export default function App() {
  return (
  	<button onClick={success}>성공시</button>
    <button onClick={error}>실패시</button>
  )
}
```

```tsx
// 커스텀 모달
import { useState } from 'react';
import { Modal } from 'antd';

export default function App() => {
  const [isOpen, setIsOpen] = useState(false);
  const onToggleModal = () => { setIsOpen(prev => !prev) }

  return (
    <>
      <button onClick={onToggleModal}>모달창 열기</button>
    	
    	{/* 모달 종료 방식 - 1. 모달 숨기기 */}
			<!-- 눈에 안보이도록 css적으로 숨김 처리 -->
      <Modal open={onToggleModal} onOk={onToggleModal} onCancel={onToggleModal}>
        <input type="password" />
      </Modal>
    	
		  {/* 모달 종료 방식 - 2. 모달 삭제 */}
			<!-- state값이 바뀌면 리렌더링되면서 새로운 모달이 생성됨 -->
    	{isOpen && (
        <Modal open={true} onOk={onToggleModal} onCancel={onToggleModal}>
        	<input type="password" />
      	</Modal>
      )}
    </>
  )
}
```

> Modal을 종료하는 방식

1. 숨겼다가 나타나게 하는 방식
   - 눈에 안보이도록 css적으로 숨김 처리
   - 이력서
2. 삭제했다가 새로 생성하는 방식
   - state값이 바뀌면 리렌더링되면서 새로운 모달이 생성됨
   - 신용카드, 비밀번호

​    

#### [Material-UI](https://material-ui.com/)

```bash
$ yarn add @material-ui/core
```

​     

---

### 2. 주소/우편번호 라이브러리

#### [React-daum-postcode](https://www.npmjs.com/package/react-daum-postcode)

- 주소 검색시 우편번호, 번지수, 도로명주소를 알려주는 라이브러리 (국내용)

```bash
$ yarn add react-daum-postcode
```

```tsx
import DaumPostcodeEmbed, { Address } from 'react-daum-postcode';

export default function PostCode() {
  const handleComplete = (address: Address) => {
    console.log(address)
  }
  
  return <DaumPostcodeEmbed onComplete={handleComplete} />;
}
```

​    

---

### 3. 캐러셀 라이브러리

#### [react-slick](https://www.npmjs.com/package/react-slick)

```bash
$ yarn add react-slick
$ yarn add --dev @types/react-slick
```

​     

---

### 4. 폼 / 검증 라이브러리

#### React-Hook-Form

- 비제어 컴포넌트를 사용하여 성능이 빠름

```bash
$ npm install react-hook-form
$ yarn add react-hook-form
```

```jsx
import { useForm } from "react-hook-form"

interface IFormDate {
  state이름1: string;
  state이름2: string;
}

export default function ReactHookFormPage() {
  const { register, handleSubmit } = useForm<IFormDate>()
  
  const onClickSubmit = (data) => {
    console.log(data)  // { state이름1: "input입력값1", state이름2: "input입력값2" }
  }
  
  return (
  	<form onSubmit={handleSubmit(onClickSubmit)}>
      <input type="text" {...register("state이름1")} />
      <input type="text" {...register("state이름2")} />
      <button>등록</button>
    </form>
  )
}
```



> button 태그의 type 속성

```html
<button type="button">그냥버튼</button>
<button type="submit">보내기</button>  <!-- 기본값 -->
<button type="reset">지우기</button>
```

​    

#### [Yup](https://www.npmjs.com/package/yup)

- 폼의 데이터들을 검증해줌
- 검증 데이터 추가에 용이함

> 설치

```bash
$ yarn add @hookform/resolvers yup
```

> 검증파일 작성

```js
import { useForm } from "react-hook-form"
import { yupResolver } from "@hookform/resolvers/yup"
import * as yup from "yup"

export const schema = yup.object({
  writer: yup.string().required("작성자를 입력해주세요")
	contents: yup.string().required("내용을 입력해주세요")
	email: yup
 		.string()
		.email("이메일 형식에 적합하지 않습니다.")
		.required("이메일은 필수 입력입니다."),
  password: yup
  	.string()
		.min(4, "비밀번호는 최소 4자리 이상 입력해주세요")
		.max(15, "비밀번호는 최대 15자리까지 입력가능합니다.")
		.required("비밀번호는 필수 입력입니다.")
	phone: yup
  	.string()
		.matches(/^\d{3}-\d{3,4}-\d{4}$/, "전화번호 형식이 알맞지 않습니다.")
		.required("전화번호는 필수 입력입니다.")
})
```

> Input, button 분리

![image-20230331150201240](React(8).assets/image-20230331150201240.png)

```jsx
// src/components/commons/inputs/01
import { UseFormRegisterReturn } from "react-hook-form"

interface IProps {
  type: "text" | "password";
  register: UseFormRegisterReturn;
}

export default function Input01(props: IProps) {
  return <input type={props.type} {...props.register} />
}
```

```jsx
// src/components/commons/button/01
interface IProps {
  isActive: boolean;
  title: string;
}

export default function Button01(props: IProps) {
  return (
  	<button style={{ backgroundColor: formState.isActive ? "색상" : ""}>
    	{props.title}    
    </button>
  )
}
```

> 정리

```jsx
import { useForm } from "react-hook-form"
import { schema } from "./src/~~"

interface IFormDate {
  state이름1: string;
  state이름2: string;
}

export default function ReactHookFormPage() {
  const { register, handleSubmit, formState } = useForm<IFormDate>({
    resolver: yupResolver(schema),  ✔️✔️
    mode: "onChange",  ✔️✔️
  })
  
  const onClickSubmit = (data) => {
    console.log(data)  // { state이름1: "input입력값1", state이름2: "input입력값2" }
  }
  
  return (
  	<form onSubmit={handleSubmit(onClickSubmit)}>
      <Input01 type="text" {...register("state이름1")} />
      <div>{formState.errors.state이름1?.message}</div>
      <Input01 type="text" {...register("state이름2")} />
      <div>{formState.errors.state이름2?.message}</div>
      <Button01 title="등록하기" isActive={formState.isValid} />
    </form>
  )
}
```

​    

### 5. 시간 관련 라이브러리

#### Moment.js 

>  시간관련 이벤트

- 시간을 새로 생성하는 작업은 절대 프론트엔드에서 하면 안됨
- 사용자의 PC가 실제와 다르면, 프론트에서 생성한 시간도 실제와 다른 시간을 따라감
- 국제 표준시인 UTC 시간을 사용함



​    

---

## 2️⃣ 파이어베이스

- Baas 서비스 (Backend As A Service)
- 구글에서 백엔드를 서비스로써 제공해줌



### 사이트 설정

>  https://firebase.google.com/?hl=ko

<img src="React(8).assets/image-20230331153512540.png" alt="image-20230331153512540" style="zoom: 50%;" /><img src="React(8).assets/image-20230331153600223.png" alt="image-20230331153600223" style="zoom:50%;" />

<img src="React(8).assets/image-20230331153649438.png" alt="image-20230331153649438" style="zoom:50%;" />

<img src="React(8).assets/image-20230331153709085.png" alt="image-20230331153709085" style="zoom: 67%;" />

<img src="React(8).assets/image-20230331153742421.png" alt="image-20230331153742421" style="zoom: 67%;" />

<img src="React(8).assets/image-20230331153939692.png" alt="image-20230331153939692" style="zoom: 67%;" /><img src="React(8).assets/image-20230331154007468.png" alt="image-20230331154007468" style="zoom: 67%;" />

<img src="React(8).assets/image-20230331154016970.png" alt="image-20230331154016970" style="zoom:67%;" />

<img src="React(8).assets/image-20230331154249976.png" alt="image-20230331154249976" style="zoom:67%;" />

​    

### 설치 

```bash
$ npm install firebase
$ yarn add firebase
```

​    

### 데이터 등록 / 조회

> [Firebase문서](https://firebase.google.com/docs/?authuser=0&hl=ko)

```jsx
import { collection, addDoc, getDocs, getFirestore } from 'firebase/firestore/lite'

export default function FirebasePage() {
  
  // 데이터 등록
	const onClickSubmit = async () => {
    // board라는 컬렉션에 연결, 없으면 만들어서 연결해줌
    const board = collection(getFirestore(firebaseApp), "board") 
    await addDoc(board, { // 데이터 전송
      writer: "작성자",
      title: "제목",
      contents: "내용"
    })
  }
  
  // 데이터 조회
  const onClickFetch = async () => {
    const board = collection(getFirestore(firebaseApp), "board")  // 컬렉션 연결
    const result = await getDocs(board)  // 데이터 조회
    const datas = result.docs.map(el => el.data())  // 배열형식으로 데이터를 받아와서 가공해줘야함
  }
  
  return (
  	<>
    	<button onClick={onClickSubmit}>등록</button>
    	<button onClick={onClickFetch}>조회</button>
    </>
  )
}
```

```js
// 파이어베이스 접속정보
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDjLBjOpY6Z6-ihw7XkSPtV7K3UUNWVy20",
  authDomain: "test-9adce.firebaseapp.com",
  projectId: "test-9adce",
  storageBucket: "test-9adce.appspot.com",
  messagingSenderId: "509929578393",
  appId: "1:509929578393:web:c7231ea2fb66a5921cbd08"
};

// Initialize Firebase
export const firebaseApp = initializeApp(firebaseConfig);
```

