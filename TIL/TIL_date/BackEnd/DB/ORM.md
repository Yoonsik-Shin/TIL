# ORM (Object Relational Mapping)

- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템간 데이터를 변환하는 프로그래밍 기술
- 파이썬은 라이브러리(SQLAlchemy, peewee)나 Django프레임워크 내장 ORM 활용
- ❗핵심 : 객체로 DB를 조작한다❗

​    

##  1. 모델 설계 및 반영

	1. 클래스를 생성하여 원하는 DB구조 생성

```python
# 기본형
class <테이블명> (models.Model):
  <컬럼명> = models.<타입명>(<타입조건>)
```

```python
# 예시
class Genre(models.Model):
	name = models.CharField(max_length=30)
```

​    

2. 클래스 내용을 DB에 반영하기 위한 마이그레이션 파일 생성

```bash
$ python manage.py makemigrations # 터미널에 작성
```

​    

3. DB에 migrate

```bash
$ python manage.py migrate # 터미널에 작성
```

​    

> Migration (마이그레이션)

- Model에 생긴 변화를 DB에 반영하기 위한 방법
- 마이그레이션 파일을 만들어 DB스키마를 반영

```bash
# 마이그레이션 명령어
$ makemigrations  # 마이그레이션 파일 생성
$ migrate         # 마이그레이션을 DB에 반영
```

​    

---

## 2. 데이터베이스 조작 (Database API)

```python
class_name . objects  .   all()
Class_Name / Manager / QuerySet API
```

> 환경설정

```bash
$ python manage.py shell_plus
>> In[0] : # 파이썬 문법 사용
```

​    

### 1. CREATE (2가지 방법)

#### 	1-1. create메서드 활용

```python
Genre.objects.create(name='락')
```

​    

#### 	1-2. 인스턴스 조작

```python
genre = Genre()
genre.name = '트로트'
genre.save()
```

​    

### 2. READ

#### 	1-1 전체 데이터 조회

```python
Genre.objects.all()
>> <QuerySet [<Genre: Genre object (1)>, <Genre: Genre object (2)>]
# 결과값이 QuerySet 타입으로 나옴
```

​     

#### 	1-2. 일부 데이터 조회 (`get`)

```python
Genre.objects.get(id=1) # << ()안에는 조회 조건
>> <Genre: Genre object (1)> # 하나의 결과값만 반환
```

​    

#### 	1-3. 일부 데이터 조회 (`filter`)

```python
Genre.objects.filter(id=1) # () 안에는 조회 조건
>> <QuerySet [<Genre: Genre object (1)>]>  # 리스트형태로 0~여러개의 값이 반환될 수 있음
```

​    

### 3. UPDATE

```python
# 변경 순서
# 1. genre 객체 활용 (변경할 데이터 조회)
genre = Genre.objects.get(id=1) # () 안에는 조회 조건

# 2. genre 객체 속성 변경
genre.name = '트로트'

# 3. genre 객체 저장
genre.save()
```

​    

### 4. DELETE

```python
# 삭제 순서
# 1. genre 객체 활용 (삭제할 데이터 조회)
genre = Genre.objects.get(id=1) # () 안에는 조회 조건

# 2. genre 객체 삭제
genre.delete()
```

