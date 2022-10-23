for t in range(1, int(input())+1):

    matrix = [list(map(int,input().split())) for _ in range(9)]
    table = [[0]*9 for _ in range(9)]
    nine = [[0]*3 for _ in range(3)]
    ans1 = 0

    for i in range(9):
        for j in range(9):
            table[j][i] = matrix[i][j]

    for k in range(9):
        if sum(matrix[k]) != 45 or sum(table[k]) != 45:
            ans1 = 0
            break
    else:
        ans1 = 1
    
    total = 0
    bool_check = True
    for m in range(0, 9, 3):
        if bool_check == True:
            for n in range(0, 9, 3):
                for o in range(m, m+3):
                    for p in range(n, n+3):
                        total += matrix[o][p]
                if total != 45:
                    ans2 = 0
                    bool_check = False
                else:
                    total = 0
        else:
            ans2 = 0
            break
    else:
        ans2 = 1

    print(f'#{t} {ans1 and ans2}')

