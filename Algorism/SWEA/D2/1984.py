for t in range(1, int(input())+1):
    lst = list(map(int,input().split()))
    lst.sort()
    lst.pop()
    print(f'#{t} {round(sum(lst[1:])/8)}')