for t in range(1, int(input())+1):
    N, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    total_count = 0

    for i in range(N):
        row_count = 0
        for j in range(N):
            if matrix[i][j] == 1:
                row_count += 1
            else:
                if row_count == K:
                    total_count += 1
                    row_count = 0
                else:
                    row_count = 0
        else:
            if row_count == K:
                total_count += 1
                row_count = 0

    for k in range(N):
        col_count = 0
        for m in range(N):
            if matrix[m][k] == 1:
                col_count += 1
            else:
                if col_count == K:
                    total_count += 1
                    col_count = 0
                else:
                    col_count = 0
        else:
            if col_count == K:
                total_count += 1
                col_count = 0

    print(f'#{t} {total_count}')
