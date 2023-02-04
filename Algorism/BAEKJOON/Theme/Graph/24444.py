from collections import deque
import sys
input = sys.stdin.readline

def bfs_order():  
  n, m, r = map(int,input().split())
  
  graph = [[] for _ in range(n+1)]
  visited = [0] * (n+1)

  for i in range(m):
    u, v = map(int,input().split())  
    graph[u].append(v)
    graph[v].append(u)
  
  for j in range(1, n+1):
    graph[j].sort()

  def bfs(r):
    global count
    queue = deque()
    queue.append(r)

    while queue:
      k = queue.popleft()
      if visited[k] == 0:
        visited[k] = count
        count += 1
        for o in graph[k]:
          queue.append(o)

  bfs(r)

  for o in range(1, n+1):
    print(visited[o])

  return

count = 1
bfs_order()