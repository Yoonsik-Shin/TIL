for t in range(1, int(input())+1):
    lst = [31, 28, 31, 30,31, 30 ,31, 31, 30, 31, 30, 31]

    date_lst = list(map(int,input().split()))

    date_total = 0
    for i in range(date_lst[0]-1):
        date_total += lst[i]
    date_total += date_lst[1]

    after_date_total = 0
    for j in range(date_lst[2]-1):
        after_date_total += lst[j]
    after_date_total += date_lst[3]

    print(f'#{t} {after_date_total-date_total+1}')