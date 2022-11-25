# 못품

N = int(input())
R = []
G = []
B = []
lst2 = []
total = 0

for _ in range(N):
    lst = list(map(int,input().split()))
    B.append(lst.pop())
    G.append(lst.pop())
    R.append(lst.pop())

lst2.append(R)
lst2.append(G)
lst2.append(B)

for i in range(N-1):
    if total == 0:
        min_a = 1e9
        for j in range(3):
            a = lst2[j][i]
            if a < min_a:
                min_a = a
                b = j
        total += min_a

    if b == 0:
        total += min(lst2[1][i+1], lst2[2][i+1])
        if min(lst2[1][i+1], lst2[2][i+1]) == lst2[1][i+1]: 
            b = 1
        elif min(lst2[1][i+1], lst2[2][i+1]) == lst2[2][i+1]:
            b = 2
    elif b == 1:
        total += min(lst2[0][i+1], lst2[2][i+1])
        if min(lst2[0][i+1], lst2[2][i+1]) == lst2[0][i+1]: 
            b = 0
        elif min(lst2[0][i+1], lst2[2][i+1]) == lst2[2][i+1]: 
            b = 2
    elif b == 2:
        total += min(lst2[1][i+1], lst2[0][i+1])
        if min(lst2[1][i+1], lst2[0][i+1]) == lst2[0][i+1]: 
            b = 0
        elif min(lst2[1][i+1], lst2[0][i+1]) == lst2[1][i+1]:
            b = 1
print(total)