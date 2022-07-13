# 💯 다시볼만한 개념

```python
# 8번문제 해설
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

