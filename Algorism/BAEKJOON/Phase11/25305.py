N, k = map(int,input().split())
x = list(map(int,input().split()))

x.sort()

for _ in range(k):
    ans = x.pop()

print(ans)