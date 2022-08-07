while True:
    x = input()
    
    if x == '.':
        break

    stack = []
    ans = ''

    for j in x:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ']':
            if len(stack) == 0:
                ans = 'no'
                break
            if stack[-1] == '[':
                stack.pop()
            elif stack[-1] == '(':
                ans = 'no'
                break
        elif j == ')':
            if len(stack) == 0:
                ans = 'no'
                break
            if stack[-1] == '(':
                stack.pop()
            elif stack[-1] == '[':
                ans = 'no'
                break
    
    if len(stack) == 0 and ans == 'no':
        print(ans)
    elif len(stack) == 0:
        print('yes')
    else:    
        print('no')