import sys
input = sys.stdin.readline

S = input()
q = int(input())
dict_ = {}

for _ in range(q):
    alpha, l, r = input().split()
    l = int(l)
    r = int(r)

    for i in range(l, r+1):
        if S[i] not in dict_:
            dict_[S[i]] = 1
        else:
            dict_[S[i]] += 1
        
    if dict_.get(alpha) == None:
        print(0)
    else:
        print(dict_.get(alpha))
    dict_ = {}