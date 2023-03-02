import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, depth):
  queue = deque()
  queue.append((start, depth))
  visited[start] = 1

  while queue:
    c, dep = queue.popleft()
    for node in nodes[c]:
      if not visited[node]:
        visited[node] = 1
        if dep + 1 == k:
          ans_lst.append(node)
          continue
        queue.append((node, dep+1))

n, m, k, x = map(int, input().split())
visited = [0] * (n+1)
ans_lst = []
nodes = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  nodes[a].append(b)

bfs(x, 0)

if len(ans_lst) == 0:
  print(-1)
else:
  ans_lst.sort()
  for ans in ans_lst:
    print(ans)