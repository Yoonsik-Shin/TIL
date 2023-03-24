# Django 1 : N 관계 (1) - Comments (댓글)

​    

## 0️⃣ 1:N 관계

- 게시글(1) - 댓글(N)

```markdown
- 게시글은 댓글을 0개 이상 가짐
	- 게시글 1개 > 여러 개의 댓글(N)
	- 게시글 1개 > 0개의 댓글
	
- 댓글은 반드시 하나의 게시글에 속함
```

​    

---

## 1️⃣ Foreign Key

- 외래키
- RDB에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본키 (Primary Key)
- 키를 사용하여 부모테이블의 유일한 값 참조 (참조 무결성)
- 외래키의 값이 반드시 부모 테이블의 기본키일 필요는 없지만 유일한 값이어야 함

​    

> ForeignKey Arguments : `on_delete`

- 외래키가 참조하는 객체가 사라졌을 때, (게시글을 삭제하면)
- 외래키를 가진 객체를 어떻게 처리할 지 정의 (게시글 속 댓글은 어떻게 할건지)
- 데이터 무결성에 중요한 설정
- on_delete 옵션
  - CASCADE : 부모객체가 삭제됐을 때, 이를 참조하는 객체도 삭제
  - PROTECT : 부모객체를 삭제하려고 할 때, 참조하는 객체가 있으면 삭제를 못하게 해줌
  - SET_NULL : ForeignKeyField값을 NULL로 변경 (`null=True`에서만 활용가능)
  - SET_DEFAULT : ForeignKeyField값을 default로 변경 (default 값이 있을 때만 활용가능)

​    

> ForeignKey Arguments : `related_name`

- 선택 옵션
- 역참조시 사용하는 매니저 이름(model_set manager) 변경
- 작성후, migration 필요

​    

---

## 2️⃣ Comment Model

### 1. 정의하기

```python
# apps/models.py
class Comment(models.Model):
  app = models.ForeignKey(App, on_delete=models.CASCADE)
```

- 외래키 필드는 ForeignKey 클래스를 작성한 위치와 상관없이 필드의 마지막에 작성됨
- 인스턴스 이름 : 단수형, 소문자

### 2. Migration

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- 컬럼명 : `app_id`

​    

## 3️⃣ 관계 모델 참조

### 역참조

- 자신을 외래키로 지정한 테이블을 참조
- 1: N 관계 > 1이 N을 참

> Related manager

```python
# App 모델이 Comment 모델을 참조할 때 사용
app.comment_set.method()
```

```python
# 1번 게시글의 모든 댓글 조회
app = App.object.get(pk=1)
app.comment_set.all()
```

- `related_name`인자를 통해 매너지 이름 변경가능

```python
# apps/models.py
class Comment(model.Model):
	app = models.ForeignKey(App, on_delete=models.CASCADE, related_name == '이름변경')

>> app.이름변경_set
```

​    

> admin site 등록

- 새로 작성한 Comment 모델 admin site에 등록

```python
# apps/admin.py
from django.contrib import admin
from . models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display  = ('content', 'created_at', 'article')

admin.site.register(Comment, CommentAdmin)
```

​    

---

## 4️⃣ Comment CRUD 구현

### CREATE

1. CommentForm 작성

```py
# apps/forms.py
from .models import Comment

class CommentForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    fields = '__all__'
    exclude = ['app',]
```

2. detail 페이지에 CommentForm 출력 [view]

```python
# apps/views.py
from .forms import CommentForm

def detail(request, pk):
  app = App.objects.get(pk=pk)
  comment_form = CommentForm()
  context = {
    'app': app,
    'comment_form': comment_form,
  }
  return render(request, 'apps/detail.html', context)
```

3. detail 페이지에 CommentForm 출력 [template]

```django
<!-- apps/detail.html -->
<form action='' method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit">
</form>
```

4. variable routing 사용

```python
# apps/urls.py
urlpatterns = [
  path('<int:pk>/comments/', views.comments_create, name=comments_create),
]
```

```django
<!-- apps/detail.html -->
<form action="{% url 'articles:commments_create' app.pk %}" method="POST">
	{% csrf_token %}
  {{ comment_form }}
  <input type="submit">
</form>
```

```python
# apps/views.py
def comments_create(request, pk):
  app = App.objects.get(pk=pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    comment = comment_form.save(commit=False)
    comment.app = app
    comment.save()
  return redirect('apps:detail', app.pk)
```

​    

> `save()` 메서드

```python
.save(commit=False)
```

- 생성하되, 아직 새로운 인스턴스를 저장하지 말아라
- 아직 DB에 저장되지 않은 인스턴스를 반환
- 저장하기전에 객체에 대한 사용자 지정 처리를 수행할 때 사용

​    

### READ

- 작성한 댓글 목록 출력

```python
# apps/views.py
from .models import Comment

def detail(request, pk):
  app = App.objects.get(pk=pk)
  comment_form = CommentForm()
  comments = app.comment_set.all()
  context = {
    'app': app,
    'comment_form': comment_form,
    'comments': comments,
  }
  return render(request, 'apps/detail.html', context)
```

```django
<!-- apps/detail.html -->
{% for comment in comments %}
	{{ comment.content }}
{% endfor %}

```

​    

### DELETE

- 댓글 삭제 구현

```python
# apps/urls.py
urlpatterns = [
  path('<int:app_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='cocomments_delete'),
]
```

```python
# apps/views.py
def comments_delete(request, app_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('apps:detail', app_pk)
```

```django
<!-- apps/detail.html -->
<form action="{% url 'articles:comments_delete' app.pk comment.pk %}" method="POST">
	{% csrf_token %}
  <input type="submit" value="DELETE">
</form>
```

​    

---

## 5️⃣ Comment Count

방법1. DTL filter의 length

```django
{{ comments|length }}
{{ app.comment_set.all|length }}
```

​    

방법2. Queryset API의 count()

```django
{{ comments.count }}
{{ app.comment_set.count }}
```

​    

---

## 6️⃣ 댓글 없는 경우

- DTL for empty 활용

```django
{% for comment in comments %}
	...
{% empty %}
	<p>아직 댓글이 없습니다. 첫 댓글을 작성해보세요!</p>
{% endfor %}
```

