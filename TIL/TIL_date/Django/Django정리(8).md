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

## Login

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
  if request.method == 'POST':
    login_form = AuthenticationForm(request, date=request.POST)
    if login_form.is_valid():
      auth_login(request, login_form.get_user())
      return redirect('apps:index')
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

```django
{{ user }}
```

- context 데이터 없이 user변수를 활용할 수 있는 이유
  -  settings.py의 context processors 설정의 'django.contrib.auth.context_processors.auth'



> context processors

