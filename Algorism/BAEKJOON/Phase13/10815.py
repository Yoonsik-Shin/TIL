import sys

N = int(input())
lst = list(map(int,sys.stdin.readline().split()))
M = int(input())
lst2 = list(map(int,sys.stdin.readline().split()))

dict_ = {}

for i in lst2:
    dict_[i] = 0

for j in lst:
    if dict_.get(j) == None:
        continue
    else:
        dict_[j]+=1

for k in dict_.items():
    print(k[1], end=' ')
