def solution(arr):
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[i])
            continue

        if stack[-1] == arr[i]:
            continue
        else:
            stack.append(arr[i])
    return stack