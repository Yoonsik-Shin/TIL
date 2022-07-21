T = int(input())

for i in range(T):
    P, Q, R, S, W = map(int,input().split())
    A = P*W 
    if R >= W:
        B = Q
    elif R < W:
        B = Q + S*(W-R)

    if A > B:
        print(f'#{i+1} {B}')
    else:
        print(f'#{i+1} {A}')