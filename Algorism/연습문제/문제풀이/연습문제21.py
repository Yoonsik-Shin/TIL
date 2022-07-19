number = 1234
lst = []

while number:
    a = number%10
    lst.append(a)
    number //= 10

for i in lst:
    print(i, end='')