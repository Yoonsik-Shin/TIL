from collections import deque

n = int(input())
A = deque(map(int,input().split()))
ans = 0

for _ in range(n):
  total = 0
  for i in range(n-1):
    total += abs(A[i] - A[i+1])
    print(total)
  
  if total > ans:
    ans = total
  
  start = A.popleft()
  A.append(start)
  print(A)
  print(ans)