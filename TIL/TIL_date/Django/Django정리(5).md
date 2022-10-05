# Django 개념 (5)

​    

## 1️⃣ Admin site

- 관리자 페이지
- 모델 class를 admin.py에 등록하고 관리
- 직접 레코드 삽입 가능

​    

### 1. admin 계정 생성

```bash
$ python manage.py createsuperuser
```

- username, email, password를 입력하여 관리자 계정 생성
- email은 선택 사항
- password는 입력시 터미널상에 보이지않지만 입력되고 있음

​    

### 2. admin site 로그인

- http://127.0.0.1:8000/admin/으로 접속 후 로그인



### 3. admin에 모델 클래스 등록

```python
# articles/admin.py
from django.contrib import admin
from .models import Article       # models.py에서 Article 클래스 불러오기

admin.site.register(Article)
```

​    

---

## 2️⃣ Static files (정적파일)

- 응답할 때 별도의 처리없이 파일 내용을 그대로 보여주면 되는 파일
- 사용자의 요청과 상관없이 내용이 바뀌지 않는 파일
- JS, CSS, 이미지

​    

### 활용

1. 기본세팅

```python
# settings.py
INSTALLED_APPS = [
  'django.contrib.staticfiles',
]

STATICFILES_DIRS = [
  BASE_DIR / 'static',
]

STATIC_URL = '/static/'
```

2. static 디렉토리 만들기 : `app/static/app/정적파일`

![image-20221005172227770](Django정리(5).assets/image-20221005172227770.png)

3. html 파일에 불러오기

```django
{% load static %}
<img src="{% static 'apps/img/001.jpg' %}">
```

​    

> STATIC_URL

```python
# settings.py
STATIC_URL = '/static/'
```

- STATIC_ROOT에 있는 정적파일을 참조할 때 사용할 URL
- 실제 파일이나 디렉토리가 아님, URL로만 존재
- 비어있지 않은 값으로 설정 시 반드시 `/`로 끝나야함

​    

> STATIC_ROOT

```python
# settings.py
STATICFILES_DIRS = [
  BASE_DIR / 'static',
]
```

- collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
- 프로젝트에서 사용하는 모든 정적 파일을 한곳에 모아 넣는 경로

​    

> collectstatic

```bash
$ python manage.py collectstatic
```

​    

---

## 3️⃣ Django - BootStrap
