T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())

    lst = []
    for j in range(1, n+1):
        lst.append(j)

    for _ in range(k):
        a = 0
        lst2 = []
        for m in range(n):
            a += lst[m]
            lst2.append(a)
        lst = lst2

    print(lst[-1])


# # 모범답안
# T = int(input())

# for i in range(T):
#     k = int(input())
#     n = int(input())

#     lst = [i for i in range(1,n+1)]

# for x in range(k):
#     for y in range(1, n):
#         lst[y] += lst[y-1]
#  print(lst[-1])