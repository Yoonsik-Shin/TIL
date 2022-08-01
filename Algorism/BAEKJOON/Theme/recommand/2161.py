from collections import deque

N = int(input())
lst = []

for i in range(1, N+1):
    lst.append(i)

queue = deque(lst)
lst2 = []

while len(queue) != 1:
    a = queue.popleft()
    lst2.append(a)
    b = queue.popleft()
    queue.append(b)

lst2.append(queue[0])

for j in lst2:
    print(j, end=' ')