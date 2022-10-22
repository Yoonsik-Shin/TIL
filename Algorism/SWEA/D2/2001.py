T = int(input())

for t in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    parry = 0

    for k in range(N-M+1):
        for o in range(N-M+1):
            for i in range(k, k+M):
                for j in range(o, o+M):
                    parry += matrix[i][j]
            lst.append(parry)
            parry = 0
    print(f'#{t} {max(lst)}')