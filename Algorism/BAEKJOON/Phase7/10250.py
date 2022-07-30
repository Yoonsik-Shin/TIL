T = int(input())

for i in range(T):
    H, W, N = map(int,input().split())
    Y = N%H
    X = N//H + 1

    if Y == 0:
        print(100*H+X-1)
    else:
        print(100*Y+X)