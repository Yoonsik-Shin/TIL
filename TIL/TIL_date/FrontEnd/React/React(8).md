# React (8)

## 

## 라이브러리 / 프레임워크

- 라이브러리 : 특정기능, 도구 1개, React
- 프레임워크 : 도구모음, Next



### 1. 컴포넌트 디자인 라이브러리

#### Ant-Design



#### Material-UI



---

### 2. 주소/우편번호 라이브러리

#### [React-daum-postcode](https://www.npmjs.com/package/react-daum-postcode)

- 주소 검색시 우편번호, 번지수, 도로명주소를 알려주는 라이브러리
- 국내용

```bash
$ yarn add react-daum-postcode
```

​    

---

### 3. 캐러셀 라이브러리

#### [react-slick](https://www.npmjs.com/package/react-slick)

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



---

## 파이어베이스

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

