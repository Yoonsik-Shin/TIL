# N, M = map(int,input().split())
# lst = []
# visited = [0] * (N+1)

# def recur(num):

#     if num == M:
#         print(' '.join(map(str,lst)))

#     for i in range(1, N+1):
#         if visited[i] == 0:
#             visited[i] = 1
#             lst.append(i)
#             recur(num+1)
#             visited[i] = 0
#             lst.pop()

# recur(0)

from itertools import combinations

lst = []
n, m = map(int, input().split())

for i in combinations(range(1, n+1), m):
    lst.append(i)

for i in lst:
    print(*i, sep=' ')