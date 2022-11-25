from collections import Counter

a_x, a_y = list(map(int,input().split()))
b_x, b_y = list(map(int,input().split()))
c_x, c_y = list(map(int,input().split()))

x_lst = [a_x, b_x, c_x]
y_lst = [a_y, b_y, c_y]

print(sorted(Counter(x_lst).items(),key=lambda x:x[1])[0][0], sorted(Counter(y_lst).items(),key=lambda x:x[1])[0][0])