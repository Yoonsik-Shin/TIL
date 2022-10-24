# C++만 가능
for t in range(1, int(input())+1):

    N = int(input())

    lst = list(map(int,input().split()))
    lst2 = []

    for i in range(N):
        lst2.append(abs(lst[i]))
    
    ans = sorted(lst2, reverse=True)[-1]

    print(f'#{t} {ans} {lst2.count(ans)}')