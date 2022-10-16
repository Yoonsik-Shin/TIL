import sys

N = int(sys.stdin.readline())
total = 0

for i in range(N):
    word = sys.stdin.readline().rstrip()

    while True:
        stack = []
        for j in range(len(word)):
            if len(stack) == 0:  
                stack.append(word[j])
                continue
            if word[j] == stack[-1]:
                stack.pop()
            else:
                stack.append(word[j])

        if len(stack) == 0:
            total += 1
            break
        elif len(stack) == len(word) or len(stack)%2 != 0:
            break

print(total)