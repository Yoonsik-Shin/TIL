H, M = map(int,input().split(sep=' '))
if M-45 < 0:
    H = H-1
    if H < 0:
        H = 23
        M = 60-abs(M-45)
        print(H, M)
    else:
        print(str(H)+' '+str(60-abs(M-45)))
elif M-45>=0:
    M = M-45
    print(H, M)

