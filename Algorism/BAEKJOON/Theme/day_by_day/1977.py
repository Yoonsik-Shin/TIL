from math import sqrt

M = int(input())
N = int(input())
lst = []
sqrt_M = sqrt(M)
sqrt_N = sqrt(N)

for i in range(round(sqrt_M), round(sqrt_N)+1):
    if M <= i**2 and N >= i**2:
        lst.append(i**2)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(lst[0])