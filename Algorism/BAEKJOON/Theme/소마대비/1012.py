import sys
sys.setrecursionlimit(10**6)

def dfs(cr, cc):
  visited[cr][cc] = 1

  for d in range(4):
    nr = cr + dr[d]
    nc = cc + dc[d]

    if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
    if not visited[nr][nc] and matrix[nr][nc] == 1:
      dfs(nr, nc)

t = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for _ in range(t):
  m, n, k = map(int,input().split())
  matrix = [[0] * m for _ in range(n)]
  visited = [[0] * m for _ in range(n)]
  count = 0

  for _ in range(k):
    x, y = map(int,input().split())
    matrix[y][x] = 1

  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 1 and not visited[i][j]:
        dfs(i, j)
        count += 1
  print(count)