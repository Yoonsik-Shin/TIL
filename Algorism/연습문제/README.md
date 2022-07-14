# 💯 다시볼만한 개념

```python
# 8번 문제 해설
numbers = [0, 20, 100, 40]"
max_number = numbers[0] # 가장 작은 수 : float("-inf")
second_number = numbers[0]

for n in numbers:
    if max_number < n:
        second_number = max_number # 최대값이었던 것이 두번째로 큰 수
        max_number = n
    elif second_number < n and max_number > n:
        second_number = n
        
print(second_number)

# 두번째로 큰 수는 최대값과 바뀔때 이전에 최대값이었던 값 
# 가장 작은 수 : float("-inf")
```

```python
# 17번 문제 개념
print(ord('아스키코드'))
>> 아스키코드 번호

print(chr('아스키코드 번호'))
>> 아스키코드
```

```python
# 18번 문제 개념
'''
세트로 중복을 처리하면 원하는 순서대로 배열을 출력할 수 없음
'''
# 리스트 중복 제거 방법 (for활용)
for i in word:
    if i not in lst: ✔️✔️
        lst.append(i)
```

