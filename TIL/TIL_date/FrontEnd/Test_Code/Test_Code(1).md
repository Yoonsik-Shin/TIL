# Test Code (1)



## 테스트 종류

1. 단위테스트

- 기능 하나하나를 테스트 진행 (버튼클릭)
- 주로 jest 사용

2. 통합테스트

- 여러 기능 한꺼번에 테스트
- 주로 jest 사용

3. E2E 테스트 (End To End)

- 시나리오가 있는 테스트를 진행
- 가상의 브라우저를 띄워 테스트 진행

​    

---

## 설치 / 세팅

> 설치

```bash
$ yarn add --dev jest jest-environment-jsdom @testing-library/react @testing-library/jest-dom
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
  moduleDirectories: ["node_modules", "<rootDir>/"],
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



__React__는 개별 페이지 폴더에 `__test__`폴더를 생성하고, 그 폴더 안에 테스트코드 파일(`index.test.ts`) 작성

__next.js__는 page폴더 바깥쪽에 `__test__`폴더를 생성하고, 해당폴더에 개별 페이지 폴더를 생성한 후 파일 작성



> 실행

```bash
$ yarn test
$ yarn test:watch
```

​    

----

## Jest 기초문법

### it

### describe



### UI 테스트

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
  expect(Text1).toBeInTheDocument()
  
  const Test2 = screen.getByText("테스트2 입력받기: ")
  expect(Text1).toBeInTheDocument()
})
```



#### snapshot 테스트

```tsx
import { render, screen } from '@testing-library/react'
import "@testing-library/jest-dom"
import TestWantPage from ''

it('스냅샷 테스트', () => {
  const result = render(<TestWantPage />)
  expect(result.container).toMatchSnapShot()
})
```



### 기능테스트