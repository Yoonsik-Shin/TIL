from collections import deque

n = int(input())
m = int(input())
count = 0
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1) 

for i in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(v):
  queue = deque()
  queue.append(v)

  while queue:
    c = queue.popleft()
    if visited[c] == 0:
      visited[c] = 1
      for j in graph[c]:
        queue.append(j)

  return visited

print(sum(bfs(1)) - 1)