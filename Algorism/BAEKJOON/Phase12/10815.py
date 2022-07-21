import sys

N = int(input())
lst = list(map(int,sys.stdin.readline().split()))
M = int(input())
lst2 = list(map(int,sys.stdin.readline().split()))

for i in lst2:
    if i in lst:
        print(1,end=' ')
    else:
        print(0,end=' ')