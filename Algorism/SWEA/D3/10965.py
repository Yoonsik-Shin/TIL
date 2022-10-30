from math import sqrt
lst = []
T = int(input())
for _ in range(1, T+1):
    A = int(input())
    B = 1
    
    while True:
        C = A*B
        sqrt_C = int(sqrt(A*B))
        if sqrt_C**2 == C:
            lst.append(B)
            break
        else:
            B+=1

for t in range(1, T+1):
    print(f'#{t} {lst[t-1]}')