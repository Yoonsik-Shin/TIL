from collections import Counter

T = int(input())

for i in range(T):
    N = int(input())
    lst = map(int,input().split())
    lst2 = []

    for j in lst:
        lst2.append(abs(0-j))

    ans = Counter(lst2).items()
    ans = sorted(ans, key=lambda x:x[0])
    print(f'#{i+1} {ans[0][0]} {ans[0][1]}')