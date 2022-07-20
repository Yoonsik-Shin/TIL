import sys

N = int(input())
lst2 = []

for i in range(N):
    lst = sys.stdin.readline().split()
    lst.insert(1,i)
    lst2.append(lst)

lst2.sort(key = lambda x : [x[0], x[1]])

for j in lst2:
    print(f'{j[0]} {j[2]}')

# 왜 오류인지 모르겠다..