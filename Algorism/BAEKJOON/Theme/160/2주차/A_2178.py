N, M = map(int,input().split())
matrix = [[] for _ in range(N)]
print(matrix)

for i in range(N):
  for j in input():
    matrix[i].append(int(j))
print(matrix)

row_r = [0, 1, -1]
col_r = [1, 0, 0]

row_d = [1, 0, -1]
col_d = [0, 1, 0]

def search_right(matrix):
  start_row = 0
  start_col = 0
  count = 1
  matrix[start_row][start_col] = 0

  while True:
    for k in range(3):
      adj_row = start_row + row_r[k]
      adj_col = start_col + col_r[k]

      if adj_row == N and adj_col == M:
        count += 1
        return count

      if adj_row >= 0 and adj_row < N and adj_col >= 0 and adj_col < M:
        if matrix[adj_row][adj_col] == 1:
          matrix[adj_row][adj_col] = 0
          start_row = adj_row
          start_col = adj_col
          count += 1

search_right(matrix)