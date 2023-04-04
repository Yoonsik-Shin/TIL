# React-query (1)

​    

## 0️⃣ 개념

- 리액트환경에서 서버상태 가져오기, 캐싱, 동기화, 업데이트를 도와주는 라이브러리
- 클라이언트 상태와 서버상태를 구분하기 위해 사용
- 예시
  - 클라이언트 상태 `input` 값
  - 서버 상태 :  DB에서 저장돼 있는 데이터
- 기능
  - 데이터 캐싱
  - 동일한 데이터에 대한 중복요청을 단일 요청으로 통합
  - 오래된 데이터들을 업데이트하고 빠르게 반영
  - 데이터가 생성되고 얼마나 지났는지 확인가능
  - 서버 상태의 메모리, 가비지 수집 관리
  - 구조 공유를 사용해 쿼리 결과 메모화
  - 페이지네이션, 무한스크롤

​    

---

## 1️⃣ 설정

- `v3` 에서 `v4`로 넘어오며 `react-query`에서 `TanStack Query`로 이름이 변경되었고, 몇가지 문법이 변경됐으나, 기본적인 틀은 비슷함
- `queryClient`에서 기본옵션을 설정을 추가 할 수 있음 ([QueryClient 옵션](https://tanstack.com/query/v4/docs/react/reference/QueryClient))

```jsx
// v3
import { QueryClient, QueryClientProvider  } from 'react-query'

// v4
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'

// 설정
const queryClientConfig = {} 
```

```jsx
// react => index.tsx
const queryClient = new QueryClient(queryClientConfig)

root.render(
  <QueryClientProvider client={queryClient}>  ✔️✔️
		<App />
  </QueryClientProvider>  ✔️✔️
)
```

```jsx
// next.js => _app.tsx
export default function App() {
  const [queryClient] = useState(() => new QueryClient());
  
  return (
    <QueryClientProvider client={queryClient}>  ✔️✔️
  		<Component {...pageProps} />
    </QueryClientProvider>  ✔️✔️
  )
}
```

​    

---

## 2️⃣ DevTools

- devTools은 `process.env.NODE_ENV === development`일 때만 실행됨
- 배포시에 따로 처리해줄 것은 없음
- `v3`까지는 패키지에 포함이었지만, `v4`부터는 별도로 설치해줘야함

```bash
# v4 버전만 설치
$ npm install @tanstack/react-query-devtools
$ yarn add @tanstack/react-query-devtools
```

```jsx
// v3
import { ReactQueryDevtools } from "react-query/devtools";

// v4
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
```

```jsx
// react => index.tsx
const queryClient = new QueryClient(queryClientConfig)

root.render(
  <QueryClientProvider client={queryClient}>  ✔️✔️
		<App />
  </QueryClientProvider>  ✔️✔️
)
```

```jsx
// v4
// next.js => _app.tsx
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

export default function App() {
  const [queryClient] = useState(() => new QueryClient());
  
  return (
    <QueryClientProvider client={queryClient}>
      <Component {...pageProps} />
      <ReactQueryDevtools initialIsOpen={false} />  ✔️✔️
    </QueryClientProvider>
  )
}
```

​     

### 옵션

- `initialIsOpen`
  - true / false (boolean)
  - `true`이면 개발자 도구가 기본적으로 열려 있게 함
- `postion` 
  - devTool 위치 설정
  - 옵션값 (없어도됨)
  - 기본값 : bottom-left
  - 종류 : `top-left`, `top-right`, `bottom-left`, `bottom-right`
- 이외 더 많음 옵션이 존재함

​    

---

## 3️⃣ 캐싱 라이프 사이클

1. Query Instances with and without cache data
2. Background Refetching
3. Inactive Queries
4. Garbage Collection



### 예시

1. `post`라는 querykey를 가진 퀴리 인스턴스가 __mount__됨
2. 네트워크에서 데이터가 fetch 되고, 불러온 데이터는 `psot` 라는 queryKey로 __캐싱__됨
3. 데이터는 `fresh`상태에서 `staleTime`이후 `stale`상태로 변환됨
4. `post` 쿼리 인스턴스가 __unmount__됨
5. `cacheTime`만큼 캐시가 유지되다가 __가비지 콜렉터(GC)__에 수집됨
6. 만약 `cacheTime`전이고, 쿼리 인스턴스가 `fresh`한 상태에서 새롭게 __mount__되면 캐시데이터를 보여줌

​    

---

## 4️⃣ `useQuery`

- 첫번 째 인자인 `queryKey`를 기준으로 데이터 캐싱을 관리

```js
const getData = async () => {
  const data = await axios()
  return data
}

const { data, isLoading, isError, ... } = useQuery({
  queryKey: ['작명'],  
  queryFn: 데이터를 불러오는 함수
  options: {}
})
```



### queryKey

- ```queryKey: unknown[]```
- 필수요소
- 사용할 쿼리에 이름을 붙이는 요소
- 이 요소가 변경되면 쿼리가 자동으로 업데이트됨 (쿼리의 의존성배열)
- 만약 같은 queryKey에서 데이터를 구분하려면, 추가적인 변수를 사용할 수 있음

```js
const { data, isLoading, isError, ... } = useQuery({
  queryKey: ['작명', 추가변수 ✔️✔️],  
  queryFn: 데이터를 불러오는 함수
  options: {}
})
```

​    

### queryFn

- `queryFn: (context: QueryFunctionContext) => Promise<TData>`
- 필수요소
- Promise 객체를 반환해야함

​    

### return

```js
const { data, isLoading, isError, error, isFetching, status, fetchStatus, ... } = useQuery()
```

1. `data` 
   - 쿼리함수가 반환한 promise 객체에서 resolved된 데이터
2. `isLoading`
   - 캐싱된 데이터가 없을 때
   - 처음 실행된 쿼리일 때 로딩 시간동안은 `true`, 이후는 `false`가 됨
   - 캐싱된 데이터가 있으면 로딩과 상관없이 `false`상태임
3. `isFetching`
   - 캐싱된 데이터가 있어도 쿼리가 실행되면 로딩 시간동안은 `true`, 이후는 `false`가 됨
   - 캐싱된 데이터가 있더라도 쿼리가 실행되면 동작함
4. `error`
   - 쿼리함수에 오류가 발생한 경우, 쿼리에 대한 오류 객체
5. `isError`
   - 에러가 발생하면 `true`값을 가짐
6. `status`
   - `loading` : 아직 캐시된 데이터가 없이 로딩중일 떄
   - `error` : 요청중 에러 발생시
   - `success` : 요청 성공시
   - ❗(`v3`까지만 적용)`idle`
7. `fetchStatus`
   - `v4`부터 status에 `idle`값이 제거되고 추가됨
   - `fetching` : 쿼리가 현재 실행중
   - `paused` : 쿼리를 요청했지만, 잠시 중단된 상태
   - `idle` : 쿼리가 현재 아무 작업도 수행하지 않은 상태



> status VS fetchStatus 

- status는 `data`가 있는지 없는지에 대한 상태를 의미
- fetchStatus는 `queryFn` 요청이 진행중인지 아닌지에 대한 상태를 의미

​    

### options

- useQuery의 3번째 인자로 들어갈 수 있는 값들

```js
const { data } = useQuery({
  queryKey: [''],                    
  queryFn: Fn,
  options: {
  	options ✔️✔️
	}
})
```

​    

#### 1. staleTime

- number | Infinity
- 데이터가 fresh상태에서 stale 상태로 변경되는데 걸리는 시간
- `stale`은 `썩은`이라는 의미로, 데이터가 최신 상태가 아님을 의미
- `fresh`는 데이터가 최신 상태를 의미함
- 데이터가 fetching된 이후 아직 staleTime이 지나지 않았다면, unmout된 후 다시 mount가 되어도 fetch가 일어나지 않음
- 기본값이 `0`이므로 일반적으로 fetch 받은 후 모든 데이터들은 `stale` 상태가 된다.

​    

#### 2. cacheTime

- number | Infinity
- 데이터가 `inactive` 상태일 때 캐싱된 상태로 남아있는 시간
- 쿼리 인스턴스가 unmount되면 데이터는 `inactive`상태로 변경되는데, 이 때부터 `cacheTime`만큼 캐시가 유지되게 됨
- 이 시간이 지나면 캐싱데이터들은 가비지 컬렉터로 수집됨
- `cacheTime`이 지나기 전에 다시 mount해주면, 데이터 fetch시에 캐시데이터를 보여줌
- `stale`타임과는 관계없이 `inactive`상태를 기준으로 행동
- 기본값은 5분

​    

#### 3. refetchOnMount

- boolean | "always"
- 데이터가 `stale`인 경우, mount마다 refetch를 실행하는 옵션
- `always` 설정시 mount마다 refetch 실행
- `false` 설정시 최초 fetch이후 refetch하지 않음
- 기본값 : `true`

​    

#### 4. refetchOnWindowFocus

- boolean | "always"
- 데이터가 `stale`일 경우, 윈도우 포커싱이 될때마다 refetch를 실행하는 옵션
- `always`설정시 윈도우가 포커싱 될 때 마다 refetch 실행

​    

#### 5. Polling (refetchInterval / refetchIntervalInBackground)

```js
const { data } = useQuery([''], Fn, {
  refetchInterval: 3000,
  refetchIntervalInBackground: true
})
```

- 폴링 : 리얼타임 웹기법으로, 일정 주기를 가지고 서버와 응답을 주고받는 방식
- `refetchInterval`옵션과 `refetchIntervalInBackground`옵션을 이용하여 구현가능
- `refetchInterval` : 시간을 넣어주면 일정 시간마다 자동으로 refetch (number)
- `refetchIntervalInBackground` : 브라우저가 focus되지 않아도 refetch 시켜주는 옵션 (boolean)

​    

#### 6. enabled / refetch

```jsx
const { data, refetch } = useQuery([], Fn, {
  enabled: false
})

return <button onClick={() => { refetch() }}>버튼</button>
```

- 자동으로 쿼리를 요청하지 않고, 버튼 클릭이나 특정 이벤트 발생시에 요청을 시도할 때 같이 사용
- `enabled` : false상태일 때, 쿼리가 자동으로 실행되지 않도록 설정
- `refetch` : 쿼리를 수동으로 다시 요청하는 기능

​    

#### 7. retry

- boolean | number
- `false` : 실패한 쿼리는 다시 시도하지 않음
- `true` : 실패한 쿼리를 무한 재요청
- `number`(숫자값) : 수만큼 실패한 쿼리 재요청
- 기본값 : 3회 실행

​    

#### 8. onSuccess / onError / onSettled

```js
const onSuccess = (data) => { console.log("Success", data) }
const onError = (error) => { console.log("Error", error) }
const onSettled = () => { console.log("Settled") }

const { data } = useQuery([''], Fn, {
  onSuccess,
  onError,
  onSettled,
})
```

- `onSuccess` : 쿼리 요청이 성공적으로 진행되어 새 데이터를 가져오거나 캐시가 업데이트 될 때 마다 실행되는 함수
- `onError` : 쿼리에 오류가 발생했을 때 실행되는 함수
- `onSettled` : 쿼리 요청이 진행됐을 때, 결과가 실패, 성공 가릴 거 없이 실행되는 함수

​    

#### 9. select

```js
const { data } = useQuery([''], Fn, {
  select(data) {
    const newData = data.data.map(el => el.attr)
    return newData
  }
})
```

- 쿼리에서 반환된 데이터의 일부를 변환하거나 선택할 수 있는 함수

​    

#### 10. keepPreviousData / isPreviousData

```js
const { data, isPreviousData } = useQuery([], Fn, {
  keepPreviousData: true
}) 
```

- `keepPreviousData`
  - `true`로 설정시 쿼리키가 변경되어 새 데이터를 요청하는 동안 마지막 데이터값을 유지해줌	
  - 페이지네이션 구현시, 캐싱되지 않은 페이지를 가져올 때 목록이 깜빡이는 현상을 방지할 수 있음
- `isPreviousData`
  - 현재 쿼리키에 해당하는 값인지 확인가능
  - 새로운 데이터 아직 캐싱되지 않았으면 이전데이터이므로 `true` 를 반환
  - 새로운 데이터를 정상적으로 받아왔다면 `false`반환

​    

### Dependent Queries

- 동기적으로 처리되어야하는 상황에서 먼저 값을 결과에 종속되는 쿼리를 종속쿼리하고 함
- `enabled` 옵션을 통해 구현가능

```js
const { data: product } = useQuery(['product'], Fn)
const productId = product?.data.productId

// product 쿼리의 결과에 종속된 종속 쿼리
const { data } = useQuery([''], Fn1(productId), {
  enabled: !!productId ✔️✔️ ❗❗// 이해가 잘 안됨..
})
```

​    

---

## 5️⃣ `UseMutation`

- 서버의 데이터를 post, put, patch, delete 할때 사용 (CUD)

```js
const Fn = async (obj) => {
  const { data } = await axios({
    method: 'post',
    url: '/',
    data: obj
  })
  return data
} 

const mutation = useMutation({ mutationFn: Fn })
```

​    

### return

- `mutate: (variables: TVariables, { onSuccess, onSettled, onError }) => void`:
  - mutate를 호출해서 mutation을 실행시킬 수 있음
  - variables 는 mutationFn에 전달하는 객체
- `mutateAsync: (variables: TVariables, { onSuccess, onSettled, onError }) => Promise<TData>` 
  -  Promise형태의 response가 필요할 때 사용
- 나머지는 useQuery와 유사

​    

### options

```js
const mutation = useMutation({
  mutationFn: Fn,
  options: {
    onSuccess: (data) => {},
    onError: (error) => {},
    onSettled: () => {},
    onMutate: () => {}
  ...
	}
})
```

- `onSuccess / onError` : 성공 / 실패시 response 데이터를 핸들링할 수 있음
- `onSettled` : 요청이 성공하든 실패하든 상관없이 마지막에 실행되는 구문
- `onMutate`: `mutationFn`이 실행되기 전에 실행되는 구문, `mutationFn`에 사용되는 변수를 받을 수 있음

###     

---

## 6️⃣ Parallel (`useQueries`)

```js
const { data: Data1 } = useQuery([''], Fn1)
const { data: Data2 } = useQuery([''], Fn2)
const { data: Data3 } = useQuery([''], Fn3)
```

- 쿼리가 여러개 선언되면 일반적으로 병렬로 요청되어 처리됨 
- 동시성이 좋다
- 동기적으로 처리해야하면 `useQueries`를 사용해야함

```js
const results = useQueries({
  quries: [
    { queryKey: ['a'], queryFn: Fn1 },
    { queryKey: ['b'], queryFn: Fn2 },
    { queryKey: ['c'], queryFn: Fn3 },
  ]
})
```

- return값으로 쿼리결과가 포함된 배열을 반환

​    

---

## 7️⃣ Infinite Queries (`useInfiniteQuery`)

- 무한스크롤, 더보기등과 같이 특정 조건에서 데이터를 추가적으로 받아오는 기능을 구현할 때 사용
- `useInfiniteQuery`를 통해 구현한다.

```jsx
import { useInfiniteQuery } from 'react-query' // v3 
import { useInfiniteQuery } from '@tanstack/react-query' // v4

const queryPage = ({ pageParam = 1 }) => {
  return axios.get(`${pageParam}`)
}

const { data, fetchNextPage, isFetchingNextPage, ... } = useInfiniteQuery({
  queryKey: [''],
  queryFn: queryPage,
  options: {
  	getNextPageParam: (lastPage, allPages) => lastPage.nextCursor,
  	getPreviousPageParam: (firstPage, allPages) => firstPage.prevCursor,
  }
})
```



### 반환값

- useQuery와의 차이점으로는 몇가지 반환값이 추가적으로 있음
  - `fetchNextPage` : 다음페이지 fetch
  - `fetchPreviousPage` : 이전페이지 fetch
  - `isFetchingNextPage` : 다음 페이지를 fetching하는 동안 `true`
  - `isFetchingPreviousPage` : 이전 페이지를 fetching하는 동안 `true`
  - `hasNextPage` : 가져올 수 있는 다음페이지가 있을 경우 `true`
  - `hasPreviousPage ` : 가져올 수 있는 이전 페이지가 있을 경우 `true` 

​    

### 옵션

#### pageParam

- `pageParam`이라는 프로퍼티가 존재하며, `queryFn`에 할당해줘야함
- 단순히 다음 page값만 관리할 수 있는 것은 아니고, `getNextPageParam`을 통해 원하는 형태로 변환한 후 `qeuryFn`에서 그 값을 받아올 수 있음

```js
const { data } = useInfiniteQuery([""], Fn, {
	getNextPageParam: (lastPage, allPages) => {
    return {
      page: allPage.length + 1
      etc: "very good"
    }
  }
})

const fetchData = ({ pageParam }) => {
  const { page=1, etc } = pageParam  ✔️✔️
  return axios.get()
}
```



#### getNextPageParam /  getPreviousPageParam

- 주로 페이지를 증감 시킬때 사용
- `getNextPageParam `
  - `lastPage` : 첫 번째 인자, 가장 최근에 fetch해온 페이지
  - `allPages` : 두 번째 인자, 현재까지 가져온 모든 페이지 데이터
- `getPreviousPageParam`
  - `firstPage` : 첫 번째 인자
  - `allPages` : 두 번째 인자

​    

#### refetchPage

- 전체 페이지 중 일부만 직접 refetch하고 싶을때 사용
- `refetchPage`는 각 페이지에 대해 실행되며, `true`를 반환하는 페이지만 refetch됨
- `refetchPage: (page: TData, index: number, allPages: TData[]) => boolean`

```js
const { refetch ✔️✔️ } = useInfiniteQuery([''], Fn, {
  getNextPageParam: (lastPage, allPages) => {
    return lastPage.nextCursor
  }
})

refetch({ refetchPage: (page, index) => index === 0 })  ✔️✔️
```

​    
