# https://www.acmicpc.net/problem/2178

from collections import deque

N, M = map(int,input().split())
matrix = [[] for _ in range(N)]

for i in range(N):
  for j in input():
    matrix[i].append(int(j))

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
queue = deque()
queue.append([0, 0])

while queue:
  [cur_row, cur_col] = queue.popleft() 

  for k in range(4):
    adj_row = cur_row + row[k]
    adj_col = cur_col + col[k]

    if adj_row >= 0 and adj_row < N and adj_col >= 0 and adj_col < M:
      if matrix[adj_row][adj_col] == 1:
        queue.append([adj_row, adj_col])
        matrix[adj_row][adj_col] = matrix[cur_row][cur_col] + 1

print(matrix[N-1][M-1])