# React (10)

​    

## 로그인

### 

Next.js 렌더링

프리렌더링

Diffing(비교) : 프리렌더링된 HTML과 브라우저에서 렌더링된 HTML을 비교하는 과정

hydration(수분공급) : JS, CSS 파일을 추가하는 과정

조건문일때만 브라우저이용

```js
// 방법1
if (process.browser) {
  // next.js의 프리렌더링시 실행됨
} else {
  // 브라우저상에서 실행됨
}

// 방법2
if (typeof window === "undefined") {
  // next.js의 프리렌더링시 실행됨
} else {
  // 브라우저상에서 실행됨 
}
```



useEffect에서 사용

```js
useEffect(() => {
  // 브라우저 렌더링 종료후 실행됨
}, [])
```



closure

외부함수의 변수는 클로저 스코프에 들어감

Local > Closure > Global



함수를 리턴하는 함수 (HOF - High Order function)

내부함수를 숨길 수 있음

```js
const aaa = (a) => (b) => {
  console.log(b)
  console.log(a)
}

aaa(200)(300)
```



(HOC - High Order Component)