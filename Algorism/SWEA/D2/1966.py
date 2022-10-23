for t in range(1, int(input())+1):
    N = int(input())
    lst = list(map(int,input().split()))
    lst.sort()

    print(f'#{t}', end=' ')
    for i in lst:
        print(i, end=' ')
    print()