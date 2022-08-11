# https://www.acmicpc.net/problem/2979

A, B, C = map(int,input().split())
dict_ = {}

for _ in range(3):
    arrive, leave = map(int,input().split())
    for i in range(arrive, leave):
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1
print(dict_)

fee = 0
for k, v in dict_.items():
    if v == 1:
        fee += v * A
    elif v == 2:
        fee += v * B
    elif v == 3:
        fee += v * C
    
print(fee)