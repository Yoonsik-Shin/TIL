for t in range(1, int(input())+1):
    row = [0, 1, 0, -1]
    col = [1, 0, -1, 0]

    N = int(input())
    count = 1
    matrix = [[0]*N for _ in range(N)]

    i = 0
    j = 0
    d = 0

    for _ in range(N*N):
        if i < N and i >= 0 and j < N and j >=0 and matrix[i][j] == 0:
            matrix[i][j] = count
            count += 1
            adj_row = i + row[d%4]
            adj_col = j + col[d%4]
            if adj_row < N and adj_row >= 0 and adj_col < N and adj_col >=0 and matrix[adj_row][adj_col] == 0:
                i = adj_row
                j = adj_col
            else:
                d += 1
                adj_row = i + row[d%4]
                adj_col = j + col[d%4]
                if adj_row < N and adj_row >= 0 and adj_col < N and adj_col >=0 and matrix[adj_row][adj_col] == 0:
                    i = adj_row
                    j = adj_col
    print(f'#{t}')
    for m in range(N):
        for j in range(N):
            print(matrix[m][j], end=' ')
        print()