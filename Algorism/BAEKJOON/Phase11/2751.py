import sys

N = int(input())
lst = []

for i in range(N):
    x = int(sys.stdin.readline())
    lst.append(x)

lst.sort(reverse=False)    

for j in lst:
    print(j)