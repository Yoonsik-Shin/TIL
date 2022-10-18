# Django 개념 (4)

​     

## ✍️ CRUD 구현

### 0️⃣ base 템플릿

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- bootstrap CSS CDN -->
<title>Document</title>
</head>
<body>
<div class="container">
{% block content %}
{% endblock content %}
</div>
<!-- bootstrap JS CDN -->
</body>
</html>
```

```python
# settings.py
`TEMPLATES = [
  {
    ...,
    'DIRS': [BASE_DIR / 'templates',],
  }
]
```

​    

### 1️⃣ urls 정리

```python
# apps/urls.py
from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
  path('', views.index, name='index'),
]
```

```python
# project/urls.py
from django.urls import path, include

urlpatterns = [
  path('apps/', include('apps.urls'))
]
```

​    

### 2️⃣ 전체 게시글 조회

```python
# apps/views.py
from .models import App

def index(request):
  apps = App.objects.all()
  context = {
    'apps': apps,
  }
  return render(request, 'apps/index.html', context)
```

```django
<!-- templates/apps/index.html -->
{% extends 'base.html' %}
{% block content %}
	{% for app in apps %}
		{{ app.pk }}
{% endblock content %}
```

​     

### 3️⃣ CREATE

- create 로직 구현에 사용되는 view 함수

1. `new` : 사용자의 입력을 받을 페이지를 렌더링하는 함수
2. `create` : 사용자가 입력한 데이터를 전송받아 DB에 저장하는 함수

```python
# apps/urls.py
urlpatterns = [
  path('', views.index, name='index'),
  path('new/', views.new, name='new'),
  path('create/', views.create, name='create'),
]
```

```python
# apps/views.py
def new(request):
  return render(request, 'apps/new.html')

def create(request):
  title = request.POST.get('title')
  content = request.POST.get('content')
  Article.objects.create(title=title, content=content)
  return redirect('apps:index')
```

```django
<!-- templates/apps/new.html -->
{% extends 'base.html' %}
{% block content %}
	<form action="{% url 'apps:create' %}" method="POST">  
  </form>
{% endblock content %}
```

​    

> redirect

- 인자에 작성된 곳으로 요청을 보냄

```python
# apps/views.py
from django.shortcuts import render, redirect

def create(request):
  return redirect('apps:index')
```

- 사용가능 인자
  1. view name (URL pattern name) : `return redirect('apps:index')`
  2. absolute or relative URL : `return redirect('/apps/')`

- 동작 원리
  1. 클라이언트가 create url로 요청을 보냄
  2. create view 함수의 redirect 함수가 `302` status code를 응답
  3. 응답받은 브라우저는 redirect인자에 담긴 주소로 이동하기 위해 django에 재요청
  4. 주소에 담긴 페이지로 정상 응답 받음 (`200` status code)

​    

> 302 Found

- HTTP response status code
- 브라우저가 사용자를 해당 URL 페이지로 이동 시킴

> 403 Forbidden

- 서버에 요청이 전달되었지만, 권한때문에 거절
- 서버에 요청은 도달했지만 서버가 접근을 거부할 때

​     

#### ✔️ CSRF

- Cross-Site-Request-Forgery (사이트 간 요청 위조)
- 사용자의 의지와 무관하게 공격자가 의도한 행동을 하게하여 특정 웹 페이지의 보안을 취약하게하거나 수정, 삭제등의 작업을 하게 만드는 공격
- 이를 방지하기 위해 `Security Token (CSRF Token)` 방식 사용

> CSRF Token

- 사용자의 데이터에 임의의 난수 값(Token)을 부여하여 매 요청마다 해당 난수 값을 포함시켜 전송
- 서버에서는 요청을 받을 때마다 전달된 Token 값이 유효한지 검증

```django
<form action="{% url '' %}" method="POST">
	{% csrf_token %}
</form>
```

- 템플릿에서 내부 URL로 향하는 Post form을 사용하는 경우 사용 (외부 URL은 보안 취약)

​    

### 4️⃣ READ

- 개별 게시글 상세 페이지 제작
- Variable Routing 활용

```python
# apps/urls.py
urlpatterns = [
  path('<int:pk>/', views.detail, name='detail'),
]
```

```python
# apps/views.py
def detail(request, pk)
  app = Article.objects.get(pk=pk)  # variable routing pk = DB레코드의 id 컬럼
  context = {
  	'app': app,
  }
  return render(request, 'apps/detail.html', context)	
```

```django
<!-- templates/apps/detail.html -->
...
{{ app.pk }} {{ app.title }} ...

<!-- templates/apps/index.html -->
...
{% for app in apps %}
	<a href="{% url 'articles:detail' app.pk %}">개별 detail 페이지</a>
{% endfor %}
```

​    

### 5️⃣ DELETE

- 특정 글 조회 후 삭제

```python
# apps/urls.py
urlpatterns = [
  path('<int:pk>/delete/', views.delete, name='delete'),
]
```

```python
# apps/views.py
def delete(request, pk):
  app = Article.objects.get(pk=pk)
  app.delete()
  return redirect('apps:index')
```

​    

### 6️⃣ UPDATE

- UPDATE 로직 구현에 사용되는 view 함수

1. `edit` : 사용자의 입력을 받을 페이지를 렌더링하는 함수
2. `update` : 사용자가 입력한 데이터를 전송받아 DB에 저장하는 함수

```python
# apps/urls.py
urlpatterns = [
	path('<int:pk>/edit/', views.edit, name='edit'),
  path('<int:pk>/update/', views.update, name='update'),
]
```

```python
# apps/views.py
def edit(request, pk):
  app = App.objects.get(pk=pk)
  context = {
  	'app': app,
  }
  return render(request, 'apps/edit.html', context)

def update(request, pk):
  app = App.objects.get(pk=pk)
  app.title = request.POST.get('title')
  app.content = request.POST.get('content')
  app.save()
	return redirect('apps:detail', app.pk)
```

```django
<!-- apps/edit.html -->
<form action="{% url 'articles:update' article.pk %}" method="POST">
	{% csrf_token %}
  <input type="text" name="title" value="{{ app.title }}">
  <textarea name="content" cols="30" rows="5">{{ app.content }}</textarea>
  <!-- textarea 태그는 value 속성이 없으므로 태그 내부 값으로 작성해야 한다. -->
  <input type="submit">
</form>

<!-- apps/detail.html -->
<a href="{% url 'apps:edit' app.pk %}">EDIT 페이지로 이동</a><
```
