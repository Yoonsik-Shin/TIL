stack = []

stack.append(1) # 삽입
stack.append(2)
stack.append(3)
stack.pop() 	# 삭제
stack.append(8)
stack.pop()

print(stack)
print(stack[::-1])
