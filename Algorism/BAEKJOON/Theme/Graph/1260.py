from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def problem():
  n, m, v = map(int,input().split())
  graph_dfs = [[] for _ in range(n+1)]
  visited_dfs = [0] * (n+1)
  visited_dfs_order = []

  graph_bfs = [[] for _ in range(n+1)]
  visited_bfs = [0] * (n+1)
  visited_bfs_order = []

  for i in range(m):
    a, b = map(int,input().split())
    graph_dfs[a].append(b)
    graph_dfs[b].append(a)
    graph_bfs[a].append(b)
    graph_bfs[b].append(a)

  for j in range(1, n+1):
    graph_dfs[j].sort()
    graph_bfs[j].sort()

  def dfs(v):
    visited_dfs[v] = 1
    visited_dfs_order.append(v)
    for k in graph_dfs[v]:
      if not visited_dfs[k]:
        dfs(k)
    return visited_dfs_order

  def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
      o = queue.popleft()
      if not visited_bfs[o]:
        visited_bfs[o] = 1
        visited_bfs_order.append(o)
        for q in graph_bfs[o]:
          queue.append(q)
    return visited_bfs_order

  print(*dfs(v))
  print(*bfs(v))

problem()