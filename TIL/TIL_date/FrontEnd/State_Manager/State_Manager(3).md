# React-query (2)

​    



## QueryClient

- 캐시와 상호작용

```js
import { QueryClient } from "@tanstack/react-query";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: Infinity,
    },
  },
});

```

​    

### Option

1. defaultOption
   - 모든 query와 mutation에 대한 기본값을 정의
   - 자주사용됨
2. queryCache : query 캐시
3. mutationCache: mutation 캐시
4. logger : 디버깅 정보, 경고, 오류등을 기록하는데 사용되는 로거 설정

​    

### useQueryClient

- `QueryClient` 인스턴스를 반환
- QueryClient 옵션을 이용할 때 이 hook을 사용함

```js
import { useQueryClient } from '@tanstack/react-query'

const queryClient = useQueryClient()
```

​    

### getQueryData / getQueriesData

- 기존 쿼리의 캐시 데이터를 가져오는 동기함수
- getQueryData : 일치하는 쿼리가 없으면 `undefined` 반환
- getQueriesData : 일치하는 쿼리가 없으면 `[]` 반환

```js
// getQueryData 
// v3
const data = queryClient.getQueryData(queryKey)

// v4
const data = queryClient.getQueryData({ queryKey })

// getQueriesData
// v3 & v4
const data = queryClient.getQueriesData(queryKey) 
const data = queryClient.getQueriesData(filters) 
```

​    

### setQueryData / setQueriesData

- 캐싱된 쿼리 데이터를 즉시 업데이트하는데 사용되는 동기함수
- 캐시 데이터 최신화시 사용

```js
// setQueryData 
// v3 & v4
queryClient.setQueryData([''], (prev) => {
  return {
    ...prev,
    data: [...prev.data, newData.data]
  }
})

// setQueriesData
// v3 & v4
queryClient.setQueriesData([''], (prev) => {
  return {
    ...prev,
    data: [...prev.data, newData.data]
  }
})
```

​    

### invalidateQueries

- 쿼리 무효화
- 화면을 최신 상태로 유지하는 가장 간단한 방법
- 쿼리가 오래되었다고 판단하고 다시 refetch할 때 사용
- 캐시데이터를 최신화할 때 사용
- 파라미터로 넣어준 쿼리를 무효화(stale처리)하고 다시 가져오는데 많이 사용됨
- ❗`enabled: false` 옵션이 있으면 무시됨

```js
// v3
await queryClient.invalidateQueries([""], {
    exact,
    refetchActive: true,
    refetchInactive: false,
	}, { throwOnError, cancelRefetch }
)

// v4
await queryClient.invalidateQueries({
  queryKey: [''],
  refetchType: 'none'  // 'active' | 'inactive' | 'all' | 'none'
}, { throwOnError, cancelRefetch })
```

- 기본적으로 지정한 쿼리의 하위 쿼리들을 모두 초기화됨 

```js
queryClient.invalidateQueries({
  queryKey: ["posts"],
});

["posts"],
["posts", 'abc'],
["posts", { id: 1 } ]
```

- 하위 쿼리를 제외하고, 해당 쿼리만 무효화 시키려면 `exact`옵션 부여

```js
// v4
await queryClient.invalidateQueries({
  queryKey: [''],
  refetchType: 'active' 
  exact: true  ✔️✔️
})
```

- `refetchType`의 기본값은 
  - `active` : 기본값, ???
  - `inactive` : ???
  - `all` : 일치하는 모든 쿼리가 refetch되어 백그라운드로 가져옴
  - `none` : 쿼리가 refetch되지 않고, 쿼리를 무효화만함

```bash
# 원문 해석이 잘 안됨
When set to active, only queries that match the refetch predicate and are actively being rendered via useQuery and friends will be refetched in the background.

When set to inactive, only queries that match the refetch predicate and are NOT actively being rendered via useQuery and friends will be refetched in the background.

When set to all, all queries that match the refetch predicate will be refetched in the background.

When set to none, no queries will be refetched, and those that match the refetch predicate will be marked as invalid only.
```

```js
// 예시
import { useMutation, useQuery, useQueryClient } from "react-query";

const queryClient = useQueryClient();
const addPost = () => {
  const { data } = axios.post('/', data)
  return data
}

useMutation({
  mutationFn: addPost,
  options: {
     onSuccess: (data) => {
      queryClient.invalidateQueries(["a", "b", "c"]); // 이 key에 해당하는 쿼리가 무효화
    }
  }
})
```

​    

### refetchQueries

- 특정 조건에 따라 쿼리를 다시 가져오는 함수
- ❗`enabled: false` 옵션이 있으면 무시됨 

```js
// v3 & v4
// 모든 쿼리 다시 가져오기
await queryClient.refetchQueries()

// 모든 stale 상태의 쿼리 다시 가져오기
await queryClient.refetchQueries({ stale: true })
```

```js
// v3
// 해당 쿼리키와 연관된 모든 활성 쿼리를 다시 가져옴
await queryClient.refetchQueries([''], { active: true });

// exact 옵션 추가시, 정확히 일치하는 쿼리만 다시 가져옴
await queryClient.refetchQueries(['', 1], {
  active: true,
  exact: true
})

// v4
// 해당 쿼리키와 연관된 모든 활성 쿼리를 다시 가져옴
await queryClient.refetchQueries({
  queryKey: [''],
  type: "active",
})

// exact 옵션 추가시, 정확히 일치하는 쿼리만 다시 가져옴
await queryClient.refetchQueries({
  queryKey: ["", 1],
  type: "active",
  exact: true,
}, { 
  throwOnError, 
  cancelRefetch 
})
```

​    

### cancelQueries

- 통신중인 쿼리를 수동적으로 취소할 수 있는 함수
- 요청이 완료되는데 너무 오래 걸려 사용자가 취소 버튼을 누른 경우
- 요청이 완료되지 않았는데 페이지를 벗어나 중간에 더 이상 요청이 필요 없어진 경우
- 낙관적 업데이트에 사용됨

```js
// v3
await queryClient.cancelQueries([''], { exact: true })

// v4
await queryClient.cancelQueries({ 
  queryKey: [''], 
  exact: true 
})
```

```js
// 예시
const query = useQuery(['too-slow'], Fn)
const queryClient = useQueryClient()

// 쿼리를 취소하는 동작
const onCancelQuery = (e) => {
  e.preventDefault()
  queryClient.cancelQueries(['too-slow'])
}
```

​    

#### Optimistic Update

- 낙관적 업데이트
- 서버에서 업데이트될 시 UI도 업데이트 될 것을 가정하여 UI를 먼저 업데이트 시키고, 나중에 서버를 통해 검증을 받은 후 업데이트하거나 롤백하는 방식
- 인터넷이 느리거나 서버가 느려도 사용자는 바로바로 처리해주는 것 처럼 여기게 해줘 UX 측면에서 좋음

​    

### removeQueries

- 캐시를 제거할 때 사용하는 함수

```js
// v3
queryClient.removeQueries([''], { exact: true })

// v4
queryClient.removeQueries({ 
  queryKey: [''],
  exact: true 
})
```

​    

### resetQueries

- 캐시 쿼리를 초기상태로 재설정하는데 사용하는 함수
- `initial`데이터가 있다면 해당 데이터로 재설정됨

```js
// v3
queryClient.resetQueries([''], { exact: true })

// v4
queryClient.resetQueries({ 
  queryKey: [''],
  exact: true 
})
```

​    

### clear

- 연결된 모든 캐시 제거

```js
queryClient.clear();
```

​    

---

## 기타

### Initial Query Data

- 데이터 fetch 전에 캐시에 미리 초기값을 넣어두는 것
- 