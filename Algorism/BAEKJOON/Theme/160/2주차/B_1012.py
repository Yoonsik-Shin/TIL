def dfs(y, x):
  if y < 0 | y >= N | x < 0 | x >= M:
    return False
  
  if matrix[y][x] == 1:
    matrix[y][x] = 0

    dfs(y-1, x) # 하
    dfs(y, x-1) # 좌
    dfs(y+1, x) # 상
    dfs(y, x+1) # 우

    return True
  return False  


T = int(input())

for t in range(T):
  M, N, K = map(int,input().split())
  matrix = [[0] * M for _ in range(N)]

  for i in range(K):
    X, Y = map(int,input().split())
    matrix[Y][X] = 1

  total = 0
  for row in range(N):
    for col in range(M):
      if dfs(row, col) == True:
        total += 1
  
  print(total)
