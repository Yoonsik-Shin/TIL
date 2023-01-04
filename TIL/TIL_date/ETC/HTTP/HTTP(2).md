# HTTP (2)

​    

## HTTP 헤더

- HTTP 전송에 필요한 모든 부가정보 (메시지 바디내용, 크기, 압축, 인증, 요청 클라이언트, 서버정보, 캐시)
- 필요시 임의의 헤더를 추가할 수 있음
- header-field : `field-name: 공백 field-value 공백`
  - `field-name`과 `:` 사이에 공백 허용안됨
- RFC2616 표준은 폐기됨, RFC7230~7235로 공부해야함



> RFC7230~7235

- 엔티티에서 표현(Representation)으로 변경
- 표현(Representation) = 표현 메타데이터(representation Metadata) + 표현 데이터(representation Data)
- 메시지 본문(message body)로 표현 데이터 전달
- 메시지 본문을 페이로드(payload)라고 함



### 표현

- 표현 : 요청이나 응답에서 전달할 실제 데이터
- 표현 헤더: 표현 데이터를 해석할 수 있는 정보 제공 / __전송, 응답__에 모두 사용됨

- `Content-Type` : 표현 데이터 형식
  - `text/html; charset=utf-8`
  - `application/json`
  - `image/png`
- `Content-Encoding` : 표현 데이터 압축 방식 / 데이터를 읽는 쪽에서 인코딩 헤더의 정보로 압축 해제
  - `gizp`
  - `deflate`
  - `identity`
- `Content-Language` : 표현 데이터 자연 언어
  - `ko`
  - `en`
  - `en-US`
- `Content-Length` : 표현 데이터 길이
  - 바이트 단위
  - 전송단위(Transfer-Encoding) 사용시 Content-Length 사용 x

​    

### 협상

- 클라이언트가 선호하는 표현 요청
- 협상 헤더는 __요청__시에만 사용

- `Accept` : 클라이언트가 선호하는 미디어 타입 전달
- `Accept-Charset` : 클라이언트가 선호하는 문자 인코딩
- `Accept-Encoding` : 클라이언트가 선호하는 압축 인코딩
- `Accept-Language` : 클라이언트가 선호하는 자연 언어

​    

> 협상 우선순위

1. `Quality Values(q)` 값 사용
   - 0 ~ 1
   - 클수록 높은 우선순위를 가짐
   - 생략하면 1
   - `Accept-Langauge: ko-KR,ko;q=0.9;en-US;q-0.8,en;q=0.7`
     1. `ko-KR`
     2. `ko;q=0.9`
     3. `en-US;q-0.8`
     4. `en;q=0.7`
2. 구체적인 것이 우선됨
   - `Accept: text/*, text/plain, text/plain;format=flowed, */*`
     1. `text/plain;format=flowed`
     2. `text/plain`
     3. `text/*`
     4. `*/*`
3. 구체적인 것을 기준으로 미디어 타입을 맞춤
   - `Accept: text/*;q=0.3, text/html;q=0.7, text/html;level=1, text/html;level=2;q=0.4, */*;q=0.5`

| Media Type        | Quality |
| ----------------- | ------- |
| text/html;level=1 | 1       |
| text/html         | 0.7     |
| text/plain        | 0.3     |
| image/jpeg        | 0.5     |
| text/html;level=2 | 0.4     |
| text/html;level=3 | 0.7     |

​    

### 전송방식

- 종류
  - 단순 전송 : `Content-Length`
  - 압축 전송 : `Content-Encoding`
  - 분할 전송 : `Transfer-Encoding` 
  - 범위 전송 : `Range, Content-Range`

​    

### 일반정보

- `From`
  - 유저 에이전트의 이메일 정보
  - 일반적으로는 잘 사용 안됨, __검색 엔진__
  - __요청__에서 사용
- `Referer`
  - 현재 요청된 페이지의 이전 웹페이지 주소
  - A에서 B로 이동하는 경우 B를 요청할 때 `Referer: A`를 포함하여 요청
  - __유입 경로 분석__시 사용
  - __요청__에서 사용
- `User-Agent`
  - 유저 에이전트 애플리케이션 정보
  - __어떤 종류의 브라우저에서 장애가 발생하는지 파악 가능__
  - __요청__에서 사용
- `Server`
  - 요청을 처리하는 오리진 서버의 소프트웨어 정보
  - __응답__에서 사용
- `Date`
  - 메시지가 생성된 날짜
  - __응답__에서 사용

​    

### 특별한 정보

- `Host`
  - 요청한 호스트 정보 (도메인)
  - 하나의 서버가 여러 도메인을 처리해야할 때 사용
  - 하나의 IP주소에 여러 도메인이 적용되어 있을 때 사용
  - __요청__에서 사용
- `Location`
  - 페이지 리다이렉션
  - 3xx 응답의 결과에 Location 헤더가 있으면 자동 이동
- `Allow`
  - 허용가능한 HTTP 메서드
  - `405 (Method Not Allowd)`에서 응답에 포함됨
  - `Allow: GET, HEAD, PUT`
- `Retry-After`
  - 유저 에어전트가 다음요청을 하기까지 기다려야하는 시간
  - `503 (Service Unavailable)`에서 서비스가 언제까지 불능인지 알려줄 수 있음
  - 날짜표기 :`Retry-After: Fri, 31 Dec 1999 23:59:59 GMT`
  - 초단위표기: `Retry-After: 120` 

​    

### 인증

- `Authorization`
  - 클라이언트 인증 정보를 서버에 전달
  - `Authorization: Basic ????`
- `WWW-Authenticate`
  - 리소스 접근시 필요한 인증 방법 정의
  - `401 Unauthorized` 응답과 함께 사용
  - `WWW-Authenticate: Newauth realm="apps", type=1, title="Login to \"apps\"", Basic realm="simple"`

​    

### 쿠키

- `Set-Cookie`
  - 서버에서 클라이언트로 쿠키 전달
- `Cookie`
  - 클라이언트가 서버에 받은 쿠키를 저장하고, HTTP 요청시 서버로 전달

- 사용처
  - 사용자 로그인 세션 관리
  - 광고 정보 트래킹
- 쿠키 정보는 항상 서버로 전송됨
  - 네트워크 트래픽을 추가로 유발함
  - 최소한의 정보만 사용해야함 (세션id, 인증토큰)
  - 보안에 민감한 데이터는 저장하면 안됨
- 생명주기 (`Expires`, `max-age`)
  - `Set-Cookie: expires=날짜` : 만료일이 되면 쿠키 삭제
  - `Set-Cookie: max-age=3600(s)` 
  - 세션쿠키 : 만료날짜를 생략하면 브라우저 종료시까지만 유지되는 쿠키
  - 영속쿠키 : 만료날짜까지 유지되는 쿠키
- 도메인 (`Domain`)
  - 명시 (`domain=example.org`)
    - 명시한 문서 기준 도메인 + 서브 도메인 (`example.org` + `dev.example.org`)
  - 생략 
    - 현재 문서 기준 도메인만 적용 (`example.org`)
- 경로 (`Path`)
  - 경로를 포함한 하위 경로 페이지만 쿠키 접근 가능
  - `path=/home`
    - `/home` : O
    - `/home/level1` : O
    - `/home/level1/level2` : O
    - `/hello` : X
- 보안 (`Secure`, `HttpOnly`, `SameSite`)
  - `Secure`
    - 적용시 https인 경우만 전송됨
  - `HttpOnly`
    - XSS 공격 방지
    - 자바스크립트에서 접근 불가 (document.cookie 불가능)
    - HTTP 전송에만 사용가능
  - `SameSite`
    - XSRF 공격 방지
    - 요청 도메인과 쿠키에 설정된 도메인이 같은 경우만 쿠키 전송
