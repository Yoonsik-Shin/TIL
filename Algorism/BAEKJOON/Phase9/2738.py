N, M = map(int,input().split())

matrix_N = [list(map(int,input().split())) for _ in range(N)]
matrix_M = [list(map(int,input().split())) for _ in range(N)]
matrix_ans = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        matrix_ans[i][j] = matrix_N[i][j] + matrix_M[i][j]
        print(matrix_ans[i][j], end=' ')
    print()