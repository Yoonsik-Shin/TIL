# 🖼️ 미디어 파일

- 사용자가 웹에서 업로드하는 정적파일

​    

## 0️⃣ Media 관련 필드

### ImageField

- 이미지 업로드에 사용하는 model field
- FileField 상속
- 업로드된 객체의 유효성 검사 포함
- 최대길이 100자, max_length인자 사용가능
- 사용하려면 반드시 `Pillow`라이브러리 필요

​    

### FileField

- 파일 업로드에 사용하는 model field

>  upload_to

```python
# models.py
# 1. 문자열 경로 지정 방식
class MyModel(models.Model):
  # MEDIA_ROOT/uploads/
  upload = models.FileField(upload_to='uploads/')
  
  # MEDIA_ROOT/uploads/
  upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
  
# 2. 함수 호출
def app_image_path(instance, filename):
  return f'user_{instance.user.pk}/{filename}'

class app(models.Model):
  image = models.ImageField(upload_to=app_image_path)
```

​      

---

## 1️⃣ 이미지 업로드

### CREATE

#### 1. URL설정

```python
# settings.py
MEDIA_ROOT = BASE_DIR/'images'
MEDIA_URL = '/media/'
```

```python
# project/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  '...',
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> MEDIA_ROOT

- 사용자가 업로드한 파일들을 포관할 디렉토리의 절대 경로
- django는 성능을 위해 업로드파일을 DB에 저장하지 않음
- DB에는 파일의 경로만 저장됨

> MEDIA_URL

- MEDIA_ROOT에서 제공되는 미디어를 처리해주는 URL
- 업로드된 파일의 URL을 만들어 주는 역할
- 비어있지않은 값으로 설정한다면 반드시 `/`로 끝나야함

​    

#### 2. 모델 설정

```python
# app/models.py
class app(models.Model):
  image = models.ImageField(blank=True, upload_to='image/')
```

> ImageField

- `upload_to = 'images/'` : 실제 이미지가 저장되는 경로 지정
- `blank=True` : 이미지 필드에 빈 값이 허용되도록 설정 

​    

> Model field option : blank & null

1. blank
   - default : False
   - Validation - related
   - True일 경우 필드 비우기 가능, DB에 `''`(빈 문자열) 저장
   - True일 경우 유효성 검사에서 빈 값 입력가능 (is_valid)
2. null
   - default : False
   - Database - related
   - True일 경우 빈 값이 DB에 NULL로 저장
   - 문자열 기반 필드에서는 사용하는 것 지양
   - 문자열 필드에서는 `''`와 NULL의 의미가 달라 서로 다른 취급
   - django에서는 빈 문자열을 주로 사용

​     

#### 3. 마이그레이션

```bash
$ pip install Pillow  # Pillow 라이브러리 설치 필수
$ python manage.py makemigrations
$ python manage.py migrate
```

​    

#### 4. HTML 설정

- form에 `enctype`속성 지정

```html
<!-- app/create.html -->
<form action="" method="" enctype="multipart/form-data">  ✔️✔️
  ...
</form>
```

> enctype 속성

1. `multipart/form-data`
   - 전송되는 데이터의 형식 지정
   - 파일 / 이미지 업로드시에 반드시 사용해야함
   - `<input type="file">` 사용시 활용
2. `application/x-www-form-urlencoded`
   - 모든 문자 인코딩
3. `text/plain`
   - 인코딩 하지 않은 문자 상태로 전송
   - 공백은 `+`로 변환, 특수문자는 인코딩 x

> input의 accept 속성

```html
<input type='file' accept='image/*'>
```

​    

#### 5. View 설정

- 업로드한 파일은 `request.FILES` 객체로 전달됨

```python
# views.py
@require_http_methods(['GET','POST'])
def create(request):
  if request.method == 'POST':
    form = appForm(data=request.POST, files=request.FILES)
    if form.is_valid():
      app.save()
      return redirect('apps:detail', app.pk)
  else:
  	form = appForm()
  context = {
    'form': form,
  }
  return render(request, 'apps/create.html', context)
```

​     

### READ

- img 태그 활용

```html
<!-- detail.html -->
<img src="{{ app.image.url }}" alt="{{ app.image }}"
```

- `src="{{ app.image.url }}"` : 업로드 파일의 경로
- `alt="{{ app.image }}"` : 업로드 파일의 파일 이름

​    

### UPDATE

- 이미지 수정
- 이미지는 바이너리 데이터 (한 덩어리) 이므로 텍스트처럼 일부만 수정하는 것 불가능
- 새로운 사진으로 덮어 씌우는 방식 사용

```python
# view.py
@require_http_methods(['GET','POST'])
def update(request, pk):
  app = get_object_or_404(Mymodel, pk=pk)
  if request.method == 'POST':
    form = appForm(request.POST, request.FILES, instance=app)
    if form.is_valid():
      form.save()
      return redirect('apps:detail', app.pk)
  else:
    form = appForm(instance=app)
  context = {
    'app': app,
    'form': form,
  }
  return render(request, 'apps:update.html', context)
```

​    

---

## 2️⃣ 이미지 Resizing

### Django-imagekit

- 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버에 큰 부담
- 업로드 될 때 이미지 자체를 resizing
- django-imagekit 라이브러리 활용

> [imagekit 문서](https://github.com/matthewwithanm/django-imagekit)

```bash
$ pip install django-imagekit
```

```python
# settings.py
INSTALLED_APP = [
  'imagekit',
]
```

```python
# models.py
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class App(models.Model):
  image = ProcessedImageField(
  	blank = True,
    processors = [Thumbnail(200, 300)],
    format = 'JPEG',
    options = {'quality': 90},
  )
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

> ProcessedImageField의 parameter 로 작성된 값들은 변경이 되더라도 다시makemigrations 를 해줄 필요없이 즉시 반영