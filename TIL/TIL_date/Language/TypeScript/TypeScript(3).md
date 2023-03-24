# TypeScript (3)

​    

## 1️⃣ React

### 설치

- typescript가 설치된 react 프로젝트 설치

```bash
$ npx create-react-app 프로젝트명 --template typescript 
```

- 기존 프로젝트에 타입스크립트 추가

```bash
$ npm install typescript @types/node @types/react @types/react-dom @types/jest -D
$ yarn add --dev typescript @types/node @types/react @types/react-dom @types/jest
```



### JSX 타입지정

```jsx
const div: JSX.Element = <div></div>
const button: JSX.Element = <button></button>
```

​    

### Component 타입지정

```tsx
interface IProps = {
  a: string;
}

function App(props: IProps): JSX.Element {  // JSX.Element는 생략가능
  return (
  	<></>
  )
}
```

​    

### State 타입지정

- 자동으로 타입할당됨
- 미리 지정하려면 Generic 사용

```jsx
const [user, setUser] = useState<string | null>('');
```

​       

---

