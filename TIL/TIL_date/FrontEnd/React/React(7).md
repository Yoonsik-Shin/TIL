# React (7)



## 1️⃣ 최근 본 상품

```jsx
useEffect(() => {
  let watched = localStorage.getItem('watched')
  watched = JSON.parse(watched)
  watched.push(product.id)
  
  // Set으로 중복제거한 후 다시 array로
  watched = new Set(watched)
  watched = Array.from(watched)
  localStorage.setItem('watched', JSON.stringify(watched))
}, [])
```

​    

---

## 2️⃣ 댓글

### 댓글 생성

```jsx
const COMMENTS_INPUTS = [
  { id: "writer", type: "text" },
  { id: "title", type: "text" },
  { id: "contents", t  ype: "text" },
]

export default function CreateComment() {
  const [inputs, setInputs] = useState({
    writer: "",
    title: "",
    contents: "",
  })
  
  const onClickSubmit = async () => {
    const result = await axios({
      method: 'post',
      url: 'https://~',
      data: { ... inputs }  ✔️✔️
    })
  }
  
  const onChangeInputs = (e) => {
    setInputs({
      ...inputs,
      [e.target.id]: e.target.value
    })
  }
  
  return (
  	<>
    	{COMMENTS_INPUTS.map((el) => (
    		<input id={el.id} type={el.type} onChange={onChangeInputs} />
  		)}
    	<button onClick={onClickSubmit}>댓글 생성</button>
    </>
  )
}
```

​    

### 댓글 수정

```jsx
import CommentItem from './'

export default function CommentPage() {
  const [data, setData] = useState()
  
  return(
  	<>
    	{data.map((el) => {
	  		<CommentItem key={el.id} el={el} />  
 		  })}
    </>
  )
}
```

```jsx
export default function CommentItem(props) {
  const [isEdit, setIsEdit] = useState(false)
  const onClickEdit = () => { setIsEdit(true) }
  
  return (
  	<>
    	{!isEdit && (
  				<div>{props.el.comment}</div>
					<button onClick={onClickEdit}>수정하기</button>
  		)}
			{isEdit && (
      	<div>
        	댓글수정: <input type="text" />
        </div>
      )}
    </>
  )
}
```

​    

---

## 3️⃣ 페이지네이션

- 페이지 번호를 클랙해서 이동하는 방식의 페이지 처리 방법

​    

### 1. offset 방식

#### RestAPI

```jsx
export default function Pagination() {
  const [data, setData] = useState([]) 
  const [startPage, setStartPage] = useState(1)
  const [page, setPage] = useState(1)
  const [lastPage, setLastPage] = useState(0)
  const [activedPage, setActivedPage] = useState(1)  // 현재 선택된 페이지
  const limit = 10
  
  // 데이터 불러오기
  const fetchData = async () => {
    const result = await axios.get() 
    setData(result.data) 
  }
  
  // 데이터 총개수 불러오기
  const fetchDataCount = async () => { 
    const result = await axios.get() 
    setLastPage(Math.ceil(result.data / limit))  // 마지막 페이지 계산
  }
  
  // 페이지별로 데이터 불러오기
  const onClickPage = (e) => { setPage(Number(e.currentTarget.id)) }
  
  // 이전 목록번호
  const onClickPrevPage = () => {
    if (startPage === 1) return 
    setStartPage((prev) => prev - 10);
    setPage(startPage - 10);
  }
  // 이후 목록번호
  const onClickNextPage = () => {
    if (startPage + 10 <= lastPage) {
      setStartPage((prev) => prev + 10);
      setPage(startPage + 10);
    }
  };  
   
  useEffect(() => {
    fetchData()  // 데이터 불러오기
    fetchDataCount()  // 데이터 총개수 불러오기
  }, [page])
  
  return (
  	<span onClick={onClickPrevPage}>이전</span>
    {new Array(10).fill(1).map(_, index)=> {
    	return (
      	index + startPage <= lastPage && (
        	<Page 
            id={String(index + startPage)} 
            onClick={onClickPage} 
            isActive={index + startPage === activedPage}
          >
          	{index + startPage}
          </Page>
        )
      )
  	}}
    <span onClick={onClickNextPage}>이후</span>
  )
}
```

​     

#### grapql

```jsx
export default function Pagination() {
  const [startPage, setStartPage] = useState(1)
  const { data, refetch } = useQuery()
  const lastPage = Math.ceil(전체데이터갯수 / 한페이지에 들어갈 데이터개수)
  
  const onClickPage = (e) => { void refetch({ page: Number(e.currentTarget.id) }) }
  const onClickPrevPage = () => { 
  	if (startPage === 1) return
    setStartPage((prev) => prev - 10);
    void refetch({ page: startPage - 10 })
  }
  const onClickNextPage = () => {
    if (startPage + 10 <= lastPage) {
      setStartPage((prev) => prev + 10)
      void refetch({ page: startPage + 10 })
    }
  }
  
  return (
  	<>
    	// 이전 1 2 3 4 5 6 7 8 9 10 이후
    	<span onClick={onClickPrevPage}>이전</span>
    	{new Array(10).fill(1).map(_, index) => {
    		return (
        	index + startPage <= lastPage && (
          	<span key={index + startPage} id={String(index + startPage)} onClick={onClickPage}>
            	{index + startPage}
            </span>
          )
        )
  		}}
    	<span onClick={onClickNextPage}>이후</span>
    </>
  )
}
```

​    

---

##  4️⃣ 무한스크롤

### [intersection Observer](https://developer.mozilla.org/ko/docs/Web/API/Intersection_Observer_API)

- 비동기적으로 동작

```tsx
interface IntersectionObserverInit {
   root?: Element | Document | null;
   rootMargin?: string;
   threshold?: number | number[];
}
const options: IntersectionObserverInit = {
  root: ,
  rootMargin: ,
  threshold:
}

// 관찰되고 있는 요소가 보여지면 실행될 함수
const callback = (entries, observer) => {
  entries.forEach(entry => {
    entry.boundingClientRect  // 관찰되는 대상의 정보반환
    entry.intersectionRect  // root 영역과 교차된 지점의 정보 반환
    entry.intersectionRatio  // root 영역과 교차된 지점비율 반환 (threshold와 유사, 0.0 ~ 1.0)
    entry.isIntersecting  // 교차되어 있는지 여부를 반환 (true/false)
    entry.rootBounds  // root 정보반환 
    entry.target  // 관찰되는 대상 자체를 반환
    entry.time  // 교차가 시작된 시간 반환
  })
}

const observer = new IntersectionObserver(callback, options)
observer.observe(요소)  // 관찰되는 대상이 됨
observer.unobserve(요소)  // 관찰되는 대상에서 해제됨
observer.disconnect()  // 관찰되는 모든 요소 관찰해제
observer.takerecords()  // 관찰되는 요소들을 배열로 리턴
```



#### options

- `root`
  - null 입력시, 기본값으로 브라우저의 __Viewport__로 설정
- `rootMargin`
  - root에 마진값을 추가하여 root의 범위를 확장할 수 있음 
  - 기본값 : `0px 0px 0px 0px`
  - 단위 반드시 입력해야함
- `threshold`
  - 콜백함수가 실행되기 위해 관찰될 요소의 보여지는 정도를 백분율로 표기
  - 기본값 : 0

​    

#### custom Hook만들기

```tsx
type IntersectHandler = (
 entry: IntersectionObserverEntry,
 observer: IntersectionObserver
) => void

interface IntersectionObserverInit {
   root?: Element | Document | null;
   rootMargin?: string;
   threshold?: number | number[];
}
 
export const useIntersect = (
 onIntersect: IntersectHandler,
 options?: IntersectionObserverInit
) => {
 const ref = useRef<HTMLDivElement>(null)
 const callback = useCallback(
   (entries: IntersectionObserverEntry[], observer: IntersectionObserver) => {
     entries.forEach((entry) => {
       if (entry.isIntersecting) onIntersect(entry, observer)
     })
   },
   [onIntersect]
 )
 
 useEffect(() => {
   if (!ref.current) return
   const observer = new IntersectionObserver(callback, options)
   observer.observe(ref.current)
   
   return () => observer.disconnect()
 }, [ref, options, callback])
 
 return ref
}
```



#### 구현

​    

### react-intersection-observer

​    

### [react-ininite-scroller](https://www.npmjs.com/package/react-infinite-scroller?activeTab=readme)

#### graphql

- 브라우저 스크롤 기준

```bash
$ yarn add react-infinite-scroller
$ yarn add --dev @types/react-infinite-scroller
```

```jsx
import InfiniteScroll from 'react-infinite-scroller'

export default function InfiniteScrollPage() {
  const { data, fetchMore } = useQuery()
  
  const onLoadMore = () => {
    void fetchMore({
      variables: { page: Math.ceil(데이터개수 / 데이터묶음수) + 1 },  // 다음페이지
      updateQuery: (prev, { fetchMoreResult }) => {
        if (!fetchMoreResult)  // 새로 받아온 데이터가 없으면
          return {
            쿼리: [...prev]  
          }
      	return {  // 데이터 새로 받아왔을때
          쿼리: [...prev ...fetchMoreResult]
        }
    	}
    })
  }
  
  return (
    <InfiniteScroll 
      pageStart={0}  // 시작페이지
      loadMore={onLoadMore}  // 새로운 데이터를 요청보내는 함수
      hasMore={true}  // hasMore가 true일때만 loadMore가 실행됨
    >
      {data.map((el) => {
        // 무한스크롤 될 요소들
      })}
    </InfiniteScroll>
  )
}
```

