# Test Code (1)

## 테스트 종류

1. 단위테스트 (Unit)
   - 함수, 컴포넌트등의 기능 하나를 테스트 진행 (버튼클릭)
   - 다른 코드의 유닛과 상호작용하는 것을 배제함
   - 주로 jest 사용

2. 통합테스트(Integration)

- 유닛 간의 상호작용 테스트
- 여러 기능 한꺼번에 테스트
- 주로 jest 사용

3. E2E 테스트 (End To End)

- 시나리오가 있는 테스트를 진행
- 가상의 브라우저를 띄워 테스트 진행

​    

- React Testing Library
  - 가상 DOM 렌더링, 검색, 상호작용
  - 가상 DOM이 원하는 대로 작동하지는 확인
- Jest
  - 테스트 러너
  - 테스트를 찾아 실행한 후 테스트 통과여부를 결정
- Jest-dom
  - DOM을 기반으로 한 매처를 제공



```ts
import { render, screen } from '@testing-library/react'
```

-  `render()` 메서드
  - 인수로 제공되는 JSX에 대한 가상 DOM을 생성
- `screen` 전역 객체
  - 렌더링된 가상 DOM에 액세스할 수 있게 해주는 객체
- `getByText()` 메서드
  - 렌더링되는 모든 텍스트에서 인수(정규표현식)로 받은 텍스트를 가상 DOM 요소에서 찾음 
- 단언 (Assertion)
  - 테스트의 통과 여부를 결정하는 부분
  - 예상과 다르게 동작되었을 때, 에러를 던져 테스트가 실패함
- `expect()` 메서드
  - 전역메서드
  - 인수로는 기대되는 값을 넣음
- 매처 (Matcher)
  - 단언의 유형



`test` 전역 테스트 메서드

- 2가지 인수를 가짐
  1. 문자열 설명
     - 테스트가 실패했을 때 어떤 테스트가 실패했는지 알려줌
  2. 테스트 함수
     - 테스트의 성공/실패를 결정하기 위해 사용



Watch Mode

- 마지막 커밋이후 파일의 모든 변경사항을 확인하여 마지막 커밋 이후 변경된 파일과 연관된 테스트만 실행



---

## 설치 / 세팅

### next.js

- [공식문서](https://nextjs.org/docs/testing)

> 설치

```bash
$ yarn add --dev jest   
$ yarn add --dev jest-environment-jsdom
$ yarn add --dev @testing-library/react
$ yarn add --dev @testing-library/jest-dom
```

​    

> Next.js에서의 jest.config.js 

```js
// jest.config.js 
const nextJest = require("next/jest");

const createJestConfig = nextJest({
  // Provide the path to your Next.js app to load next.config.js and .env files in your test environment
  dir: "./",
});

// Add any custom config to be passed to Jest
/** @type {import('jest').Config} */
const customJestConfig = {
  // Add more setup options before each test is run
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  // if using TypeScript with a baseUrl set to the root directory then you need the below for alias' to work
  moduleDirectories: ["node_modules", "<rootDir>/"],  ✔️✔️ // 추가로 작성해줘야함
  testEnvironment: "jest-environment-jsdom",
};

// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
module.exports = createJestConfig(customJestConfig);
```

>  eslint와 함께 사용하려면 필요한 설정

```js
// .eslint.js
plugins: ["react", "jest/globals"]
```

>  package.json에 jest 실행 명령어 추가

```json
"scripts": {
  "test": "jest",
  "test:watch": "jest --watch"
}
```



> ❗주의사항

- __React__는 개별 페이지 폴더에 `__test__`폴더를 생성하고, 그 폴더 안에 테스트코드 파일(`index.test.ts`) 작성
- __next.js__는 page폴더 바깥쪽에 `__test__`폴더를 생성하고, 해당폴더에 개별 페이지 폴더를 생성한 후 파일 작성



> 실행

```json
// package.json
{
  "scripts": {
    ...
    "test": "jest"
  }
}
```

```bash
$ yarn test
$ yarn test:watch
```

​    

----

## Jest 

### 기본문법

#### it

- 단일 테스트

```js
it("테스트명 작성", () => {
  const result = 테스트할 로직
  expect(result).매쳐
})
```



#### describe

- 단일테스트를 하나의 그룹으로 묶기

```js
describe("테스트 그룹명 작명", () => {
  it("테스트명 작성", () => {
    const result = 테스트할 로직
    expect(result).매쳐
  })
  
  it("테스트명 작성", () => {
    const result = 테스트할 로직
    expect(result).매쳐
  })
  
  ...
})
```



### 단위테스트 (unit)

#### UI 테스트

- 원하는대로 렌더링 됐는지 확인

```tsx
// 테스트할 실제 코드
export default function TestWantPage() {
  return (
  	<div>테스트1</div>
    테스트2 입력받기: <input type="text" />
  )
}
```

```tsx
import { render, screen } from '@testing-library/react'
import "@testing-library/jest-dom"
import TestWantPage from ''

it('UI 렌더링 테스트', () => {
  render(<TestWantPage />)
  
  const Text1 = screen.getByText("테스트1")
  expect(Text1).toBeInTheDocument()  // dom안에 '테스트1' 이라는 텍스트가 있는지 확인
  
  const Test2 = screen.getByText("테스트2 입력받기: ")
  expect(Text1).toBeInTheDocument()  // dom안에 '테스트2 입력받기: ' 이라는 텍스트가 있는지 확인
})
```

​    

##### snapshot 테스트

- 코드 수정시 기존 UI와 바뀐 부분이 없는지를 테스트
- 기존 snapshot이 없는 상태에서 실행하면 snapshot을 생성
- snapshot이 있다면 그 snapshot과 현재 상태를 비교

```tsx
import { render, screen } from '@testing-library/react'
import "@testing-library/jest-dom"
import TestWantPage from ''

it('스냅샷 테스트', () => {
  const result = render(<TestWantPage />)
  expect(result.container).toMatchSnapShot()
})
```

![image-20230427131311878](Test_Code(1).assets/image-20230427131311878.png)

![image-20230427131551066](Test_Code(1).assets/image-20230427131551066.png)

- snapshot 테스트 실패시, 코드를 수정한 후 아래 명령어 실행하면 snapshot을 업데이트한 후 테스트 진행

```bash
$ yarn test -u
```

![image-20230427131627656](Test_Code(1).assets/image-20230427131627656.png)

​    

#### 기능테스트

##### 클릭 테스트

```js
it("버튼 클릭시, 정상 작동 확인", () => {
  render(<TestPage />)
  fireEvent.click(screen.getByRole("countUp"))
  expect(screen.getByRole("count")).toHaveTextContent("1")
})
```

```jsx
// 테스트할 페이지
export default function TestPage() {
  const [count, setCount] = useState(0)
  const onClickCountUp = () => { setCount((prev) => prev + 1) }
  
  return (
  	<>
    	<div role="count">{count}</div>
    	<button role="countUp" onClick={onClickCountUp}>클릭</button>
    </>
  )
}
```

​    

##### API요청 테스트

```js
it("API요청 테스트", () => {
  render(<TestPage />)
  fireEvent.change(s)
})
```



msw

```bash
$ yarn add --dev msw
```

cross-fetch

```bash
$ yarn add --dev cross-fetch
```

next-router-mock

```bash
$ yarn add --dev next-router-mock 
```

​    

## Cypress

```bash
$ yarn add --dev cypress
```

```json
// package.json
{
  "scripts": {
    "cypress": "cypress open"
  }
}
```

```bash
$ yarn cypress
```

