import sys
input = sys.stdin.readline

K = int(input())
stack = []

for _ in range(K):
    number = int(input())
    
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))