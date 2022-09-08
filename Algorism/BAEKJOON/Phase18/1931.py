# 시간초과

import sys
input = sys.stdin.readline

N = int(input())
visited = [0] * N
lst = []
lst2 = []

for i in range(N):
    lst.append(tuple(map(int,input().split())))

lst.sort()

for j in range(N):
    count = 0
    while True:
        if visited[j] == 1:
            break

        if not visited[j]:
            visited[j] = 1

            a = 1e9
            for k in range(j+1,N):
                if lst[j][1] <= lst[k][0] and a > lst[k][0]:
                    a = lst[k][0]
                    j = k
        count+=1
    lst2.append(count)

print(lst2)