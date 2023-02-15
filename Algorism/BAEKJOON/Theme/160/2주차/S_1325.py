from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
  visited = [0] * (n+1)
  order = 1
  visited[start] = order
  queue = deque()
  queue.append(start)
  m = 0
  while queue:
    c = queue.popleft()
    if network[c]:
      for j in network[c]:
        if not visited[j]:
          order += 1
          visited[j] = order
          queue.append(j)
          if visited[j] > m:
            m = visited[j]
    else:
      continue
  return m

n, m = map(int,input().split())
network = [[] for _ in range(n+1)]
ans_lst = []
lst = []

for _ in range(m):
  a, b = map(int,input().split())
  network[b].append(a)

max_value = 0
for i in range(1, n+1):
  k = bfs(i)
  ans_lst.append((i, k))
  if k > max_value:
    max_value = k

for a in sorted(ans_lst):
  if a[1] == max_value:
    print(a[0], end=' ')