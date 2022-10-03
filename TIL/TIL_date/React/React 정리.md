# React 정리



## 왜 사용하는가

- 싱글페이지 어플리케이션 (Single Page Application)을 만들고 싶을 때 사용
- html 재사용 편리
- React Native에도 활용가능



## 설치법

1. node.js 설치
2. 프로젝트 폴더 만들기
3. 터미널에서 명령어 입력

```bash
npx create-react app <앱 이름>
```

> (윈도우) 설치 오류시

```bash
Set-ExecutionPolicy Unrestricted
```



src파일 > App.js

미리보기 : npm start

Create React App 라이브러리 사용



## React 파일정리

node_modules

- 라이브러리 코드 보관함
- 따로 수정 x

public 

- static 파일 보관함
- html, 이미지 파일등을 임시로 저장하고 싶을때

src

- 소스코드 보관함
- 직접 코드를 작성하는 곳
- App.js : 메인페이지

package.json

- 프로젝트 정보
- 따로 수정 x



## JSX

- 자바스크립트 파일에서 HTML언어와 유사한 기능을 하는 언어

### HTML과 다른점

1. 클래스

```jsx
<div className="클래스이름"></div>
```

2. 변수 (데이터 바인딩)

```jsx
let 변수명;
<h4>{ 변수명 }</h4>
```

3. 스타일

```jsx
<h1 style= { {스타일명:'값'} }></h1>
<h1 style= { {color:'red', fontSize: '16px'} }></h1>
```

> ❗ 변수명 카멜케이스 사용

4. return () 안에는 병렬로 태그 2개이상 기입 금지

```jsx
return (
	<div>1번</div>
	<div>2번</div>  // 불가능
)
```

```jsx
return (
	<div>  // 무조건 하나에 들어있어야함 (컨테이너 같은 느낌)
  	<div>1번</div>
		<div>2번</div>  // 불가능
  </div>
)
```

​    

## State

- 자료 잠깐 보관하기
- 변수는 자동으로 내용 변경시 html에 재렌더링 안됨
- state는 재렌더링이 자동으로 html에 반영
- 자주 변경될거같은 html 부분은 state로 만들기

```javascript
import { useState } from "react";

let [변수명1, 변수명2] = useState('보관할 자료')
let [글제목, b] = useState('남자 코트 추천')
```

- 변수명1 : state에 보관했던 자료
- 변수명2 : state변경을 도와주는 함

​    

> 자바스크립트 Destructuring

```javascript
let num = [1, 2, 3]

// 기본
let a = num[0]
let b = num[1]
let c = num[2]

// Destructuring
let [a, b, c] = [1, 2, 3]
```

​    

### State 수정

- array, object를 다룰 때 원본은 보존하는게 좋음
- array/object를 담은 변수엔 메모리값만 저장되어있음 (reference data type)

```jsx
let a = [1, 3, 5];
let b = a;
b[0] == 300;
console.log(a === b) // true
```

- `기존 state == 신규 state`의 경우 변경 안함

- state가 array나 object이면 독립적인 카피본(shallow copy)을 만들어 수정해야함

```jsx
<button onClick={ () => {
    let copy = [...state_1];   // 메모리값을 바꿔줌
    copy[바꿀 인덱스] = "바꿀값";
    state_2(copy);
  }};
```

