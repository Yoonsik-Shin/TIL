# https://www.acmicpc.net/problem/18111

N, M, B = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]
max_matrix = -10000000
min_matrix = 1e9

for row in range(N):
    for col in range(M):
        if matrix[row][col] > max_matrix:
            max_matrix = matrix[row][col]
        if matrix[row][col] < min_matrix:
            min_matrix = matrix[row][col]

check = max_matrix - min_matrix
