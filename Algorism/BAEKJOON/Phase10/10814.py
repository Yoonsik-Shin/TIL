import sys

N = int(input())
lst2 = []

for i in range(N):
    x, y = sys.stdin.readline().split()
    lst = []
    lst.append(int(x))
    lst.append(i)
    lst.append(y)
    lst2.append(lst)

lst2.sort(key = lambda x : [x[0], x[1]])

for j in lst2:
    print(f'{j[0]} {j[2]}')

# 왜 오류인지 모르겠다..
# 정렬전에 숫자가 문자열로 되어있어 정렬이 이상해짐