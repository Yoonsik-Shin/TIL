# React (9)

​    

## 댓글 수정



## 페이지네이션

- 페이지 번호를 클랙해서 이동하는 방식의 페이지 처리 방법



```jsx

```



##  무한스크롤

react-ininite-scroller





## 검색

### 디바운싱 (Debouncing)

- 마지막 입력을 기준으로, 특정 시간 이내에 추가 입력이 없으면 1번 실행하는 것
- 반복적인 동작을 강제적으로 대기하는 것을 의미
- 마지막 한번 요청
- 검색시 엔터를 치지 않아도 사용자 입력이 멈추고 일정시간이 지났을 때 자동으로 함수를 실행시켜 결과를 보여줌

> `lodash`라이브러리의 `debounce()` 함수 사용

```js
_.debounce(() => {
  실행될 이벤트
}, 시간) // 이 시간동안 아무일도 일어나지 않으면 위에 이벤트 실행
```

```js
import { debounce } from 'lodash'

export default function Page() {
  const getDebounce = _.debounce((value) => {
    // refecth 요청
    void refetch({ search: value, page: 1 })  // graphql
  }, 400)
  
  const onChangeSearch = (e: ChangeEvent<HTMLInputElement>) => {
    getDebounce(e.target.value)
  }
}
```

​    

### 검색 키워드 강조

```jsx
const [keyword, setKeyword] = useState('')

const getDebounce = _.debounce((value) => {
    // refecth 요청
    void refetch({ search: value, page: 1 }
  	setKeyword(value)  ✔️✔️
  }, 400)

const onChangeSearch = (e: ChangeEvent<HTMLInputElement>) => {
    getDebounce(e.target.value)
}

return (
	<>
  	<input type="text" onChange={onChangeSearch} />
  	{result.data.map((el) => (
			<div key={el.id}>
  			<span>{el.내용1}</span>
 				<!-- 검색 키워드 강조 시작 -->
		    <span>
          {el.내용2
          	.replaceAll(keyword, `%$#@!${keyword}%$#@!`)
           	.split('%$#@!')
           	.map((el) => (
            	<span key={uuid4()}>{el}</span>
          	))}
        </span>
    		<!-- 검색 키워드 강조 끝 -->
  		</div>	
		))}
  </>
)
```

​    

### 쓰로틀링 (Throttle)

- 최초 입력을 기준으로, 특정 시간 이내에 발생한 추가 입력을 무시하는 것
- 먼저 한번 요청
- 무한스크롤



## 지도

##  