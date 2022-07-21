T = int(input())

for i in range(T):
    lst = map(int,input().split())
    ans = []
    for j in lst:
        if j%2 == 1:
            ans.append(j)
    print(f'#{i+1} {sum(ans)}')