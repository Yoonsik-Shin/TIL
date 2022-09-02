from copy import deepcopy

n = int(input())
total = 0
total_lst = [0] * n
lst2 = [0] * n

for i in range(n):
    lst = list(map(int,input().split()))
    
    if len(lst) == 1:
        total_lst[0] = lst[-1]
        continue

    for j in range(i):
        a = total_lst[j]
        lst2[j] = max(lst2[j], a + lst[j])
        lst2[j+1] = max(lst2[j+1], a + lst[j+1])

    total_lst = deepcopy(lst2)

print(max(total_lst))