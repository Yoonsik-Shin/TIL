N = int(input())
A = map(int,input().split())
M = int(input())
check = map(int,input().split())
dict_ = {}

for i in A:
    if i not in dict_:
        dict_[i] = 0

for j in check:
    if j in dict_:
        dict_[j] = 1
        print(dict_[j])
    else:
        print(0)