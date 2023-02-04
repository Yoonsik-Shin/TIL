# 문제풀이로 획득한 개념 총정리

| Site     | README                           |
| -------- | -------------------------------- |
| BAEKJOON | [BAEKJOON](./BAEKJOON/README.md) |
| Codeup   | [Codeup](./Codeup/README.md)     |
| SWEA     | [SWEA](./SWEA/README.md)         |

```python
# startswith 메소드
>> 문자열의 시작 or 끝 조건을 판단
# startswith(시작하는 문자열, 시작지점)
string = 'hello world!'

string.startswith('hello')
>> True

# 튜플 활용
tuple_string = ('hello', 'bye')
string.startswith(tuple_string)
>> True
```

```python
# endswith 메소드
```

```python
# zip함수
a_lst = [1,2,3]
b_lst = ['a','b','c']
c_lst = ['A','B','C']

for i, j, k in zip(a_lst, b_lst, c_lst):
    print(i, j, k)
    
>> 1, 'a', 'A'
>> 2, 'b', 'B'
>> 3, 'c', 'C'
```

```python
# 표준모듈
import math
math.pi()
math.log()

import itertools
itertools.combinations(배열, 뽑을갯수) # 조합
itertools.combinateions_with_replacement() # 중복조합
itertools.permutations() # 순열
itertools.product(배열, 배열) # 가능한 모든 순서쌍
```

```python
# unpacking을 이용한 복사
a = {1: '신', 2: '윤', 3: '식'}
b = {**a}

a[1] = '갓'
print(a)  # {1: '갓', 2: '윤', 3: '식'}
print(b)  # {1: '신', 2: '윤', 3: '식'}
```



