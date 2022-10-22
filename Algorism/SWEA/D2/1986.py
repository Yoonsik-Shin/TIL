# T = int(input())


# for i in range(T):
#     N = int(input())
#     lst = []
#     for j in range(1,N+1):
#         if j%2 == 1:
#             lst.append(j)
#         elif j%2 == 0:
#             lst.append(j*(-1))

#     print(f'#{i+1} {sum(lst)}')

for t in range(1, int(input())+1):
    num = int(input())
    total = 0

    for i in range(1, num+1):
        if i%2 == 0:
            total -= i
        else:
            total += i
    
    print(f'#{t} {total}')