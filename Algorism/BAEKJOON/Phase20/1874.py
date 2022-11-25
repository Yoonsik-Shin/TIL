import sys
input = sys.stdin.readline

n = int(input())
stack = []
i = 1
lst = []
a = True

for _ in range(n):
    x = int(input())
    while True:
        if len(stack) == 0:
            stack.append(i)
            i += 1
            lst.append('+')
        if stack[-1] == x:
            stack.pop()
            lst.append('-')
            break
        if stack[-1] > x:
            a = False
            break
        else:
            stack.append(i)
            lst.append('+')
            i += 1

if a == False:
    print('NO')
else:
    for j in lst:
        print(j)