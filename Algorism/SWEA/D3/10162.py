time_list = [300, 60, 10]
ans = []

T = int(input())

for i in time_list:
    ans.append(T//i)
    T%=i

if T:
    print(-1)
else:
    for j in ans:
        print(j, end=' ')