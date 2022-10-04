# Django 개념

​    

## ModelForm

### 생성

```python
# 앱/forms.py

from django import forms
from .models import 앱

class 앱폼(forms.ModelForm):
  
  class Meta:
    model = 앱
    fields = '__all__'
```

- forms 라이브러리의 ModelForm 클래스 상속
- Meta 클래스 선언

​    

> Meta Class

- ModelForm의 정보를 작성하는 곳
- 참조하는 모델에 정의된 field 정보를 Form에 적용

```python
# 앱/forms.py

class 앱폼(forms.ModelForm):
  
   class Meta:
    model = 앱
    fields = '__all__'            # 모델의 모든 필드 포함
    exclude = (포함하지 않을 값,)   # 모델에서 사용하지 않을 필드 지정
```



### 활용

1. ModelForm 객체를 context로 전달

```python
# 앱/views.py

from .forms import 앱폼

def new(request):
  form = 앱폼()
  
  context = {
    'form': form,
  }
  
  return render(request, '앱/new.html', context)
```

2. Input Field 활용 (Html)

```html
<!-- 앱/new.html -->
<form action="{% url '앱:create' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
</form>
```

​    

> Form rendering options

1. `as_p()`
   - 각필드가 `<p>` 로 감싸져 렌더링
2. `as_ul()`
   - 각 필드가 `<li>` 로 감싸져 렌더링
   - `<ul>` 태그는 직접 작성해야 함
3. `as_table`() 
   - 각 필드가 `<tr>` 로 감싸져 렌더링

​    

 ### 로직

1. 요청 방식에 따른 분기
   - GET/POST
2. 유효성 검사에 따른 분기
   - 실패시 다시 Form으로 전달
   - 성공시 DB저장



### CREATE

```python
# 앱/views.py

def create(request):
  form = 앱폼(request.POST)
  if form.is_valid():
    acticle = form.save()
    return redirect('앱:detail', 앱.pk)  # 유효성 검사 통과시 : 데이터 저장 후 상세페이지로 redirect
 	print( {form.error} )    #
  return redirect('앱:new')              # 유효성 검사 통과 실패시 : 작성 페이지로 redirect
```

​    

####  `is_valid()` 

- 유효성 검사를 실행하고, 데이터가 유효한지 여부를 __boolean__ 형태로 반환

> `error` 속성

- is.valid()의 반환 값이 False일 경우, form 인스턴스의 errors 속성에 유효성 검증 실패 원인이 딕셔너리 형태로 저장됨
- 유효성 검증 실패시 사용자에게 실패 결과 메시지 출력할 때 사용

​     

#### `save()`

- form 인스턴스에 바인딩된 데이터를 통해 DB객체를 만들고 저장
- `instance` 여부로 생성/ 수정 여부 결정

```python
# CREATE
form = 앱폼(request.POST)                # 인스턴스 X
form.save()

# UPDATE
form = 앱폼(request.POST, instance=앱)    # 인스턴스 O
form.save()
```

​     

### UPDATE



