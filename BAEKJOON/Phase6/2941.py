x = input()

c = ['c=','c-','dz=','d-','lj','nj','s=','z=']
total = 0
for i in c:
    x = x.replace(i,'c')
print(len(x))