N = int(input())

matrix = [input() for _ in range(N)]
print(matrix)
count = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] == '#':
            x = i
            adj_col = j+1
            if adj_col < N:
                if matrix[i][adj_col] == '#':
                    count += 1
                else:
                    continue
        a = True
        for k in range(count):
            if a == False:
                break
            else:
                adj_row = x + k
                if adj_row < N:
                    for l in range(count):
                        adj_col2 = j + l
                        if matrix[adj_row][adj_col2] == '#':
                            a = True
                        else:
                            a = False
                            break
    count = 0
    print(a)