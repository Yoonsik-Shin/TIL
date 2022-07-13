N = int(input())
lst = []
y = N//5

for i in range(y+1):
    if (N-(5*i))%3 == 0:
        x = (N-(5*i))/3
        y = i
        lst.append(int(x+y))

if len(lst) == 0:
    print('-1')
else:
    print(min(lst))