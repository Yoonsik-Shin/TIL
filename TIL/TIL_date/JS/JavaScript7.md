# JavaScript 정리 (7)



## AJAX (Asynchronous JavaScript And XML)

- 비동기식 JS와 XML



## API (Application Programming Interface)

- 여러 SW가 상호작용하거나 소통하는 모든 인터페이스를 의미



## WebAPI

- 웹, HTTP를 기반으로 하는 인터페이스



## XML (eXtensible Markup Langauge)

- 확장성이 있는 마크업 언어
- 요새는 보기힘듬



## JSON (JavaScript Object Notation)

- JS 객체 문법
- 계속해서 데이터를 전송하거나 정보를 전송하는 포맷
- JS와 1:1 대응 안됨 ❗❗
- 큰따옴표만 사용 [`""`]

> [JSON문서](https://www.json.org/json-ko.html)
>
> [JSON문 고쳐주는 사이트](https://jsonformatter.curiousconcept.com/)

```json
data = {
  "A": 1,
  "B": "banana",
  "C": ["apple", "pineapple"]
  "D": true
  "E": null
  "F": {"a": 1, "b":2, "c":3}
	// undefined는 안됨
}
```

### JSON.parse() ✔️✔️

- 문자열을 전달하면 파싱되어 JS객체로 변환

```javascript
JSON.parse(text[, reviver])
```

```javascript
const parsedData = JSON.parse(data)
parsedData.C.b
>> 2
```

### JSON.stringify()

- JS 객체를 JSON으로 변환할 경우 사용
- JSON형식의 데이터를 받는 API에 정보를 보낼 때
- `undefined` 값은 모두 `null`값으로 바뀜

```javascript
JSON.stringify(value[, replacer[, space]])
```



## HTTP 동사 (Verbs)

### GET

- 정보를 가져올 때 사용

### POST

- 데이터를 어딘가로 보낼 때 사용



## HTTP 상태코드 (State Codes)

- 200번대 : 일반적으로 문제가 없을 때의 상태코드 (성공적인 응답)
- 300번대 : 리디렉션(Redirect)과 연관
- 400번대 : 클라이언트 사이드 오류시
  - 404
  - 405
- 500번대 : 서버 사이트 오류시 (API쪽 문제)



## 쿼리 문자열 (Query Strings)

- url에 추가 정보 넣기
- 키-값 쌍으로 작성
- `&`로 구분
- 대부분의 API들은 쿼리 문자열 무시

```http
?sort=desc&color=blue
```



## HTTP 헤더 (Headers)

- 요청과 함께 정보를 전달하는 부수적인 방식으로 응답에 포함
- 메타데이터
- 개발자 도구로 확인가능 (`Network`)
- 일부 API는 요청과 함께 특정 헤더나 여러 헤더를 보내야함



## XHR (XMLHttpRequest)

- JS에서 요청을 보내는 기존 방식으로 `promise`를 지원하지 않아 요새는 잘 안쓰임 ❌

```javascript
const req = new XMLHttpRequest();

req.onload = function () {
  console.log("LOAD");
  const data = JSON.parse(this.responseText);
  console.log(data. , data. );
}

req.onerror = function () => {
  console.log("ERROR");
  console.log(this); 
}

req.open("GET", "URL");
req.send();
```



## Fetch API

- `fetch`함수를 호출하면 `Promise`가 반환됨
- JSON을 따로 구문 분석하여 또 다른 프로미스로 반환해야함

```javascript
const load = async () => {
  try {
    const res = await fethch("URL");
    const data = await res.json();
    console.log(data);
	} catch (e) {
    console.log("ERROR", e);
  }
};

load();
```



## Axios

> https://axios-http.com/kr/

- JS 라이브러리의 함수
- JS 내장함수가 아님 (import 필요)
- HTTP요청의 생성과 처리를 최대한 간소화할 목적으로 만들어짐
- JSON을 구문 분석하고 그 결과가 `data`에 나옴

> jsDelivr CDN 사용하기

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

```javascript
axios.get("URL");  // Promise 반환
  .then((res) => {
    console.log("RESPONSE", res);
  })
	.catch((e) => {
    console.log("ERROR", e);
  });
```

```javascript
const get = async () => {
  try{
    const res = await.axios.get("URL");
    console.log(res.data);
  } catch(e) {
    console.log("ERROR", e);
  }
};
  
get();
```

