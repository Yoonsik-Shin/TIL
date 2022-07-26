
















# 모범답안
T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    lst = [i for i in range(1,n+1)]

for x in range(k):
    for y in range(1, n):
        lst[y] += lst[y-1]
    print(lst)
# print(lst[-1])