import sys
from copy import deepcopy
S = sys.stdin.readline().rstrip()
lst = []
dict_lst = {}
q = int(sys.stdin.readline())

for i in range(1, len(S)):
    for j in S[0:i]:
        if j not in dict_lst:
            dict_lst[j] = 1
        else:
            dict_lst[j] += 1
    lst.append(dict_lst)
    dict_lst = {}

for _ in range(q):
    deep_copy_lst = deepcopy(lst)
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    try:
        if l == 0:
            print(deep_copy_lst[r])
            print(deep_copy_lst[r][a])
        else:
            for k in deep_copy_lst[l-1]:
                deep_copy_lst[r][k] -= deep_copy_lst[l][k]
            print(deep_copy_lst[r])
            print(deep_copy_lst[r][a])
    except:
        print(0)
