S = input()
word = []
stack = []
lst = []

i = 0 

while i != len(S):
    if S[i] == '<':
        word.append(S[i])
        stack = stack[::-1]
        lst.append(''.join(stack))
        stack.clear()
        while True:
            i += 1

            if S[i] == '>':
                word.append(S[i])
                lst.append(''.join(word))
                word.clear()
                i += 1
                break
            word.append(S[i])
    else:
        if S[i] == ' ':
            stack = stack[::-1]
            lst.append(''.join(stack))
            lst.append(' ')
            stack.clear()
            i += 1
        else:
            stack.append(S[i])
            i += 1
if len(stack) == 0:
    print(''.join(lst))
else:       
    stack = stack[::-1]
    lst.append(''.join(stack))
    print(''.join(lst))
