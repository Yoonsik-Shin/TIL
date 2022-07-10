T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    C = len(S)
    pnt = ''
    for j in range(C):
        pnt += S[j]*R
    print(pnt)