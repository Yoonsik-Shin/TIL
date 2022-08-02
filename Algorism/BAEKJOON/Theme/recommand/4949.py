while True:
    char = input()

    if char == '.':
        break
    
    stack = []

    for i in char:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if '(' in stack:
                stack.pop()
            else:
                print('no')
                break
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if '[' in stack:
                stack.pop()
            else:
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')