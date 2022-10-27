for t in range(1, int(input())+1):
    N, M = map(int,input().split())
    matrix = []
    for _ in range(N):
        S = input()
        S_lst = []
        for k in range(M):
            S_lst.append(S[k])
        matrix.append(S_lst)
    answer = 'possible'
    row = [0, 1, 0, -1]
    col = [1, 0, -1, 0]

    for i in range(N):
        if answer == 'possible':
            for j in range(M):
                if matrix[i][j] == '#':
                    for k in range(4):
                        adj_row = i + row[k]
                        adj_col = j + col[k]

                        if adj_row >= 0 and adj_row < N and adj_col >= 0 and adj_col < M:
                            if matrix[adj_row][adj_col] == '.':
                                continue
                            elif matrix[adj_row][adj_col] == '?':
                                matrix[adj_row][adj_col] = '.'
                            else:
                                answer = 'impossible'
                                break
                elif matrix[i][j] == '.':
                    for k in range(4):
                        adj_row = i + row[k]
                        adj_col = j + col[k]

                        if adj_row >= 0 and adj_row < N and adj_col >= 0 and adj_col < M:
                            if matrix[adj_row][adj_col] == '#':
                                continue
                            elif matrix[adj_row][adj_col] == '?':
                                matrix[adj_row][adj_col] = '#'
                            else:
                                answer = 'impossible'
                                break
        else:
            break

    print(f'#{t} {answer}')