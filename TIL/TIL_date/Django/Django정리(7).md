# Django정리 (7)

​    

## 0️⃣ Django Auth

- django authentication system (인증시스템)
- 인증(Authentication) 과 권한(Authorization) 부여를 함께 제공
  - User, 권한 및 그룹, 암호 해시 시스템, Form, View 도구


```python
# settings.py
INSTALLED_APPS = [
  'django.contrib.auth',
]
```

>  인증(Authentication)

- 사용자 신원 확인

> 권한(Authorization) 

- 권한부여
- 인증된 사용자가 수행할 수 있는 작업 결정

​    

### 사전 설정

1. accounts 앱 생성 및 등록

```bash
$ python manage.py startapp accounts
```

```python
# settings.py
INSTALLED_APPS = [
  'accounts',
]
```

2. url 분리 및 매핑

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = []
```

```python
# 프로젝트/urls.py
urlpatterns = [
  path('accounts/', include('accounts.urls')),
]
```

​    

---

## 1️⃣ Django User Model

- 대부분 기본 유저모델을 상속받은 커스텀 유저모델을 이용
- 커스텀 유저모델 설정시 프로젝트의 모든 migrations / 첫 migrate 실행전에 작업을 완료해야함

​    

### AUTH_USER_MODEL ✔️✔️

- 프로젝트에서 Userr를 나타낼 때 사용하는 모델
- 프로젝트 진행중에는 변경 불가
- 첫 migration 전에는 확정 지어져야함

```python
# settings.py
AUTH_USER_MODEL = 'auth.User'  # 기본값
```

​    

### 대체하기

1. `AbstractUser`를 상속받는 커스텀 User 클래스 작성

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass
```

2. 커스텀 유저 모델 지정

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```

3. User 모델 등록

```python
# accounts/admin.py
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

​    

### User 객체활용

- 기본속성
  - username
  - password
  - email
  - first_name
  - last_name

​    

- User 생성

```python
user = User.objects.create_user('username','email','password')
```

- User 비밀번호 변경

```python
user = User.objects.get(pk=1)
User.set_password('new password')
User.save()
```

- User 인증 (비밀번호 확인)

```python
from django.contrib.auth import authenticate
user = authenticate(username=' ', password=' ')
```

​    

---

## 2️⃣ 암호관리

- django 기본 : PBKDF2 (Password-Based Key Derivation Function) 사용
- 단방향 해시함수 활용 (SHA256)
- 다이제스트로 암호화
- 복호화 불가능

​    

> 단방향 해시함수의 약점

1. 레인보우 공격
2. 무차별 대입 공격

- 보완법

1. 솔팅 (Salting) : 패스워드에 임의의 문자열인 salt를 추가하여 다이제스트 생성
2. 키 스트레칭 (Key Stretching) : 해시를 여러 번 반복해 시간을 늘림

​    

---

## 3️⃣ 회원가입

### UserCreationForm

- 주어진 username과 password로 권한이 없는 새로운 유저를 생성하는 ModelForm
- 3가지의 필드를 가짐
  - username
  - password1
  - password2

​    

### UserCreationForm 커스텀

- 기존 UserCreationForm을 상속받아 재정의

```py
# apps/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
  
  class Meta(UserCreationForm.Meta):
    model = get_user_model()
```

> `get_user_model()` : 현재 프로젝트에서 활성화된 사용자 모델을 반환

​    

### 회원가입 구현

```python
# apps/urls.py
app_name = 'apps'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
]
```

```python
# apps/views.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('apps:index')
  else:
    form = CustomUserCreationForm()
  context = {
    'form': form,
  }
  return render(request, 'accounts/signup.html', context)
```

```django
<!-- apps/signup.html -->
<form action="{% url 'accounts:signup' %}" method="POST">
  {% csrf_token %}
  {{ form }}
  <input type="submit">
</form>

<!-- base.html -->
<a href ="{% url 'accounts:signup' %}">회원가입</a>
```

​    

> UserCreationForm 의 save 메서드

- user를 반환

```python
def save(self, commit=True)
	user = super().save(commit=False)
  user.set_password(self.cleaned_data["password1"])
  if commit:
    user.save()
  return user
```

