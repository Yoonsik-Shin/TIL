for t in range(1, int(input())+1):
    N = int(input())
    word = ''

    for i in range(N):
        alpha, num = input().split()
        word = word + alpha*int(num)

    print(f'#{t}')
    for m in range(len(word)//10):
        for n in range(10*m, 10*(m+1)):
            print(word[n], end='')
        print()
    for k in range(len(word)%10):
        print(word[-1-k],end='')
    print()