from collections import deque

N, M = map(int,input().split())
pick_lst = map(int,input().split())
queue = deque([_ for _ in range(1,N+1)])
count = 0

for i in pick_lst:

    if len(queue)%2 == 0:
        check = len(queue)//2
    elif len(queue)%2 != 0:
        check = len(queue)//2 + 1

    idx = queue.index(i) + 1

    if idx <= check:
        while True:
            a = queue.popleft()
            if a == i:
                break
            queue.append(a)
            count += 1
    elif idx > check:
        while True:
            b = queue.pop()
            if b == i:
                count += 1
                break
            else:
                queue.appendleft(b)
                count += 1

print(count)