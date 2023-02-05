from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]


for _ in range(v):
  lst = deque(map(int,input().split()))
  idx = lst.popleft()
  lst.pop()
  for j in range(0, len(lst), 2):
    graph[idx].append((lst[j], lst[j+1]))

def bfs(start):
  visited = [-1] * (v+1)
  max_length = [0, 0]
  queue = deque()
  queue.append(start)
  visited[start] = 0
  
  while queue:
    c = queue.popleft()
    for e, w in graph[c]:
      if visited[e] == -1:
        visited[e] = visited[c] + w
        queue.append(e)
        if max_length[0] < visited[e]:
          max_length = visited[e], e
  
  return max_length

a, b = bfs(1)
a, b = bfs(b)
print(a)