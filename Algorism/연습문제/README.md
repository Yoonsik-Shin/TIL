# π― λ€μλ³Όλ§ν κ°λ

```python
# 8λ² λ¬Έμ  ν΄μ€
numbers = [0, 20, 100, 40]"
max_number = numbers[0] # κ°μ₯ μμ μ : float("-inf")
second_number = numbers[0]

for n in numbers:
    if max_number < n:
        second_number = max_number # μ΅λκ°μ΄μλ κ²μ΄ λλ²μ§Έλ‘ ν° μ
        max_number = n
    elif second_number < n and max_number > n:
        second_number = n
        
print(second_number)

# λλ²μ§Έλ‘ ν° μλ μ΅λκ°κ³Ό λ°λλ μ΄μ μ μ΅λκ°μ΄μλ κ° 
# κ°μ₯ μμ μ : float("-inf")
```

```python
# 17λ² λ¬Έμ  κ°λ
print(ord('μμ€ν€μ½λ'))
>> μμ€ν€μ½λ λ²νΈ

print(chr('μμ€ν€μ½λ λ²νΈ'))
>> μμ€ν€μ½λ
```

```python
# 18λ² λ¬Έμ  κ°λ
'''
μΈνΈλ‘ μ€λ³΅μ μ²λ¦¬νλ©΄ μνλ μμλλ‘ λ°°μ΄μ μΆλ ₯ν  μ μμ
'''
# λ¦¬μ€νΈ μ€λ³΅ μ κ±° λ°©λ² (forνμ©)
for i in word:
    if i not in lst: βοΈβοΈ
        lst.append(i)
```

