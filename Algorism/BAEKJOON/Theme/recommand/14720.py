from collections import deque

N = int(input())
x = list(map(int,input().split()))

queue = deque(x)
count = 0
ans = 0

for i in range(N):
    if queue.popleft() == count%3:
        count+=1
        ans += 1

print(ans)