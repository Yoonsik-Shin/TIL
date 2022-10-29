N, M = map(int,input().split())
r, c, d = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]

print(matrix)

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

print(matrix[r][c])
print(d)

while True:
    matrix[r][c] = 1
    d -= 1

    adj_row = r + row[d%4]
    adj_col = c + col[d%4]

    if adj_col >= 0 and adj_col < M and adj_row >= 0 and adj_row < N :
        if matrix[adj_row][adj_col] == 0:
            r = adj_row
            c = adj_col