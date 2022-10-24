for t in range(1, int(input())+1):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    word = input()
    count = 0

    for i in range(len(word)):
        if word[i] == alpha[i]:
            count += 1
        else:
            break
        
    print(f'#{t} {count}')