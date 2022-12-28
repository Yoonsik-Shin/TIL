# Django정리 (8)

​    

## 1️⃣ 쿠키 (Cookie)

- 서버가 사용자의 웹브라우저(클라이언트)에 전송하는 작은 데이터 조각
- 브라우저는 쿠키를 로컬에 Key-value 형식을 저장
- 동일한 서버에 재요청시 저장된 쿠키를 함께 전송
- 서로 다른 요청이 동일한 브라우저로부터 발생한 것인지 판단할 때 사용
- 상태가 없는 HTTP에서 상태정보를 관리
- 사용자가 로그인 상태를 유지할 수 있게 해줌

​    

### 1. 사용목적

- 세션관리 : 로그인, 아이디 자동완성, 공지 하루동안 안보기, 팝업체크, 장바구니등의 정보관리
- 개인화 : 사용자 선호, 테마 설정
- 트래킹 : 사용자의 행동을 기록 및 분석

​    

> 세션 (Session)

- 사이트와 특정 브라우저 사이의 상태를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 세션 ID를 발급하고, 클라이언트는 이를 쿠키에 저장
- 세션 ID는 세션을 구별하기 위해 필요

​    

### 2. 수명

- Session cookie
  - 현재 세션이 종료되면 삭제
  - 브라우저 종료와 함께 세션 삭제
- Persistent cookies
  - Expires 속성에 지정된 날짜나 Max-Age속성에 지정된 기간이 지나면 삭제

​    

### 3. Django에서의 세션

- database-backed sessions 저장 방식을 기본값으로 사용
- session 정보는 Django DB의 `django_session` 테이블에 저장

​    

---

## 2️⃣ Login

 ### AuthenticationForm

- 로그인을 위한 내장 폼
- 로그인하고자 하는 사용자 정보를 입력 받음 (`username`, `password`)
- ModelForm이 아닌 일반 Form을 상속 받아, request를 첫번째 인자로 취함

```python
class AuthenticationForm(forms.Form):
  username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
 	password = forms.CharField(
  	label = _("Password"),
    strip = False,
    widget = forms.PasswordInput(attrs={"autocomplete": "current-password"}),
  )
```

​    

### login

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('login/', views.login, name='login'),
]
```

```python
# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
  if request.user.is_authenticated:
    return redirect('apps:index')
  if request.method == 'POST':
    login_form = AuthenticationForm(request, date=request.POST)
    if login_form.is_valid():
      auth_login(request, login_form.get_user())
      return redirect(request.GET.get('next') or'apps:index')
  else:
    login_form = AuthenticationForm()
  context = {
    'login_form': login_form,
  }
  return render(request, 'accounts/login.html', context)
```

```django
<!-- template -->
<a href="{% url 'accounts:login' %}">로그인</a>
```

​    

> login 함수

```python
login(request, user, backend=None)
```

- 인증된 사용자를 로그인
- 유저 ID를 세션에 저장하고 기록
- HttpRequest객체와 User 객체가 필요
  - authenticate() 함수를 활용한 인증
  - AuthenticastionForm을 활용한 is_valid
- 일반적인 ModelForm 기반 Create 로직과 동일하나 필수 인자 구성이 다름

​    

> get_user()

- AuthenticationForm의 인스턴스 메서드
- 유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환



> 세션 데이터 확인

- django_session 테이블
- 브라우저 개발자도구 - Application - Cookies

​    

#### 로그인 상태의 유저 정보

- context 데이터 없이 user변수를 활용할 수 있는 이유
  -  settings.py의 context processors 설정의 'django.contrib.auth.context_processors.auth'

​    

> context processors

- django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해둔것
- 템플릿이 렌더링될 때 호출가능한 컨텍스트 데이터 목록
- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용가능한 변수로 포함됨

​    

> django.contrib.auth.context_processors.auth

```django
{{ user }}
```

- 클라이언트가 로그인한 경우 User 클래스의 인스턴스
- 클라이언트가 로그인하지 않은 경우 AnonymousUser 클래스의 인스턴스

​    

---

## 3️⃣ Logout

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
  path('logout/', views.logout, name='logout'),
]
```

```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
  auth_logout(request)
  return redirect('apps:index')
```

```django
<!-- base.html -->
<form action="{% url 'accounts:logout' %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="로그아웃">
</form>
```

​    

>  logout 함수

```python
logout(request)
```

- 요청 유저에 대한 세션 정보를 삭제함
  - DB에서 session data 삭제
  - 클라이언트 쿠키에서 세션ID 삭제
- HttpRequest 객체를 인자로 받음
- 반환값 없음
- 사용자가 로그인하지 않은 경우에 호출해도 오류가 발생하지 않음

​    

---

## 4️⃣ Limiting access

- 로그인 사용자에 대한 접근 제한하기

​    

### 1. is_authenticated 속성을 활용한 조건문

- 로그인 / 비로그인 상태에서 출력되는 링크 다르게 하기

```django
<!-- template -->
{% if request.user.is_authenticated %}
```

- 인증된 사용자는 로그인 로직을 수행할 수 없도록 처리

```python
# accounts/views.py
def login(request):
  if request.user.is_authenticated
  	return redirect('apps:index')
```

​    

> is_authenticated

```python
class AbstractBaseUser(models.Model):
  def is_authenticated(self):
    return True
```

- 사용자가 인증되었는지 여부를 알 수 있는 방법
-  User model의 속성
- 모든 User 인스턴스에 대해 항상 True
- AnonymousUser에 대해 항상 False
- 일반적으로 `request.user`에서 사용
- 권한(permission)은 관련 없음
- 사용자가 활성화 상태이거나 유효한 세션을 가지는지 확인하지 않음

​    

### 2. login_required decorator를 활용한 view 제한

- 로그인 상태에서만 글 작성/수정/삭제

```python
from django.contrib.auth.decorators import logine_required

@login_required
def create(request):
  pass

@login_required
def update(request):
  pass

@login_required
def delete(request):
  pass
```

​    

> login_required decorator

- 사용자가 로그인 되어있으면 정상적으로 view함수 실행
- 로그인하지 않은 사용자는 settings.py의 LOGIN_URL 문자열 주소('/accounts/login/')로 redirect됨 
- 인증 성공시 사용자가 redirect 경로는 `next`라는 query string 매개변수에 저장

```python
/accounts/login/?next=/articles/create
```

​    

> "next" query string

```python
# accounts/views.py
def login(request):
  if request.user.is_authenticated:
    return redirect('apps:index')
  
  if request.method == 'POST':
    login_form = AuthenticationForm(request, request.POST)
    if login_form.is_valid():
      auth_login(request, login_form.get_user())
      return redirect(request.GET.get('next') or 'apps:index')
```

- 주의사항 : form의 action이 빈 값이여야함

```django
<form action="" method="POST"></form>
```

