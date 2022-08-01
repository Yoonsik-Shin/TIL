# https://www.acmicpc.net/problem/10773 

import sys

K = int(sys.stdin.readline())
stack = []

for i in range(K):
    stack.append(int(sys.stdin.readline()))
    if stack[-1] == 0:
        stack.pop()
        stack.pop()

print(sum(stack))