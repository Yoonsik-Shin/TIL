N = int(input())

r_lst = list(map(int,input().split()))

first = r_lst[0]

for i in r_lst[1:]:
    check = min(i, first)
    for j in range(check, 0, -1):
        if first % j == 0 and i % j == 0:
            print(f'{first//j}/{i//j}') 
            break