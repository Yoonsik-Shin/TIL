from collections import deque

N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
  a, b = map(int,input().split())
  graph[a].append(b)

print(graph)
visited = []

def DFS(cur_v):
  visited.append(cur_v)
  print(cur_v, end=' ')
  for v in graph[cur_v]:
    if v not in visited:
      DFS(v)

def BFS(graph, start_v):
  visited = [start_v]
  queue = deque()
  queue.append(start_v)
  print(start_v, end=' ')
  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]:
      if v not in visited:
        queue.append(v)
        visited.append(v)
        print(v, end=' ')

DFS(V)
print()
BFS(graph, V)

