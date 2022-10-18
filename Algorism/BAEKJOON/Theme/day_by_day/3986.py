import sys

N = int(sys.stdin.readline())
total = 0

for i in range(N):
    word = sys.stdin.readline().rstrip()
    stack = []
    for i in word:
        if len(stack) == 0:  
            stack.append(i)
        else: 
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        total += 1

print(total)