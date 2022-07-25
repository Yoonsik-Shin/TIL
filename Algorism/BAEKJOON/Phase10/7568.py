N = int(input())
lst = []

for i in range(N):
    x, y = map(int,input().split())
    lst.append([x,y])

for j in range(len(lst)-1):
    ans = len(lst)
    for k in range(j+1, len(lst)):
        if lst[j][0] > lst[k][0] and lst[j][1] > lst[k][1]:
            ans -= -1
    print(ans, end=' ')

