from copy import deepcopy
N = int(input())
lst = []
lst2 = []

for _ in range(N):
    dice = list(map(int,input().split()))
    lst.append(dice)

for i in range(6):
    total = 0
    lst1 = deepcopy(lst)
    idx = i
    value = lst1[0][i]
    for j in lst1:
        idx = j.index(value)
        if idx == 0:
            j[0] = 0
            value = j[5]
            j[5] = 0
        elif idx > 0 and idx <= 2:
            j[idx] = 0
            value = j[idx+2]
            j[idx+2] = 0
        elif idx > 2 and idx <= 4:
            j[idx] = 0
            value = j[idx-2]
            j[idx-2] = 0
        else:
            j[5] = 0
            value = j[0]
            j[0] = 0
        total += max(j)
    lst2.append(total)
print(max(lst2))