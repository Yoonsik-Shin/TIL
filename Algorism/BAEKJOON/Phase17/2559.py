N, K = map(int,input().split())

lst = list(map(int,input().split()))
psum = [lst[0]]
ans = []

for i in range(1, N):
    psum.append(psum[i-1] + lst[i])

ans.append(psum[K-1])

for j in range(K, N):
    ans.append(psum[j] - psum[j-K])

print(max(ans))