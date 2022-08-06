from collections import Counter

K = int(input())
lst = []
lst2 = []
rl = []
ud = []

for _ in range(6):
    direction, length = map(int,input().split())
    lst.append(direction)
    lst2.append(length)
    if direction == 1 or direction == 2:
        rl.append(length)
    else:
        ud.append(length)

big = max(rl) * max(ud)

for i in range(5):
    if lst[i] == 1 and lst[i+1] == 3: 
        small = lst2[i] * lst2[i+1]
    elif lst[-1] == 1 and lst[0] == 3:
        small = lst2[-1] * lst2[0]

    elif lst[i] == 3 and lst[i+1] == 2:
        small = lst2[i] * lst2[i+1]
    elif lst[-1] == 3 and lst[0] == 2:
        small = lst2[-1] * lst2[0]

    elif lst[i] == 2 and lst[i+1] == 4:
        small = lst2[i] * lst2[i+1]
    elif lst[-1] == 2 and lst[0] == 4:
        small = lst2[-1] * lst2[0]

    elif lst[i] == 4 and lst[i+1] == 1:        
        small = lst2[i] * lst2[i+1]
    elif lst[-1] == 4 and lst[0] == 1:
        small = lst2[-1] * lst2[0]

ans = (big - small) * K
print(ans)