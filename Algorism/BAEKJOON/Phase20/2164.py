from collections import deque

queue = deque()
N = int(input())

for i in range(1, N+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    back = queue.popleft()
    queue.append(back)

print(queue[0])