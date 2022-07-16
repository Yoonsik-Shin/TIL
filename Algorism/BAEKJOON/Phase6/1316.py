N = int(input())
count = 0

for i in range(N):
    x = input()
    lst = []
    lst2 = []
    for i in x:
        if i not in lst:
            lst.append(i)
    for j in range(len(lst)-1):
        if len(lst) == 1:
            continue
        elif lst[j] == lst[j+1]:
            continue
        elif lst[j] != lst[j+1]:
            if lst[j+1] in lst and len(lst) != len(x):
                count-=1
                break
            else:
                continue
    count+=1
    
print(count)


