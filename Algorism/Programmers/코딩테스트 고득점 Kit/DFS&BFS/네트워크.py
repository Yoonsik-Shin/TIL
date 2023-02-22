def solution(n, computers):
  lst = [[] for _ in range(n+1)]
  visited = [0] * (n+1)
  count = 0

  for i in range(1, n+1):
    for j in range(i+1, n+1):
      if i == j: continue
      if computers[i-1][j-1] == 1:
        lst[i].append(j)
        lst[j].append(i)

  def dfs(start):
    visited[start] = 1
    for i in lst[start]:
      if not visited[i]:
        dfs(i)
        
  for p in range(1, n+1):
    if not visited[p]:
      dfs(p)
      count += 1

  return count

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))