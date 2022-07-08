x = input()
a, b = map(int,x.split(sep=' '))
if a>b:
    print('>')
elif a<b:
    print('<')
elif a==b:
    print('==')