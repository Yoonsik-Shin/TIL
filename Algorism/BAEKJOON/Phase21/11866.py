from collections import deque

N, K = map(int,input().split())
queue = deque()
lst = []

for i in range(1, N+1):
    queue.append(i)

while True:

    for _ in range(K-1):
        queue.append(queue.popleft())

    lst.append(queue.popleft())

    if len(queue) == 1:
        lst.append(queue[0])
        break
    elif len(queue) == 0:
        break

print('<',end='')
for j in range(N-1):
    print(lst[j], end=', ')
print(lst[-1], end ='')
print('>',end='')