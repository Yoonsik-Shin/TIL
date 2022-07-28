from pprint import pprint

N, M = map(int,input().split())


lst2 = []

for i in range(N):
    x = input()
    lst = []
    for j in x:
        lst.append(j)
    lst2.append(lst)

pprint(lst2)

# for i in range(N):
#     for j in range(M):
#         if lst2[i][j] == 'B':   
