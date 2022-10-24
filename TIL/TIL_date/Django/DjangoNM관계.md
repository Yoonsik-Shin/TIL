# Django N:M 관계

​    

## 1️⃣ Many to many relationship (M:N 관계)

- 병원 예약 시스템 구축 DB 모델링

​    

### 1. 중개모델 활용

- 환자 모델의 외래키를 삭제하고 별도의 예약 모델 새로 작성
- 예약 모델은 의사, 환자와 각각 1:N 관계

```python
# hospitals/models.py
# 환자
class Patient(models.Model):
  name = models.TextField()
  
# 의사
class Doctor(models.Model):
  name = models.TextField()
  
# 예약 (중개모델)
class Reservation(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

- 새로운 예약 만들기

```python
doctor1 = Doctor.objects.create(name='yoon')
patient1 = Patient.objects.create(name='shin')

Reservation.objects.create(doctor=doctor1, patient=patient1)
```

- 예약 정보 조회

```python
# 의사
doctor1.reservation_set.all()

# 환자
patient1.reservation_set.all()
```

​    

### 2. ManyToManyField 활용

- Django는 `ManyToManyField` 를 통해 중개 테이블을 자동으로 생성함
- M:N 관계로 맺어진 두 테이블에는 변화가 없음
-  ManyToManyField는 M:N 관계를 가진 모델 어디에 위치해도 상관 없음
- ❗필드 작성 위치에 따라 참조와 역참조의 방향이 바뀜으로 주의

```python
# hospitals/models.py
class Doctor(models.Model):
  name = models.TextField()
  
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor) ✔️✔️
  name = models.TextField( ) # 환자이름
```

- 의사 1명, 환자 2명 생성

```python
doctor1 = Doctor.objects.create(name='yoon')
patient1 = Patient.objects.create(name='shin')
patient2 = Patient.objects.create(name='sik')
```

- 예약 생성 [`add()`]

```python
# 환자 shin이 의사 yoon에게 예약
patient1.doctors.add(doctor1)

# 환자 shin의 예약 의사목록 확인
patient1.doctors.all()

# 의사 yoon의 예약 환자목록 확인
doctor1.patient_set.all()

# 의사 yoon이 환자 sik을 예약
doctor1.patient_set.add(patient2)
```

- 예약 취소 [`remove()`]

```python
# 의사 yoon이 환자 shin의 진료예약 취소
doctor1.patient_set.remove(patient1)

# 환자 sik이 의사 yoon의 진료예약 취소
patient2.doctors.remove(doctor1)
```

​    

> `related_name` argument

- 참조할 때 사용할 매니저 이름 지정
- ForeignKey의 `related_name`과 동일

​    

> `through` argument

- 중개 테이블을 수동으로 지정하려는 경우 사용하여 모델을 지정
- 중개 테이블에 추가 데이터를 사용해 다대다 관계로 연결하려는 경우

```python
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor, through='Reservation') ✔️✔️
  name = models.TextField()

# 예약 정보에 증상과 예약일 추가
class Reservation(models.Model):
  doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  symptom = models.TextField()
  reserved_at = models.DateTimeField(auto_now_add=True)
```

​    

> symmetrical argument

- default : True
- ManyToManyField가 동일한 모델을 가리킬 때 사용
- ManyToManyField는 기본적으로 대칭적 관계

```python
class Person(models.Model):
  friends = models.ManyToManyField('self', symmetrical=False)
```

- True일 경우
  - _set 매니저를 추가하지않음
  - 대칭적 구조 (두 모델 인스턴스들이 서로 참조가능)

- False일 경우 
  - 지정시 비대칭적으로 만들어줌
  - 팔로우 기능 구현시 사용

​    

### 3. Related Manager

- 1:N or M:N 관계에서 사용가능한 context
- Django는 모델간 1:N or M:N 관계가 설정되면 역참조시에 사용할 수 있는 manager 생성
- 같은 메서드여도 각 관계별로 다르게 동작함
  - 1:N : target 모델 객체만 사용가능
  - M:N : 관련된 두 객체 모두 사용 가능
- 메서드 종류
  - add() : 지정된 객체를 관련 객체 집합에 추가
  - remove() : 관련 객체 집합에서 지정된 모델 개체를 제거

​    

### 4. 중개 테이블 필드 생성 규칙

- 소스모델 및 대상모델이 다른 경우
  - id
  - <containing_model>_id
  - <other_model>_id
- ManyToManyField가 동일한 모델을 가리키는 경우
  - id
  - from`_<model>_`id
  - to`_<model>_`id

​    

---

## 2️⃣ 좋아요 구현

### 1. 모델 관계 설정

```py
# 오류 발생
class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
```

- like_users 필드 생성시 자동으로 역참조에 `.article_set` 매니저 생성
- 이미 Aritcle-User 관계에서 해당 매니저를 사용중
- 둘 중 하나에 `related_name`을 지정해줘야함 (보편적으로 M:N 관계에 지정)

```python
class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

​    

> User - Article 간 사용가능한 related manager

- `article.user` : 게시글을 작성한 유저 [1:N]
- `user.article_set` : 유저가 작성한 게시글 (역참조) [1:N]
- `article.like_users` : 게시글을 좋아요한 유저 [M:N]
- `user.like_articles` : 유저가 좋아요한 게시글 (역참조) [M:N]

​     

### 2. MVT 구현

```python
# articles/urls.py
urlpatterns = [
  path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

```python
# articles/views.py
def likes(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  if article.like_users.filter(pk=request.user.pk).exists():
# if request.user in article.like_users.all():
		article.like_user.remove(request.user)
	else:
    article.like_users.add(request.user)
  return redirect('articles:index')
```

> `.exists()` : QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False 반환

```django
<!-- articles/index.html -->
<form action="{% url 'articles:likes' article.pk %}" method="POST">
  {% csrf_token %}
  {% if request.user in article.like_users.all %}
  	<input type="submit" value="좋아요 취소">
  {% else %}
  	<input type="submit" value="좋아요">
  {% endif %}
</form>
```

