# Django정리 (1)

​    

## Variable routing

- URL주소를 변수로 사용하는 것을 의미
- URL의 일부를 변수로 지정하여 view함수의 인자로 넘길 수 있음
- 변수 값에 따라 하나의 `path()`에 여러 페이지 연결 가능
- 5가지 타입
  - 기본 타입 : `str`
  - 나머지 : `int`, `slug`, `uuid`, `path`

```python
# urls.py

urlpatterns = [
	...,
	path('index/<str:name>/', views.index),  ⬅️⬅️
]
```

```python
# apps/views.py 
def hello(request, name):  ⬅️⬅️
	context = {
    'name': name,
  }
  return render(request, 'index.html', context)
```



## Template inheritance (템플릿 상속)

```html
<!-- base.html [부모] -->
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- bootstrap CDN 작성 -->
 	<title>Document</title>
</head>
<body>
  {% block content %}      ⬅️⬅️ <!-- 상속 x, content는 임의로 붙인 이름으로 아무글자 가능 -->  
  {% endblock content %}   ⬅️⬅️ <!-- 상속 x, -->
  <!-- bootstrap CDN 작성 -->
</body>
</html>
```

```html
<!-- index.html -->
{% extends 'base.html' %}   ⬅️⬅️ <!-- 상속 (반드시 맨 위에 작성해야함) -->

<!-- 파일별로 개별적인 컨텐츠 작성 -->
{% block content %}
	<h1>이 파일은 index.html 입니다.</h1>
{% endblock content %}
```



> 부모 html의 위치를 프로젝트 최상단에 위치시키기❗❗



---

## form 데이터 다루기

### Sending form data (Client)

#### form

```html
<form action="" method=""></form>
```

- 데이터를 '어디(action)'로 '어떤 방식(method)'으로 보낼건지

- form 태그 속성

  1. action

     - 입력 데이터가 전송될 URL 지정

     - 반드시 유효한 URL이어야 함

     - 미지정시 데이터는 현재 form이 있는 페이지의 URL로 보내짐

  2. method
     - 데이터를 어떻게 보낼 것인지 정의 (HTTP request methods)
     - `GET` or `POST`

​    

#### input

```html
<input type="" name="">
```

- input 태그 속성
  1. name
     - 데이터 `submit`시 `name`속성값을 서버로 전송
     - 파라미터로 매핑됨



> GET

```html
<form action="" method="GET"></form>
```

- 서버로부터 정보를 조회하는데 사용
- 서버에게 리소스를 요청하기 위해 사용
- 데이터를 가져올 때만 사용
- 데이터를 서보로 전송시 Query String Parameters를 통해 전송
- 대소문자 구분 없지만 대부분 대문자 사용

​    

> Query String Parameters

```http
https://naver.com/search?key=value&key=value
```

- 사용자가 입력 데이터를 전달하는 방법 중 하나
- URL주소에 데이터를 파라미터를 통해 넘기는 것
- 키-값 쌍으로 구성
- `&`로 여러 개 연결
- 기본 URL과는 `?`로 구분됨



### Retrieving the data (Server)

- 데이터 가져오기, 검색하기
- 모든 요청 데이터는 `view`함수의 첫번째 인자 `request`에 들어 있음

```python
request.GET
>> <QueryDict: {'message': ['데이터']}>

request.GET.get('message')
>> '데이터'
```