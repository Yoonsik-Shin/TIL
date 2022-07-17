T = int(input())
lst = []

for i in range(T):
    H, W, N = map(int,input().split())

    a = N//H
    b = N%H

    if a < 9:
        ans_1 = str(1+a)
        ans_10 = '0'
    else:
        ans_1 = str(1+a)
        ans_10 = ''
        
    if b == 0:
        ans_100 = str(H)
    else:    
        ans_100 = str(b)

    lst.append(int(ans_100+ans_10+ans_1))

for j in lst:
    print(j)