S = input()
stack = []
count = {
    '0': 0,
    '1': 0,
}

for i in S:
    if len(stack) == 0:
        stack.append(i)
    if stack[-1] != i:
        stack = [i]
        count[i] += 1

print(max(count.values()))
