def solution(s):
    stack = []
    
    for i in s:
        if not len(stack):
            stack.append(i)
        else:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == ')':
                break
            else:
                stack.append(i)
    
    if len(stack):
        return False
    else:
        return True