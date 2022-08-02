import sys

T = int(sys.stdin.readline())

for _ in range(T):
    dict_ = {}

    N = int(sys.stdin.readline())
    lst_1 = list(map(int,sys.stdin.readline().split()))

    for i in range(N):
        dict_[lst_1[i]] = 0

    M = int(sys.stdin.readline())
    lst_2 = list(map(int,sys.stdin.readline().split()))

    for j in range(M):
        if lst_2[j] in dict_:
            print(1)
        else:
            print(0)