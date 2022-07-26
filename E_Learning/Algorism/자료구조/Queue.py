from collections import deque # 시간복잡도 때문에 활용

queue = deque()

queue.append(1) # 삽입
queue.append(2)
queue.append(3)
queue.popleft() # 삭제

print(queue)
queue.reverse()
print(queue)