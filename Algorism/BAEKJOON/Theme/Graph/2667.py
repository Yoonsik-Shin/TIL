from collections import deque

def bfs(row, col):
  queue = deque()
  queue.append((row, col))
  boundary_sum = 1
  visited[row][col] = 1

  while queue:
    cr, cc = queue.popleft()

    for d in range(4):
      nr = cr + dr[d]
      nc = cc + dc[d]

      if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
      if graph[nr][nc] == 1 and not visited[nr][nc]:
        visited[nr][nc] = 1
        boundary_sum += 1
        queue.append((nr, nc))
  
  return boundary_sum

n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
count_sum = []
count = 0

for _ in range(n):
  lst = list(map(int,input()))
  graph.append(lst)
  
for row in range(n):
  for col in range(n):
    if graph[row][col] == 1 and not visited[row][col]:
      count_sum.append(bfs(row, col))
      count += 1

print(count)
count_sum.sort()
for _ in count_sum:
  print(_)