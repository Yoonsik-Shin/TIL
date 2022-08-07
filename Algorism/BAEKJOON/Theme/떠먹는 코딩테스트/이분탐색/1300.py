# https://www.acmicpc.net/problem/1300 / K번째 수

# my
N = int(input())
K = int(input())

lst = []

for i in range(1, N+1):
    for j in range(1, N+1):
        lst.append(i*j)

lst.sort()
print(lst[K-1])

