# import sys
# sys.setrecursionlimit(10**7)

def dfs(row, col):
  if row < 0 or row >= N or col < 0 or col >= N:
    return False

  if visited[row][col] != 2:
    visited[row][col] = 0
    dfs(row-1, col) # 하
    dfs(row, col-1) # 좌
    dfs(row+1, col) # 상
    dfs(row, col+1) # 우
    return True
  
  return False

N = int(input())
visited = [[1] * N for _ in range(N)]
matrix = []
for _ in range(N):
  matrix.append(list(map(int,input().split())))

start = 2
total = 0
max_total = -1

while True:

  for i in range(N):
    for j in range(N):
      if matrix[i][j] == start:
        visited[i][j] = 1
      elif visited[i][j] != 1:
        visited[i][j] = 0
  
  for i in range(N):
    for j in range(N):
      if dfs(i, j) == True:
        total += 1
  
  if total < max_total:
    print(max_total)
    break
  else:
    max_total = total
    total = 0
    start += 1