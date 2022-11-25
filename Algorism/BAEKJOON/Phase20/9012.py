T = int(input())


for _ in range(T):
    
    stack = []
    x = input()
    
    for i in x:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print('NO')
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                continue
    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')