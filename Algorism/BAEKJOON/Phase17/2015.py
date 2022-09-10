# 시간초과
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

A = list(map(int,input().split()))
psum = []
count = 0

for i in range(N-1):
    for j in range(i, N):
        if i == j:
            psum.append(A[j])
            if psum[-1] == K:
                count += 1 
        else:
            psum.append(psum[-1]+A[j])
            if psum[-1] == K:
                count += 1
    psum = []

print(count)

# 메모리 초과
N, K = map(int,input().split())

A = list(map(int,input().split()))
psum = []

for i in range(N-1):
    for j in range(i, N):
        if i == j:
            psum.append(A[j])
        else:
            psum.append(psum[-1]+A[j])

print(psum.count(K))

# 정답 
N, K = map(int,input().split())
a = list(map(int,input().split()))

psum = [0] * N
psum[0] = a[0]
for i in range(1, N):
    psum[i] = psum[i-1] + a[i]
    
count = {}
ans = 0
for i in range(N):
    goal = psum[i] - K
    
    if goal in count:
        ans += count[goal]
    if goal == 0:
        ans += 1
        
    if psum[i] not in count:
        count[psum[i]] = 0
    count[psum[i]] += 1

print(ans)