x = input()
cut = []
stack = []

for i in range(len(x)-1):
    if x[i] == '(':
        if x[i+1] == ')':
            cut.append(i)
        else: 
            stack.append(i)
    elif x[i] == ')':
        if x[stack[-1]] == '(':
            