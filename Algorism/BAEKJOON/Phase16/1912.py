# 못품

n = int(input())

lst = list(map(int,input().split()))
check_lst = [lst[0]]
ans_max = -1e9

for i in range(1,n):
    
    if len(check_lst) == 0:
        check_lst.append(lst[i])
        continue

    check_lst.append(check_lst[-1]+lst[i])
    
    if check_lst[-1] < check_lst[-2]:
        if check_lst[-2] > ans_max:
            ans_max = check_lst[-2]
        check_lst = []

print(ans_max)