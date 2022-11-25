T = int(input())

for i in range(T):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int,input().split())

    # 1 일치
    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        print(-1)
    elif x_1 == x_2 and y_1 == y_2 and r_1 != r_2:
        print(0)
    # 2 외접      
    elif ((x_1-x_2)**2 + (y_1-y_2)**2) == (r_1 + r_2)**2:
        print(1)
    # 3 내접
    elif ((x_1-x_2)**2 + (y_1-y_2)**2) == (r_1-r_2)**2:
        print(1)
    # 4 서로 떨어짐    
    elif ((x_1-x_2)**2 + (y_1-y_2)**2) > (r_1+r_2)**2:
        print(0)
    # 5 원 내부에서 안만남
    elif ((x_1-x_2)**2 + (y_1-y_2)**2) < (r_1-r_2)**2:
        print(0)
    # 6
    else:
        print(2)

    