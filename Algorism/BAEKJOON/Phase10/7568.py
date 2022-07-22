N = int(input())
lst = []

for i in range(N):
    x, y = map(int,input().split())
    lst.append([x,y])

for j in range(N-1):
    for k in range(j+1,N):
        if lst[j][0] > lst[k][0] and lst[j][0] > lst[k][0]
