import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  dr = [0, 1, 0, -1]
  dc = [1, 0, -1, 0]

  while queue:
    cr, cc = queue.popleft()
    
    for d in range(4):
      nr = cr + dr[d]
      nc = cc + dc[d]

      if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
      if box[nr][nc] == 0:
        box[nr][nc] = box[cr][cc] + 1
        queue.append((nr, nc))

m, n = map(int,input().split())

box = [list(map(int,input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      queue.append((i, j))

bfs()

check = True
for i in range(n):
  if check == True:
    for j in range(m):
      if box[i][j] == 0:
        check = False
        print(-1)
        break
  else:
    break
else:
  print(max([max(r) for r in box]) - 1)