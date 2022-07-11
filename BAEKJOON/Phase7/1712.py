A, B, C = map(int,input().split())
try:
    k = int(A/(C-B))
except:
    k = -1

if k<0:
    print(-1)
else:
    print(k+1)