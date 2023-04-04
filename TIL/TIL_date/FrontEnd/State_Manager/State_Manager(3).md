# React-query (2)

​    

## useQueryClient

- `QueryClient` 인스턴스를 반환
- QueryClient는 캐시와 상호작용함

```js
import { useQueryClient } from '@tanstack/react-query'

const queryClient = useQueryClient()
```







## 기타

### Initial Query Data



### `cancelQueries`

- 쿼리를 수정으로 취소시키고 싶을 경우 사용
- 요청이 완료되는데 너무 오래 걸려 사용자가 취소 버튼을 누른 경우
- 요청이 완료되지 않았는데 페이지를 벗어나 중간에 더 이상 요청이 필요 없어진 경우

```js
const query = useQuery(['too-slow'], Fn)
const queryClient = useQueryClient()

// 쿼리를 취소하는 동작
const onCancelQuery = (e) => {
  e.preventDefault()
  queryClient.cancelQueries(['too-slow'])
}
```

​    



### 쿼리 무효화 (`invalidateQueries`)

- 화면을 최신 상태로 유지하는 가장 간단한 방법
- 쿼리가 오래되었다고 판단하고 다시 refetch할 때 사용
- `invalidateQueries`메소드 활용

```js
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

### 캐시데이터 즉시 업데이트

​    

### Optimistic Update

- 낙관적 업데이트
- 서버에서 업데이트될 시 UI도 업데이트 될 것을 가정하여 UI를 먼저 업데이트 시키고, 나중에 서버를 통해 검증을 받은 후 업데이트하거나 롤백하는 방식
- 인터넷이 느리거나 서버가 느려도 사용자는 바로바로 처리해주는 것 처럼 여기게 해줘 UX 측면에서 좋음



​    

## React Query Typescript