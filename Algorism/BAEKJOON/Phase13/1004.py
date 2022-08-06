from re import A


T = int(input())

for i in range(T):
    x_1, y_1, x_2, y_2 = map(int,input().split())
    n = int(input())
    count = 0

    for j in range(n):
        c_x, c_y, r = map(int,input().split())
        a = (x_1-c_x)**2 + (y_1-c_y)**2 < r**2
        b = (x_2-c_x)**2 + (y_2-c_y)**2 < r**2
        if a and b:
            continue
        elif a or b:
            count += 1
    
    print(count)