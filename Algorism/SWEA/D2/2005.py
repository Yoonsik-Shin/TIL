T = int(input())

for _ in range(1, T+1):
    
    lst = [1, 1]
    
    N = int(input())
    print(f'#{_}')
    print(1)
    if N != 1:
        print(1, 1)

    for i in range(2, N):
        lst2 = [1]
        print(1, end=' ')
        for j in range(i-1):
            print(lst[j]+lst[j+1], end=' ')
            lst2.append(lst[j]+lst[j+1])
        print(1, end=' ')
        lst2.append(1)
        lst = lst2
        print()
