n = int(input())
lst = list(map(int,input().split()))
d = []

for i in range(24):
    d.append(0)

for j in range(n):
    d[lst[j]] += 1

for k in range(1, 24):
    print(d[k], end=' ')