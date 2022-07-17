d = []

for i in range(19):
    d.append(list(map(int,input().split()))) # 배열입력 만들기\

n = int(input())
for j in range(n):
    x, y = map(int,input().split())
    for k in range(19):
        if d[k][y-1] == 1:
            d[k][y-1] = 0
        else:
            d[k][y-1] = 1

        if d[x-1][k] == 1:
            d[x-1][k] = 0
        else:
            d[x-1][k] = 1

for m in d:
    p = list(map(str,m))
    q = ' '.join(p)
    print(q)