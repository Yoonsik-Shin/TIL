N, K = map(int,input().split())
lst = []

for i in range(N):
    lst.append(int(input()))

lst = lst[::-1]

count = 0
for j in lst:
    if K // j == 0:
        continue
    else:
        count += (K // j)
        K = K%j
    if K == 0:
        break

print(count)