T = int(input())

for i in range(T):
    H, W, N = map(int,input().split())
    Y = N%H
    X = N//H

