# 이러닝 강의 정리



## 스택 구현

```python
stack = []

stack.append(1) # 삽입
stack.append(2)
stack.append(3)
stack.pop() 	# 삭제
stack.append(8)
stack.pop()

print(stack)
>> [1, 2]
print(stack[::-1])
>> [2. 1]
```



## 큐 구현

```python
from collections import deque # 시간복잡도 때문에 활용

queue = deque()

queue.append(1) # 삽입
queue.append(2)
queue.append(3)
queue.popleft() # 삭제

print(queue)
>> deque([2, 3])

queue.reverse()
print(queue)
>> deque([3, 2])
```



## 우선순위 큐 (Priority Queue) 

