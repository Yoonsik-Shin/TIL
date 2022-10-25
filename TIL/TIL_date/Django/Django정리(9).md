# Django정리 (9)

​    

## 1️⃣ 회원정보 수정

### UserChangeForm

- 사용자의 정보와 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

```python
# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    model = get_user_model()
    fields = ['email', 'first_name', 'last_name']
```

​    

### MTV

```python
# accounts/urls.py
app_name = 'accounts'

urlpatterns = [
  path('update/', views.update, name='update'),
]
```

```python
# accounts/views.py
def update(request):
  if request.method == POST:
    user_update_form = CustomUserChangeForm(request.POST, instance=request.user)
  else:
    user_update_form = CustomUserChangeForm(instance=request.user)
  context = {
    'user_update_form': user_update_form,
  }
  return render(request, 'accounts/update.html', context)
```

```django
<!-- accounts/update.html -->
<form action="{% url 'accounts:update' %}" method="POST">
  {% csrf_token %}
  {{ user_update_form }}
  <input type="submit">
</form>
```

​    

---

## 2️⃣ 비밀번호 변경

### PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

​    

### MTV

```python
# accounts/url.py
app_name = 'accounts'

urlpatterns = [
  path('password/', views.change_password, name='change_password')
]
```

```python
# accounts/view.py
from django.contrib.auth.forms import PasswordChangeForm

def change_password(request):
  if request.method == 'POST':
    password_change_form = PasswordChangeForm(request.user, data=request.POST)
    if password_change_form.is_valid():
      password_change_form.save()
      return redirect('apps:index')
  else:
    password_change_form = PasswordChangeForm(request.user)
  context = {
    'password_change_form': password_change_form,
  }
  return render(request, 'accounts/change_password.html', context)
```

```django
<!-- accounts/change_password.html -->
<form action="{% url 'accounts:change_password' %}" method="POST">
  {% csrf_token %}
  {{ password_change_form }}
  <input type="submut">
</form>
```

​    

---

## 3️⃣ EXTRA

### 1. AbstractBaseUser의 모든 subclass 와 호환되는 forms

- forms.ModelForm 상속
  - `UserCreationForm`
  - `UserChangeForm`
- forms.Form 상속
  - `AuthenticationForm`
  - `SetPasswordForm`
  - `PasswordChangeForm`
  - `AdminPasswordChangeForm`

​    

### 2. 회원가입 이후 자동로그인

```python
# accounts/views.py
def signup(request):
  if request.method == 'POST':
    signup_form = CustomUserCreationForm(request.POST)
    if signup_form.is_valid()
    	user = signup_form.save()
      auth_login(request, user)
      return redirect('apps:index')
  else:
    signup_form = CustomUserCreationForm()
  context = {
    'signup_form': signup_form,
  }
  return render(request, 'accounts/signup.html', context)
```

​    

### 3. 암호변경시 세션 무효화 방지

- 비밀번호 변경시 기존 세션과 회원 인증 정보가 일치하지 않아 로그인 해제됨
- update_session_auth_hash 함수를 사용하여 이를 방지

```python
from django.contrib.auth import update_session_auth_hash

def change_password(request):
  if request.method == 'POST':
    password_change_form = PasswordChangeForm(request.user, request.POST)
    if password_change_form.is_valid():
      password_change_form.save()
      update_session_auth_hash(request, password_change_form.user)
      return redirect('apps:index')
  else:
  	password_change_form = PasswordChangeForm(request.user)
  context = {
    'password_change_form': password_change_form,
  }
  return render(request, 'accounts/change_password.html', context)
```

​    

> update_session_auth_hash 함수

```python
from django.contrib.auth import update_session_auth_hash

update_session_auth_hash(request, user)
```

- 현재 요청과 새 사용자 객체를 가져와 세션 데이터를 적절하게 업데이트 해줌
- 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 세션 데이터를 세션에 업데이트

​    

### 4.  회원탈퇴시 세션 삭제

- 탈퇴를 먼저 진행 후 로그아웃 하여야함
- 로그아웃 먼저하면 요청 객체가 없어져 버림

```python
# accounts/views.py
def delete(request):
  request.user.delete()
  auth_logout(request)
```

