for t in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    table1 = [[0]*N for _ in range(N)]
    table2 = [[0]*N for _ in range(N)]
    table3 = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            table1[j][N-1-i] = matrix[i][j]
            table2[N-1-i][N-1-j] = matrix[i][j]
            table3[N-1-j][i] = matrix[i][j]

    print(f'#{t}')
    for m in range(N):
        print(''.join(map(str,table1[m])), end=' ')
        print(''.join(map(str,table2[m])), end=' ')
        print(''.join(map(str,table3[m])), end=' ')
        print()