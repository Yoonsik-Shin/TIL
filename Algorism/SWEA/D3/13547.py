for t in range(1, int(input())+1):
    S = input()
    S_length = len(S)
    left_S = 15 - S_length

    if S.count('o') >= 8 or left_S + S.count('o') >= 8:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')
