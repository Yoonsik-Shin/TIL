T = int(input())

for i in range(T):
    x = input()
    if x[4:6] == '02' and int(x[6:]) > 28:
        print(f'#{i+1} -1')
    elif int(x[4:6]) > 12 or int(x[4:6]) < 1:
        print(f'#{i+1} -1')
    elif int(x[6:]) > 30:
        print(f'#{i+1} -1')
    else:
        print(f'#{i+1} {x[:4]}/{x[4:6]}/{x[6:]}')