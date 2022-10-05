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
  1.	CharField(max_length=None, **options) : 길이 제한 있는 문자열, 유효성 검증 o
  1.	TextField(**options) :글자수 많을 때, 유효성 검증 x

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

