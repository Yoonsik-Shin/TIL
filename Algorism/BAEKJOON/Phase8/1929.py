# M, N = map(int,input().split())
# lst=[]

# for i in range(M,N+1):
#     e = 0
#     for j in range(2,i+1):
#         if i%j == 0:
#             e+=1
#     if e == 1:
#        print(i)
'''
구글링
'''

M, N = map(int,input().split())
a = [False, False] + [True]*(N-1)
lst = []

for i in range(2, N+1):
    if a[i]:
        lst.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

for k in lst:
    if k >= M:
        print(k)

'''
새로운 개념
에라토스테네스의 체
'''