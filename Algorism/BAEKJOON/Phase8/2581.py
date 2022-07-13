M = int(input())
N = int(input())
lst = list(range(M,N+1))
lst2 = []

for i in lst:
    error = 0
    for j in range(2,i+1):
        if i%j == 0:
            error+=1
    if error == 1:
        lst2.append(i)
        
if len(lst2) == 0:
    print('-1')
else:
    print(sum(lst2))
    print(min(lst2))