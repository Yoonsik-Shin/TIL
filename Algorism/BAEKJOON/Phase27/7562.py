from collections import deque

T = int(input())
# 시계 방향
dr = [-2, -1, 1, 2,  2,  1, -1,  -2]
dc = [ 1,  2, 2, 1, -1, -2, -2, -1]

def bfs(sr, sc, er, ec, i):
  queue = deque()
  queue.append((sr, sc))
  min_move = 1e19
  visited[sr][sc] = 1

  while queue:
    cr, cc = queue.popleft()

    for d in range(8):
      nr = cr + dr[d]
      nc = cc + dc[d]

      if nr < 0 or nr >= i or nc < 0 or nc >= i: continue 
      if not visited[nr][nc]:
        visited[nr][nc] = visited[cr][cc] + 1
        if nr == er and nc == ec:
          min_move = min(min_move, visited[nr][nc] - 1)
        queue.append((nr, nc))
  return min_move

for _ in range(T):
  i = int(input())
  sr, sc = map(int,input().split())
  er, ec = map(int,input().split())
  visited = [[0]*i for _ in range(i)]

  ans = bfs(sr, sc, er, ec, i)
  if ans == 1e19: print(0)
  else: print(ans)