# https://www.acmicpc.net/problem/2628

x, y  = map(int,input().split())
cut = int(input())

lst_x = [0, x]
lst_y = [0, y]

for i in range(cut):
    direction, cut_line = map(int,input().split())
    if direction == 1:
        lst_x.append(cut_line)
    else:
        lst_y.append(cut_line)

lst_x.sort()
lst_y.sort()

ans_x_lst = []
ans_y_lst = []

for j in range(len(lst_x)-1):
    ans_x_lst.append(lst_x[j+1] - lst_x[j])

for k in range(len(lst_y)-1):
    ans_y_lst.append(lst_y[k+1] - lst_y[k])

ans = 0
for m in ans_x_lst:
    for n in ans_y_lst:
        if ans < m*n:
            ans = m*n

print(ans)