for t in range(1, int(input())+1):
    N, K = map(int, input().split())
    total_lst = []
    num = N//10
    a = ['A']*num + ['A0']*num + ['A-']*num + ['B+']*num + ['B0']*num + ['B-']*num + ['C+']*num + ['C0']*num + ['C-']*num + ['D0']*num

    for i in range(N):
        lst = list(map(int,input().split()))
        total = lst[0]*0.35 + lst[1]*0.45 + lst[-1]*0.2
        total_lst.append(total)
    sorted_total_lst = sorted(total_lst, reverse=True)
    
    print(f'#{t} {a[sorted_total_lst.index(total_lst[K-1])]}')