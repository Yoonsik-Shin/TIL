start, end = map(int,input().split())

if start % 4 == 0:
    x_s = start // 4 - 1
    y_s = 3
else:   
    x_s = start // 4
    y_s = start % 4 - 1

if end % 4 == 0:
    x_e = end // 4 - 1
    y_e = 3
else:   
    x_e = end // 4
    y_e = end % 4 - 1

print(abs(x_e - x_s) + abs(y_e - y_s))