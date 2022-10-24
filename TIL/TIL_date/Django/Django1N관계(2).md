# Django 1 : N 관계 (2) - Like(좋아요)

​    

## 1️⃣ User(1) - Comment(N)

- User모델과 Comment모델 간의 관계 설정
- 1명의 회원은 0개 이상의 댓글을 작성할 수 있음 

​    

### 모델 관계 설정

```python
# articles/models.py
class Comment(models.Model):
  user = models.ForeingnKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

​    

---

## 2️⃣ CRUD

### 1. CREATE

- 인증된 회원의 댓글 작성 구현

```python
# articles/forms.py
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['user',]
```

- user필드에 작성해야하는 user객체는 view함수의 request 객체

```python
# articles/views.py
def comments_create(request, pk):
  article = Article.objects.get(pk=pk)
  comment_form = CommentForm(request.POST)
  if comment_form.is_valid():
    comment = comment_form.save(commit=False)  ❗❗
    comment.article = article  ❗❗
    comment.user = request.user  ❗❗
    comment.save()  ❗❗
  return redirect('articles:detail', article.pk)
```

​    

> NOT NULL constraint failed

- 댓글 작성시 외래키에 저장되어야할 작성자 정보가 누락 되었을 때 발생
- 댓글 작성시 작성자의 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용하면 해결가능

​    

### 2. READ

```django
{{ comment.user }}    <!-- 작성자 -->
{{ comment.content }} <!-- 댓글내용 -->
```

​    

### 3. DELETE

- 삭제 요청자와 댓글 작성자를 비교하여 본인이 쓴 댓글만 삭제할 수 있도록 해야함

```python
# articles/views.py
def comments_delete(request, article_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  if request.user == comment.user:   ❗✔️
    comment.delete()
  return redirect('articles:detail', article_pk)
```

- 댓글의 작성자가 아니면 삭제버튼을 비활성화

```django
<!-- articles/detail.html -->
{% if request.user == comment.user %}
	삭제버튼
{% endif %}
```

