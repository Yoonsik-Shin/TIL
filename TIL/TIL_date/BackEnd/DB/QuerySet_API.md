# QuerySet API

​    

## 0️⃣ QuerySet 개념

- Django ORM에서 제공하는 데이터 타입
- 데이터베이스에서 전달받은 객체 목록
- 구조는 List형태와 같지만 파이썬 파일에서 읽고 쓰기 위해서는 자료형 변환을 해줘야함

​    

## 1️⃣ QuerySet 종류

> 출처 : [잘 정리된 블로그](https://devvvyang.tistory.com/37)

### 1. SELECT

1. <Class_name>.object.all()

- 테이블 안에 있는 모든 데이터 조회
- QuerySet형태로 반환 

​    

2. <Class_name>.object.get()

- 하나의 row만 조회
- 주로 PK컬럼으로 조회 (`.get(id=1)`)
- ❗결과가 1건 초과일때 에러 발생❗
- ❗객체 타입으로 반환 (QuerySet 형태 x)❗

​    

3. <Class_name>.objects.filter()

- 특정 조건에 맞는 row만 조회하고 싶을 때
- QuerySet형태로 반환

​    

4. <Class_name>.objects.exclude()

- 특정 조건을 제외한 데이터만 조회하고 싶을 때 (filter와 반대)
- QuerySet형태로 반환

​    

---

#### ♾️ Lookup filter

- filter(), exclude() 메소드에서 사용가능한 내장 모듈
- 필드 별 구체적인 값에 대한 비교를 가능하게하는 Django 내장 모듈

​    

1. __contains

   - 특정 문자가 포함된 것을 찾을 때 (❗대소문자 구분 o)

   ```django
   <Class_name>.object.filter(<column_name>__contains='특정문자')
   ```

2. __icontains

   - 특정 문자가 포함된 것을 찾을 때 (❗대소문자 구분x)

   ```django
   <Class_name>.object.filter(<column_name>__icontains='특정문자')
   ```

3. __startswith

   - 특정 문자로 시작하는 것을 찾을 때 (❗대소문자 구분 o)

   ```django
   <Class_name>.object.filter(<column_name>__startswith='특정문자')
   ```

4. __endswith

   - 특정 문자로 끝나는 것을 찾을 때(❗대소문자 구분 x)

   ```django
   <Class_name>.object.filter(<column_name>__endswith='특정문자')
   ```

5. __gt

   - 특정 값보다 큰 데이터만 조회 (Greater than의 약자)

   ```django
   <Class_name>.object.filter(<column_name>__gt=3)
   ```

6. __gte

   - 특정 값보다 크거나 같은 데이터만 조회 (Greater than equal의 약자)

   ```django
   <Class_name>.object.filter(<column_name>__gte=3)
   ```

7. __lt

   - 특정값보다 작은 데이터만 조회 (Less than의 약자)

   ```django
   <Class_name>.object.filter(<column_name>__lt=3)
   ```

8. __lte

   - 특정값보다 작거나 같은 데이터만 조회 (Less than equal의 약자)

   ```django
   <Class_name>.object.filter(<column_name>__lte=3)
   ```

9. __isnull

   - True로 지정시 특정필드값이 null인 것만 조회

   ```django
   # null인 것만 조회
   <Class_name>.object.filter(<column_name>__isnull=True)
     
   # null이 아닌 것만 조회
   <Class_name>.object.filter(<column_name>__isnull=False)
   ```

10. __in

    - 리스트안에 지정한 문자열들 중 하나라도 포함된 데이터를 찾을 때 사용
    - 단, 문자열이 정확히 일치해야함

    ```django
    # a 또는 b 값이 있는 것만 조회
    <Class_name>.object.filter(<column_name>__in=['a', 'b'])
    ```

11. \__year / \__month / \__day / __date

    - date타입 필드에서 특정 년, 월, 일 혹은 특정 날짜 (__date : YY-MM-DD)의 데이터 조회

    ```django
    <Class_name>.objects.filter(<column_name>__year=2022)
    <Class_name>.objects.filter(<column_name>__month=8)
    <Class_name>.objects.filter(<column_name>__day=25)
    <Class_name>.objects.filter(<column_name>__date=datetime.date(2022, 8, 25))
    ```

​    

> AND / OR

- filter() 메소드 사용 시, 두개 이상의 조건을 AND 또는 OR로 표현가능

1. AND : `&` / OR : `|`

```django
# AND 조건
<Class_name>.object.filter(<column_name>__gt=6) & <Class_name>.object.filter(<column_name>__lt=5)
  
# OR 조건
<Class_name>.object.filter(<column_name>__gt=6) | <Class_name>.object.filter(<column_name>__lt=5)
```

2. Q 객체 활용

```django
from django.db.models import Q
<Class_name>.object.filter(Q(<column_name>__gt=6) & Q(<column_name>__lt=5))
<Class_name>.object.filter(Q(<column_name>__gt=6) | Q(<column_name>__lt=5))
```

---

​    

5. <Class_name>.objects.count()

- 쿼리 셋에 포함된 데이터 개수 리턴

​    

6. <Class_name>.objects.exists()

- 해당 테이블에 데이터가 있는지 확인 (True / False)

```django
IN : <Class_name>.objects.filter(<column_name>='').exist()
OUT : True 
```

​    

7. <Class_name>.objects.values()

- QuerySet 내용을 딕셔너리 형태로 반환
- 인자값 x : 모든 필드를 딕셔너리 형태로 반환
- 인자값 o : 해당 컬럼만 딕셔너리 형태로 반환

```django
# 인자값 x
IN : <Class_name>.objects.values()
OUT : <QuerySet [{'id': 1, 'name': '두현'}, {'id': 2, 'name': '민영'}]>
  
# 인자값 o
IN : <Class_name>.objects.values('name')
OUT : <QuerySet [{'name': '두현'}, {'name': '민영'}]>
```

​    

8. <Class_name>.objects.values_list()

- QuerySet 내용을 리스트 타입으로 반환

```django
# 인자값 x
IN : <Class_name>.objects.values()
OUT : <QuerySet [(1, '민수'), (2, '민영')]>
  
# 인자값 o
IN : <Class_name>.objects.values('name')
OUT : <QuerySet [('민수', ), ('민영', )]>
```

​    

9. <Class_name>.objects.order_by()

```django
# 오름차순
<Class_name>.objects.order_by('<column_name1>', '<column_name2>')

# 내림차순
<Class_name>.objects.order_by('-<column_name1>')
```

​    

10. <Class_name>.objects.first() / <Class_name>.objects.last()

- 쿼리셋 결과 중 가장 첫번째 / 마지막 row만 조회할 때 사용
- 객체 타입 반환

```django
# 전체 조회
In : Drink.objects.all()
Out: <QuerySet [<Drink: 나이트로 바닐라 크림>, <Drink: 나이트로 쇼콜라 클라우드>, <Drink: 망고 패션 후르츠 블렌디드>, <Drink: 딸기 요거트 블렌디드>, <Drink: 블랙 티 레모네이드>, <Drink: 쿨라임 피지오>, <Drink: 말차 초콜릿 라떼>, <Drink: 라임패션티>]>

# 가장 첫번째 row만 조회
In : Drink.objects.first()
Out: <Drink: 나이트로 바닐라 크림>

# 가장 마지막 row만 조회
In : Drink.objects.last()
Out: <Drink: 라임패션티>
```

​    

11.  <Class_name>.objects.aggregate()

- django의 집계함수 모듈 사용시 사용하는 메소드
- 집계함수의 파라미터로 받음
- 딕셔너리 타입 반환

```django
# 집계함수를 사용하려면 import 해줘야 함
In : from django.db.models import Max, Min, Avg, Sum

# Nutrition 테이블의 id 컬럼과 one_serving_kcal 컬럼만 조회
In : Nutrition.objects.values('id','one_serving_kcal')
Out: <QuerySet [{'id': 1, 'one_serving_kcal': Decimal('75.00')}, {'id': 2, 'one_serving_kcal': Decimal('120.00')}]>

# one_serving_kcal 값 모두 더하기
In : Nutrition.objects.aggregate(Sum('one_serving_kcal'))
Out: {'one_serving_kcal__sum': Decimal('195.00')}

# one_serving_kcal컬럼에서 가장 큰 값과 가장 작은 값의 차이
In : Nutrition.objects.aggregate(diff_kcal = Max('one_serving_kcal') - Min('one_serving_kcal'))
Out: {'diff_kcal': Decimal('45.00')}

# one_serving_kcal 컬럼 값들의 평균
In : Nutrition.objects.aggregate(avg_kcal = Avg('one_serving_kcal'))
Out: {'avg_kcal': Decimal('97.500000')}
```

​    

12. <Class_name>.objects.annotate()

- 각 컬럼별 주석을 달고 집계함수를 사용하여 반환
- SQL의 group by절과 같은 의미
- QuerySet형태로 반환

```django
In : Nutrition.objects.values('drink_id__category_id').annotate(Sum('one_serving_kcal'))
Out: <QuerySet [{'drink_id__category_id': 1, 'one_serving_kcal__sum': Decimal('80.00')}, {'drink_id__category_id': 2, 'one_serving_kcal__sum': Decimal('410.00')}, {'drink_id__category_id': 3, 'one_serving_kcal__sum': Decimal('170.00')}, {'drink_id__category_id': 4, 'one_serving_kcal__sum': Decimal('425.00')}]>
```

​    

>Chaining Methods

- 여러 메소드를 `.`로 연결하여 사용 가능

```django
# filter와 count 메소드를 함께 사용
In : Drink.objects.filter(category_id=2).count()
Out: 2
```

​    

> Slicing

- 쿼리셋 결과를 인덱스의 슬라이싱처럼 사용

```django
In : Drink.objects.all()[3:5]
Out: <QuerySet [<Drink: 딸기 요거트 블렌디드>, <Drink: 블랙 티 레모네이드>]>
```

​    

---

### 2. Insert

2-1. <Class_name>.objects.__create()__

```django
In : Nutrition.objects.create(one_serving_kcal=120, sodium_mg=70, saturated_fat_g=0, sugers_g=25, protei
    ...: n_g=1, caffeine_mg=35, drink_id=3, size="Tall(톨)", size_fluid_ounce=355, size_ml=12)
Out: <Nutrition: 망고 패션 후르츠 블렌디드 nutritions>
```

​    

2-2. <Class_name>.objects.**bulk_create()**

- 여러개의 object를 한꺼번에 생성할 때 사용

```django
In : Nutrition.objects.bulk_create([
    ...: ...     Nutrition(one_serving_kcal = 5, sodium_mg = 5, saturated_fat_g = 0, sugers_g = 0, protein_g
    ...:  = 0, caffeine_mg = 245, drink_id = 2, size = 'Tall(톨)', size_fluid_ounce = 355, size_ml = 12),
    ...: ...     Nutrition(one_serving_kcal = 290, sodium_mg = 110, saturated_fat_g = 0.9, sugers_g = 57, pr
    ...: otein_g = 8, caffeine_mg = 0, drink_id = 4, size = 'Tall(톨)', size_fluid_ounce = 355, size_ml = 12
    ...: ),
    ...:  ^I    Nutrition(one_serving_kcal = 65, sodium_mg = 0, saturated_fat_g = 0, sugers_g = 17, protein_
    ...: g = 0, caffeine_mg = 30, drink_id = 5, size = 'Tall(톨)', size_fluid_ounce = 355, size_ml = 12),
    ...: ...     Nutrition(one_serving_kcal = 105, sodium_mg = 20, saturated_fat_g = 0, sugers_g = 26, prote
    ...: in_g = 0, caffeine_mg = 110, drink_id = 6, size = 'Tall(톨)', size_fluid_ounce = 355, size_ml = 12)
    ...: ... ])

Out:
[<Nutrition: 나이트로 쇼콜라 클라우드 nutritions>,
 <Nutrition: 딸기 요거트 블렌디드 nutritions>]
```

​    

2-3. <Class_name>.objects.__get_or_create()__

- 테이블에 조건에 맞는 데이터가 이미 존재하면 `get`해오고, 없으면 `create`하는 메소드
- 튜플 타입으로 반환 (True/False)
- get >> False / create >> True
- create된 값들은 빈칸, null, default값등이 자동으로 채워짐

```django
# 이미 존재하는 데이터를 get_or_create 했을 때
In : Drink.objects.filter(korean_name='나이트로 쇼콜라 클라우드')
Out: <QuerySet [<Drink: 나이트로 쇼콜라 클라우드>]>

In : new_drink = Drink.objects.get_or_create(korean_name='나이트로 쇼콜라 클라우드')

# 기존에 있는 데이터 반환
In : new_drink
Out: (<Drink: 나이트로 쇼콜라 클라우드>, False)

# 없는 데이터를 get_or_create 했을 때
In : Drink.objects.filter(korean_name='new')
Out: <QuerySet []>

In : new_drink
Out: (<Drink: new>, True)

# 새로 추가된 것을 확인할 수 있다.
In : Drink.objects.filter(korean_name='new')
Out: <QuerySet [<Drink: new>]>
```

​    

### 3. Update

#### 3-1. 방법1

- 업데이트할 row를 변수에 저장한 후, 그 변수에서 각 필드에 접근하여 값을 변경해주기
- 반드시 `.save()`를 해줘야 변경사항이 저장됨

```django
a = Drink.objects.get(id=8)

In : a
Out: <Drink: 라임패션티>

# id가 8인 row의 description 컬럼 값을 'Lime Passion 2'로 업데이트
In : a.description = "Lime Passion 2"

# 변경사항 저장 >> 실제 DB에 적용됨
In : a.save()

# 결과 확인
In : Drink.objects.values('id','description').filter(id=8)
Out: <QuerySet [{'id': 8, 'description': 'Lime Passion 2'}]>
```

​    

#### 3-2. 방법2

- `Filter().update()`

```django
# filter로 조건을 걸고(id=8) 그 row의 특정 컬럼(discription) 값을 update
In : Drink.objects.filter(id=8).update(description = "Lime Passion 3")
Out: 1

# 결과 확인
In : Drink.objects.values('id','description').filter(id=8)
Out: <QuerySet [{'id': 8, 'description': 'Lime Passion 3'}]>
```

​    

---

### 4. Delete

- 삭제할 row를 변수에 저장하고 그 변수에 `.delete`메소드를 사용

```django
# 처음 데이터 확인
In : Menu.objects.all()
Out: <QuerySet [<Menu: 음료>, <Menu: 푸드>, <Menu: 상품>, <Menu: 카드>, <Menu: MD>]>

# 변수에 저장
In : a = Menu.objects.get(id=5)

# 삭제
In : a.delete()
Out: (1, {'products.Menu': 1})

# 결과 확인
In : Menu.objects.all()
Out: <QuerySet [<Menu: 음료>, <Menu: 푸드>, <Menu: 상품>, <Menu: 카드>]>
```

