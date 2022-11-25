import sys

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dict_ = {}

a = set(lst)
sorted_lst = sorted(list(a))

for i in range(len(sorted_lst)): ## 생각해내지 못한 부분
    dict_[sorted_lst[i]] = i     ## 생각해내지 못한 부분

for j in lst:
    print(dict_.get(j), end=' ')