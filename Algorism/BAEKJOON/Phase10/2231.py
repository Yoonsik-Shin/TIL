N = int(input())
lst = []

for i in range(1, N):
    k = i
    for j in range(len(str(i))):
        k = k + int(str(i)[j])
    if k == N:
        lst.append(i)

if len(lst) == 0:
    print(0)
else:
    print(lst[0])


# 더 괜찮은 풀이
N = int(input())
result = 0
for i in range(1, N+1):  
    A = list(map(int, str(i)))
    result = i + sum(A)
    if result == N:
        print(i)
        break

    if i==N: #6
        print(0)