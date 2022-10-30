dict_lst = {
    'MON': 6,
    'TUE': 5,
    'WED': 4,
    'THU': 3,
    'FRI': 2,
    'SAT': 1,
    'SUN': 7
}

for t in range(1,int(input())+1):
    S = input()

    print(f'#{t} {dict_lst[S]}')