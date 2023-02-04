import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs_order():  
  n, m, r = map(int,input().split())  
  graph = [[] for _ in range(n+1)]
  visited = [0] * (n+1)

  for i in range(m):
    u, v = map(int,input().split())  
    graph[u].append(v)
    graph[v].append(u)
  
  for j in range(1, n+1):
    graph[j].sort()

  def dfs(r):
    global count
    visited[r] = count
    for k in graph[r]:
      if visited[k] == 0:
        count += 1
        dfs(k)    
  
  dfs(r)

  for o in range(1, n+1):
    print(visited[o])

  return

count = 1
dfs_order()