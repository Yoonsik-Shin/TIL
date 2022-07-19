h, w = map(int,input().split())
demension = []

for i in range(h):
    demension.append([])
    for j in range(w):
        demension[i].append(0)

n = int(input())

for k in range(n):
    l, d, x, y = map(int,input().split())
    if d == 0:
        for m in range(l):
            demension[x-1][y-1+m] = 1
    elif d == 1: 
        for o in range(l):
            demension[x-1+o][y-1] = 1

for p in demension:
    ans = ' '.join(map(str,p))
    print(ans)