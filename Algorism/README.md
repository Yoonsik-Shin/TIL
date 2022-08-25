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

