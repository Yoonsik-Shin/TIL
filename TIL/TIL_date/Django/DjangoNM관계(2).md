# Django N:M 관계 (2)

​    

## 1️⃣ Profile (프로필)

```python
# accounts/urls.py
urlpatterns = [
  path('profile/<username>/', views.profile, name='profile'),
]
```

```python
# accounts/views.py
from django.contrib.auth import get_user_model

def profile(request, username):
  person = get_user_model().objects.get(username=username)
  context = {
    'person': person,
  }
  return render(request, 'accounts/profile.html', context)
```

```django
<!-- accounts/profile.html -->
<h1>{{ person.username }}님의 프로필</h1>

<h2>{{ person username }}'s 게시글</h2>
{% for article in person article_set all %}
	<div>{{ article.title }}</div>
{% endfor %}

<h2>{{ person username }}'s 댓글</h2>
{% for comments in person.comment_set.all %}
	<div>{{ comments.content }}</div>
{% endfor %}

<h2>{{ person.username }}'s 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
	<div>{{ article.title }}</div>
{% endfor %}
```

```django
<!-- 프로필로 이동 -->
{% if request.user.is_authenticated %}
	<a href="{% url 'accounts:profile' user.username %}">내 프로필 보기</a>
```

​    

---

## 2️⃣ Follow (팔로우)

### 모델 관계 설정

```python
# accounts/models.py
class User(AbstractUser):
  followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

​    

### MTV

```python
# accounts/urls.py
urlpatterns = [
  path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

```python
# accounts/views.py
@require_POST
def follow(request, user_pk):
  if request.user.is_authenticated:
    person = get_user_model().objects.get(pk=user_pk)
    if person != request.user:
      if person.followers.filter(pk=request.user.pk).exists():
    # if request.user in person.followers.all():
        person.followers.remove(request.user)
      else:
        person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
  return redirect('accounts:login')
```

```django
<p>팔로잉 : {{ person.followings.all|length }}</p>
<p>팔로워 : {{ person.followers.all|length }}</p>

{% if request.user != person %}
	<form action="{% url 'accounts:follow' person.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in person.follpwers.all %}
    	<input type="submit" value="Unfollow">
    {% else %}
    	<input type="submit" value="follow">
   	{% endif %}
  </form>
{% endif %}
```

​    

---

## 3️⃣ View decorators / functions

>  데코레이터 (Decorator)

- 기존 함수를 수정하지 않고 기능을 추가해주는 wrapper함수

```python
def a(func):
  def wrapper():
    print('1')
    func()         # bye() 함수 실행
    print('2')
  return wrapper

@hello
def bye():
  print('?')

bye()
>> 1
>> ?
>> 2
```

​    

### 405 Method Not Allowed

- django.views.decorators.http 데코레이터를 사용하여 요청 메서드를 기반으로 접근 제한
- 메서드 종류
  1. `require_http_methods()`
  2. `require_POST()`
  3. `require_safe()`

​    

> require_http_methods()

- View함수가 특정한 요청 method만 허용하도록 하는 데코레이터

```python
# views.py
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET','POST'])
def create(request):
  pass

@require_http_methods(['GET','POST'])
def update(request, pk):
  pass
```

​     

> require_POST()

- View함수가 POST요청 method만 허용하도록 하는 데코레이터

```python
# views.py
from django.views.decorators.http import require_POST

@require_POST
def delete(request, pk):
  app = App.object.get(pk=pk)
  app.delete()
  return redirect('apps:index')
```

​    

> require_safe()

- require_GET이 있지만 Django에서는 require_safe를 사용하는 것을 권장

```python
# views.py
from django.views.decorators.http import require_safe

@require_safe
def index(request):
  pass

@require_safe
def detail(request, pk):
  pass
```



> login_required와 require_POST

- login_required는 GET 요청을 처리하는 View함수에서만 사용해야함
- POST method만 허용하는 delete 같은 함수는 내부에서 is_authenticated 속성을 사용하여 처리

```python
# apps/views.py
@require_POST
def delete(request, pk):
  if request.user.is_authenticated:
    app = App.objects.get(pk=pk)
    app.delete()
  return redirect('apps:index')
```

​    

### 404 Not Found

> Django Shortcut functions

- 해당하는 객체가 존재하지 않으면 404 상태코드를 반환하는 함수

1. `get_object_or_404()` : get 사용시 객체가 존재하지 않을 때

```python
from django.shortcuts import get_object_or_404

def my_view(request):
    obj = get_object_or_404(MyModel, pk=1)
```

​    

2. `get_list_or_404()` : filter 사용시 빈 리스트를 반환할 때

```python
from django.shortcuts import get_list_or_404

def my_view(request):
    my_objects = get_list_or_404(MyModel, published=True)
```

