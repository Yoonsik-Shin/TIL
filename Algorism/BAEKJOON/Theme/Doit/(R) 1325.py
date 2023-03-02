import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, depth):
  visited = set()  
  queue = deque()
  queue.append((start, depth))
  visited.add(start)

  while queue:
    c, dep = queue.popleft()
    for node in nodes[c]:
      if node not in visited:
        visited.add(node)
        queue.append((node, dep+1))

  return dep

n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
ans_lst = []

for _ in range(m):
  a, b = map(int, input().split())
  nodes[b].append(a)

max_dep = 0
for i in range(1, n+1):
  re_dep = bfs(i, 0)
  if re_dep < len(nodes[i]):
    re_dep = len(nodes[i]) 

  if re_dep == 0:
    re_dep = 1

  ans_lst.append((i, re_dep))

  if re_dep > max_dep:
    max_dep = re_dep

for p, q in ans_lst:
  if q == max_dep:
    print(p, end=' ')

