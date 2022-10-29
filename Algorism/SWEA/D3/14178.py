for t in range(1, int(input())+1):
    N, D = map(int,input().split())
    width = 2*D
    count = 0

    i = 1
    while True:
        if i > N:
            break
        else:
            i += width+1
            count += 1

    print(f'#{t} {count}')