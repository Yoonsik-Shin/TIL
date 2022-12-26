# HTTP (1)



## IP (인터넷 프로토콜)

- 특정 IP주소에 데이터 전달
- 통신 단위 : 패킷(Packet) 

### 한계

- 비연결성 : 패킷을 받을 대상이 없거나 서비스 불능이어도 패킷을 전송함
- 비신뢰성 : 중간에 패킷이 소실되거나, 순서가 바뀔 가능성이 있음
- 프로그램 구분 : 같은 IP를 사용하는 애플리케이션이 둘 이상일 경우 구분 힘듬

​    

---

## TCP (UDP)

### TCP/IP 프로토콜

1. 애플리케이션 계층 : HTTP, FTP
2. 전송 계층 : TCP, UDP
3. 인터넷 계층 : IP
4. 네트워크 인터페이스 계층

​    

### TCP 특징

- 전송 제어 프로토콜 (Transmission Control Protocol)
- 연결지향 : TCP 3way handshake
- 데이터 전달 보증 : 데이터를 잘 받았는지 확인해줌
- 순서 보장 : 순서가 잘못됬을 때, 잘못된 부분부터 다시 전송요청
- 신뢰할 수 있는 프로토콜

​    

### UDP 특징

- 사용자 데이터그램 프로토콜 (User Datagram Protocol)
- 기능 거의 없음 (하얀 도화지)
- 연결지향 x
- 데이터 전달 보증 x
- 순서 보장 x
- 단순하고 빠름
- IP와 거의 같음 (PORT와 체크섬 정도만 추가됨)
- 애플리케이션에서 추가 작업 필요

​    

---

## PORT

- 같은 IP내에서 프로세스 구분
- IP는 아파트 PORT는 몇동 몇호
- 할당 가능한 포트 : 0 ~ 65535
- 잘 알려진 포트 : 사용하지 않는 걸 추천
  - FTP : 20, 21
  - TELNET : 23
  - HTTP : 80
  - HTTPS : 443

​    

## DNS

- 도메인 네임 시스템 (Domain Name System)
- 도메인명을 IP주소로 변환

​    

### 사용이유

- IP는 기억하기 힘듬
- IP는 변경될 수 있음

​    

---

## URI (Uniform Resource Identifier)

- Uniform : 리소스를 식별하는 통일된 방식
- Resource : 자원 / URI로 식별할 수 있는 모든 것
- Identifier : 다른 항목과 구분하는데 필요한 정보

​    

### URN : Resource Name

- 리소스에 이름을 부여
- urn:example:animal:ferret:nose
  - scheme : urn
  - path : example:animal:ferret:nose
- 거의 사용x

​       

### URL(Resource Locator)  

- 리소스가 있는 위치를 지정

- foo://example.com:8042/over/there?name=ferret#nose

  - scheme : foo
  - authority : example.com:8042
  - path : over/there
  - query : ?name=ferret
  - fragment: #nose

- 전체문법

  - `scheme://[userinfo@]host[:port][/path][?query][#fragment]`
  - `https://www.google.com:443/search?q=hello&hl=ko`
  - 프로토콜 : `https`
    - 어떤 방식으로 자원에 접근할 것인가? (http, https, ftp, ...)
    - http : 80포트 / https : 443포트
  - userinfo : URL에 사용자정보를 포함하여 인증 (거의 사용x)
  - 호스트명 : `www.google.com`
    - 도메인명 or IP주소
  - 포트번호 : 443
    - 접속포트
    - 일반적으로 생략가능
  - 패스 : `/search`
    - 리소스 경로
    - 계층적구조 (/members/100)
  - 쿼리 파라미터 : `key1=value1&key2=value2`
    - key = value 형태
    - `?`로 시작
    - `&`로 추가가능
    - query string, query parameter로 불림
    - 웹서버에 제공하는 파라미터

  - fragment
    - html 내부 북마크등으로 활용
    - 서버에 전송하는 정보 아님



---

## HTTP (HyperText Transfer Protocol)

- 거의 모든 형태의 데이터 전송 가능

역사 

- HTTP/0.9 (1991년) : GET 메서드만 지원, HTTP 헤더 X
- HTTP/1.0 (1996년) : 메서드, 헤더추가
- __HTTP/1.1 (1997년) : 가장 많이 사용__
  - RFC2068 >> RFC2616 >> __RFC7230~7235__
- HTTP/2 (2015년) : 성능개선
- HTTP/3 (진행중) : TCP 대신 UDP 사용 (성능개선)

> TCP : HTTP/1.1, HTTP/2
>
> UDP : HTTP/3

특징

- 클라이언트 서버 구조
- 무상태 프로토콜 (stateless)
  - 서버가 클라이언트의 상태를 보존하지 않음
  - 서버의 확장성이 높음, 수평확장에 유리함(스케일아웃) [장점]
  - 클라이언트가 추가 데이터를 더 많이 사용해야함 [단점]
  - 모든 것을 무상태로 설계할 수는 없다.
    - ex) 로그인은 쿠키나 세션등을 이용하여 상태 유지를 해야함
- 비연결성 (connectionless)
  - HTTP는 기본적으로 연결을 유지하지 않는 모델
  - 초단위 이하의 빠른 속도로 응답
  - 다수의 사람들이 서비스를 이용하여도 실제 서버에서 처리되는 요청은 별로 안됨 [장점]
  - 항상 새로운 TCP/IP 연결을 맺어야해 시간이 추가됨 [단점]
  - 요청시 수많은 자원을 함께 다운로드해야함 [단점]
  - HTTP 지속 연결(Persistent Connections)로 문제를 해결함
- HTTP 메시지
  - HTTP 메시지에 모든 것을 전송함
- 단순함
- 확장 가능



HTTP 요청 메시지

```http
GET /search?q=hello&hl=ko HTTP/1.1  << start-line
Host: www.google.com  << HTTP Header
```

- start-line : request-line
- request-line : `method 공백 request-target 공백 HTTP-version CRLF(엔터)`
  - method : HTTP 메서드 (GET, POST, PUT, DELETE)
  - request-target : 요청대상
    - absolute-path[?query] : 절대경로[?쿼리]
    - `/`로 시작하는 경로
  - HTTP-version : HTTP 버전

HTTP 응답 메시지

```http
HTTP/1.1 200 OK  << start-line
Content-Type: text/html;charset=UTF-8  << HTTP Header
Content-Length: 3423  << HTTP Header

<html>
	<body>...</body>
</html>
```

- start-line : status-line
- status-line = `HTTP-version 공백 status-code 공백 reason-phrase CRLF`
  - HTTP-version : HTTP 버전
  - status-code : HTTP 상태코드
  - reason-phrase : 이유 문구 : 사람이 이해할 수 있는 짧은 상태코드 설명글

​        

HTTP 헤더

- header-field = field-name":" OWS field-value OWS (OWS : 띄어쓰기 허용)
- field-name은 대소문자 구분없음

용도

- HTTP 전송에 필요한 모든 부가정보
- 표준헤더의 종류는 매우 많음, 일일히 다 외울 수 없음
- 필요시 임의의 헤더를 추가할 수 있음 (needThisHeader: required-header)



HTTP 메서드의 속성

1. 안전 (Safe Methods)
   - 리소스를 호출해도 리소스를 변경하지 않는다.
2. 멱등 (Idempotent Methods)
   - 한번 호출이나 100번 호출이나 결과가 똑같다. (GET, PUT, DELETE)
   - POST는 멱등이 아님, 같은 결제가 중복해서 발생할 수 있음
   - 멱등은 외부 요인으로 중간에 리소스가 변경되는 것은 고려하지 않음
3. 캐시가능 (Cacheable Methods)
   - GET, HEAD, POST, PATCH
   - 실제로는 GET, HEAD 정도만 캐시 사용

​    

### 클라이언트 >> 서버 데이터 전송

전달방식 (2가지)

- 쿼리 파라미터 사용
  - GET
  - 정렬 필터, 검색어
- 메시지 바디 활용
  - POST, PUT, PATCH
  - 회원가입, 상품주문, 리소스등록, 리소스변경

4가지 상황

1. 정적 데이터 조회 :  이미지, 정적 텍스트 문서 (GET), query string 미사용
2. 동적 데이터 조회 : 검색, 게시글 목록 정렬, query string 사용
3. HTML form 전송
   - POST 전송
   - Content-Type : application/x-www-form-urlencoded 사용시
     - form 내용을 메시지 바디로 전송 (query string)
     - url encoding 처리후 전송 (김 >> %EA%B9%80)
   - Content-Type : multipart/form-data
     - 파일 업로드같은 바이너리 데이터 전송시 사용
     - 다른 종류의 여러 파일과 폼의 내용 함께 전송가능
4. HTTP API를 통한 전송 : AJAX, server to server
   - 백엔드 시스템 통신 : server to server
   - 앱 클라이언트 : 아이폰, 안드로이드
   - 웹 클라이언트 : AJAX
   - POST, PUT, PATCH : 메시지 바디 활용
   - Content-Type : application/json 주로 활용

​    

---

## API URI 설계

- 리소스를 기준으로 설계 (회원) [명사]
- 리소스를 대상으로 하는 행위로 분리 (조회, 등록, 삭제, 변경) [동사]

### GET

- 리소스 조회
- 서버에 전달하고 싶은 데이터는 `query string`를 통해 전달
- 메시지 바디를 사용할 수는 있지만, 지원하는 곳이 많지않아 권장하지 않음

### POST

- 요청 데이터 처리
- 메시지 바디를 통해 서버로 요청데이터 전달
- 서버는 요청 데이터를 처리
- 신규 리소스 등록
- 프로세스 처리
- 다른 메서드로 처리하기 애매한 경우 사용
  - JSON으로 조회 데이터를 넘길 때, GET메서드를 사용하기 어려울 때 사용
  - 애매하면 POST 사용

### PUT

- 리소스를 완전히 대체 (덮어쓰기) : 주의해서 사용해야함
  - 리소스가 있으면 대체
  - 리소스가 없으면 생성
- 클라이언트가 리소스를 식별한다.
  - 클라이언트가 리소스 위치를 인지하고 URI로 지정한다. (POST와의 차이점)

### PATCH

- 리소스 부분변경
- PUT과 달리 요청한 요소만 변경되고, 기존데이터는 유지됨

### DELETE

- 리소스 제거

​    

> URL 설계 개념

- 문서 (document)
  - 단일 개념 : 파일 1개, 객체 인스턴스, DB 한행
  - /members/100, /files/star.jpg
- 컬렉션 (collection)
  - 서버가 관리하는 리소스 디렉토리
  - 서버가 리소스의 URI를 생성하고 관리
  - /members
- 스토어 (store)
  - 클라이언트가 관리하는 자원 저장소
  - 클라이언트가 리소스의 URI를 알고 관리
  - /files
- 컨트롤러 (controller), 컨트롤 URI
  - 문서, 컬렉션, 스토어로 해결하기 어려운 추가 프로세스 실행
  - 동사를 직접 사용
  - /members/{id}/delete

​    

---

## HTTP 상태코드

- 클라이언트가 보낸 요청의 처리상태를 응답에서 알려주는 기능

| 상태코드 | 명칭          | 설명                                                         |
| -------- | ------------- | ------------------------------------------------------------ |
| 1xx      | Informational | 요청이 수신되어 처리중 (거의 안씀)                           |
| 2xx      | Successful    | 요청 정상 처리                                               |
| 3xx      | Redirection   | 요청을 완료하려면 추가 행동이 필요                           |
| 4xx      | Client Error  | 클라이언트 오류, 잘못된 문법등으로 서버가 요청을 수행할 수 없을 때 |
| 5xx      | Server Error  | 서버 오류, 서버가 정상 요청을 처리하지 못할 때               |

​    

> 모르는 상태코드 ?

- 클라이언트는 상위 상태코드로 해석해서 처리

​    

### 2xx (Successful)

- 클라이언트 요청을 성공적으로 처리

1. `200 OK` : 요청성공
2. `201 Created` : 요청 성공, 새로운 리소스 생성
3. `202 Accepted` : 요청은 접수되었으나 처리가 완료되지 않음 (배치 처리)
4. `204 No Content` : 서버가 요청을 성공적으로 수행했지만, 응답 페이로드 본문에 보낼 데이터가 없을 때 (save 버튼)

​    

### 3xx (Redirection)

- 요청을 완료하기 위해 유저 에이전트의 추가조치가 필요
- 3xx 응답 결과에 Location Header가 있으면 자동이동

1. `300 Multiple Choices` : 안씀
2. `301 Moved Permanetly`
3. `302 Found`
4. `303 See Other`
5. `304 Not Modified`
6. `307 Temporary Redirect`
7. `308 Permanent Redirect`



리다이렉션 종류

- 영구 리다이렉션 (`301`, `308`)
  - 특정 리소스의 URI가 영구적으로 이동
  - `301 Moved Permanetly` : 요청 메서드가 GET으로 변하고, 본문이 제거될 수 있음
  - `308 Permanent Redirect` : 요청 메서드와 본문이 유지 (사용 잘 안함)
- 일시 리다이렉션 (`302`, `307`, `303`)
  - 일시적인 변경
  - `302 Found` : 요청 메서드가 GET으로 변하고, 본문이 제거될 수 있음
  - `307 Temporary Redirect` : 요청 메서드와 본문 유지 (요청 메서드를 변경해서는 안됨 [MUST NOT])
  - `303 See Other` : 요청 메서드가 GET으로 변경
  - PRG (POST >> Redirect >> GET)
    - POST로 주문후 새로고침으로 인한 중복 주문 방지
    - 주문결과 화면은 GET 메서드로 리다이렉트
- 특수 리다이렉션 : 결과대신 캐시 사용
  - `304 Not Modified`
    - 캐시를 목적으로 사용
    - 클라이언트에게 리소스가 수정되지 않았음을 알려줌
    - 이를 통해 클라이언트는 저장된 캐시를 재사용
    - 304 응답은 메시지 바디를 포함하면 안됨

​    

### 4xx (Client Error)

- 클라이언트의 요청이 잘못되어 서버가 요청을 수행할 수 없는 상태
- 오류의 원인 : 클라이언트
- 요청 내용을 재검토하고 수정후 다시 시도해야함

1. `401 Unauthorized`
   - 클라이언트가 해당 리소스에 대한 인증(Authentication)이 필요
   - 해당 오류시 WWW-Authenticate 헤더와 함께 인증

> 인증 (Authentication) : 본인이 누구인지 확인 (로그인)
>
> 인가 (Authorization) : 권한부여 

2. `403 Forbidden`
   - 서버가 요청을 이해했지만 승인을 거부
   - 인증 자격 증명은 있지만, 접근 권한이 충분하지 않는 경우 (어드민 아닌데 어드민 정보에 접근)

3.  `404 Not Found`
   - 요청 리소스를 서버에서 찾을 수 없음
   - 클라이언트가 권한이 안되는 리소스에 접근 시도시 리소스를 숨기고 싶을 때 사용

​    

### 5xx (Server Error)

- 서버 문제로 오류 발생
- 재시도시 요청이 성공할수도 있음

1. `500 Internal Server Error`
   - 서버 내부 문제로 오류 발생
   - 애매하면 500 에러 발생
2. `503 Service Unavailable`
   - 서비스 이용 불가
   - 서버가 일시적인 과부화 or 예정된 작업으로 잠시 요청을 처리할 수 없음
   - Retry-After 헤더 필드로 얼마뒤에 복구되는지 확인할 수 있음
