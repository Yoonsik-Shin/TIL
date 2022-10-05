# Django정리 (2)

​    

## 0️⃣ URLs

- 장고프레임워크는 URL끝에 `/` 자동으로 붙여줌

​    

---

## 1️⃣ App URL mapping

- 앱이 다수일 때, urls.py를 각 app에 매핑시키기

1. 각 앱의 view 함수를 다른 이름으로 import [✖️비추천]

```python
# 프로젝트/urls.py
from articles import views as articles_views
from pages import views as pages_views

urlpatterns = [
  path('', articles_views.index)
  path('', pages_view.index)
]
```

​    

2. 각 앱안에 urls.py 만들어 연결

<img src="Django정리(2).assets/image-20221004225008610.png" alt="image-20221004225008610" style="zoom:50%;" />

```python
# articles/urls.py
from django.urls import path
	path('index/', views.index),
urlpatterns = [
  
]
```

```python
# 프로젝트/urls.py 
from django.urls import path, include

urlpatterns = [
  path('articles/', include('articles.urls')),
] 
```

​    

> `include()`

- 다른 URL들을 참조할 수 있도록 돕는 함수

​    

---

## 2️⃣ Templates namespace

- 장고는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾을 수 있음
- settings.py의 INSTALLED_APPS에 작성한 app순서로 template 검색 후 렌더링
- 디렉토리 생성으로 물리적인 이름공간 구분하기
  - Templates의 기본 경로에 app과 같은 이름의 폴더를 생성
  - app_name/templates/app_name/ 형태로 변경됨

```python
# articles/views.py
return render(request, 'articles/index.html')

# pages/views.py
return render(request, 'pages/index.html')
```

​    

---

## 3️⃣ Naming URL patterns

- 문자열 주소 변경시 유지보수 편함
- path() 함수에 name인자 정의

```python
urlpatterns = [
  path('index/', views.index, name='index')
]
```

> 내장태그 - [`url`] 

```python
{% url 'index' %}
```

- URL 패턴이름와 일치하는 절대 경로 주소로 반환



> DRY 원칙

- Don't Repeat Yourself
- 소스코드에서 동이한 코드를 반복하지 말자

​    

---

## 4️⃣ URL namespace

- 서로 다른 앱에서 동일한 URL이름을 사용하는 경우 이름이 지정된 URL을 고유하게 사용가능

```python
# articles/urls.py
app_name = 'articles'  ✔️✔️
urlpatterns = []
```

- URL 태그 변화

```python
{% url 'index' %}
{% url 'articles:index' %}
```

-  app_name을 지정한 이후에는 반드시 app_name:url_name 형태로만 사용해야 함.
- 그렇지 않으면 NoReverceMatch 에러가 발생
