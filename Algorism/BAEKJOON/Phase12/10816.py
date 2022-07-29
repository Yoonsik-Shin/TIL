N = int(input())
s_card = list(map(int,input().split()))
M = int(input())
check_card = list(map(int,input().split()))

check_dict = {}
for i in check_card:
    check_dict[i] = 0

for j in s_card:
    if check_dict.get(j) == None:
        continue
    else:
        check_dict[j] += 1

for k in check_card:
    print(check_dict.get(k), end=' ')