for t in range(1, int(input())+1):
    S = input()

    answer = S.count('(|') + S.count('|)') + S.count('()')

    print(f'#{t} {answer}')