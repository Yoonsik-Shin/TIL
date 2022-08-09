from pprint import pprint

N, M = map(int, input().split())
matrix = [[0] * 7 for _ in range(7)]
lst =  [[] for _ in range(7)]

for i in range(M):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1
    lst[u].append(v)
    lst[v].append(u)

pprint(matrix)
print(lst)