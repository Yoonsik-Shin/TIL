x = input()
lst = []

for i in x:
    lst.append(ord(i)-64)

for j in lst:   
    print(j, end=' ')