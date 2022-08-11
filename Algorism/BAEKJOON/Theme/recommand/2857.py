# https://www.acmicpc.net/problem/2857

lst = []

for _ in range(1, 6):
    x = input()
    if x.find('FBI') >= 0:
        lst.append(_)

if len(lst) == 0:
    print('HE GOT AWAY!')
else:
    for i in lst:
        print(i, end = ' ')