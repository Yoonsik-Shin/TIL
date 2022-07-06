x = input()
lists = list(map(int,x.split(sep=' ')))
A, B, C = lists
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)