# Django정리 (3)

​    

## 0️⃣ Framework 특징   

### 1.  Framework의 성격

- 독선적 (Opionionated)
  - 올바른 방법에 대한 분명한 규약이 존재
  - 문서화가 잘 되어 있음
  - 주요상황을 벗어난 문제에 대해서는 유연하지 못함
- 관용적 (Unopinionated)
  - 제약이 거의 없음
  - 자유도가 높음
  - 써야할 것들을 직접 찾아야하는 어려움이 있음

​    

### 2. Django의 성격

- 다소 독선적 : 양쪽 모두에게 최선의 결과를 준다고 강조

​    

### 3. Django의 설계 철학

1. 표현과 로직(view) 분리
2. 중복 배제

​    

---

## 1️⃣ Django Model

- Django는 Model을 통해 데이터에 접근하고 조작
- 일반적으로 각각의 모델은 하나의 DB테이블에 매핑 (모델 클래스 == DB테이블)

​    

### 1. Model 작성하기

1. 새 프로젝트, 앱 작성 및 앱등록

```bash
$ django-admin startproject CRUD .
$ python manage.py startapp articles
```

```python
# settings.py
INSTALLED_APPS = [
  'articles',
  ...,
]
```

2. models.py 작성

- 모델의 클래스 == 테이블 스키마

```python
# articles/models.py
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```

​    

> [Django Model Field](https://docs.djangoproject.com/ko/3.2/ref/models/fields/)

- 데이터 유형에 따라 다양한 모델 필드 제공
- 자주 사용하는 모델 필드
  1.  CharField(max_length=None, **options) : 길이 제한 있는 문자열, 유효성 검증 o
  1.  TextField(**options) : 글자수 많을 때, 유효성 검증 x
  1.  DateTimeField() : 파이썬의 datetime.datetime 인스턴스로 표시되는 날짜, 시간 값을 사용
  
      3-1. auto_now_add : 최초 생성일자
  
      3-2. auto_now : 최종 수정일자

| Column  | Data Type   |
| ------- | ----------- |
| title   | VARCHAR(10) |
| content | TEXT        |

​    

### 2. Migrations

1. makemigrations

- 모델의 변경사항에 대한 새로운 migration을 만들 때 사용

```bash
$ python manage.py makemigrations
```

2. migrate

- makemigrations로 만든 설계도를 실제 DB에 반영하는 과정 (동기화)
- db.sqlite3 파일에 반영됨

```bash
$ python manage.py migrate
```



> Migrations 기타 명령어

1. showmigrations

```bash
$ python manage.py showmigrations
```

- migrations 파일들의 migrate여부를 확인하는 용도
- `[X]` 표시가 있으면 migrate가 완료됐음을 의미

2. sqlmigrate

```bash
$ python manage.py sqlmigrate articles 0001
```

- 해당 migrations 파일이 SQL문으로 어떻게 해석되는지 미리 확인 가능

​    

### 3. 모델 변경사항 반영

1. 추가 모델 필드 작성 후 다시 makemigrations을 진행
2. 이미 존재하는 컬럼에 대해 어떤 값을 설정할 것인지 물어봄

```bash
You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.

# 1) 다음 화면으로 넘어가서 새 컬럼의 기본값을 직접 입력하는 방법
1) Provide a one-off default now (will be set on all existing rows)
# 2) 현재 과정에서 나가고 모델 필드에 default 속성을 직접 작성하는 방법
2) Quit, and let me add a default in models.py
Select an option: 1     # 1번 옵션 선택
```

3. 아무것도 입력하지 않고 Enter를 누르면 장고에서 알아서 기본값 처fl

```bash
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>>
```

4. 새로운 마이그레이션 파일이 만들어진 것을 확인 후 DB와 동기화

```bash
$ python manage.py migrate
```

​    

---

## 2️⃣ ORM

> [ORM 참조](../DB/ORM.md)

- Object - Relational - Mapping
- SQL을 사용하지 않고 DB를 조작할 수 있게 만들어주는 매개체

​    

---

## 3️⃣ QuerySet API

### 1. 사전준비

- 외부 라이브러리 설치/설정

```bash
$ pip install ipython   # 파이썬 기본 쉘보다 더 강력한 파이썬 쉘
$ pip install django-extensions  # Django 확장 프로그램 모음 (shell_plus, graph model)
```

```python
# settings.py
INSTALLED_APPS = [
  'django_extensions',
]
```

​    

> Shell

- 운영체제상에 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
- 사용자 <-> Shell <-> 운영체제

​    

> Python Shell

- 파이썬 코드를 실행해주는 인터프리터
- 인터렉티브 or 대화형 shell
- 명령어 실행후 바로 결과 제공

​     

> Django shell

```bash
$ python manage.py shell_plus
```

```bash
# shell_plus 실행시
# Shell Plus Model Imports
from articles.models import Article
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery
Python 3.9.13 (main, Aug 24 2022, 22:54:29) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.4.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: 
```

​    

### 2. 활용

> [QuerySet API 종류](../DB/QuerySet_API.md)

#### CREATE

##### 방법1

```python
article = Article()    # 1. 클래스를 통한 인스턴스 생성
article.title = ' '    # 2. 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
article.save()         # 3. 인스턴스로 save 메서드 호출
```

#### 방법2

```python
article = Article(title=' ', content=' ')
article.save()
```

