T = int(input())

for _ in range(T):
    set_ = sorted(set(map(int,input().split())))
    print(set_[-3])