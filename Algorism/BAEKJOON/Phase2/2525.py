# My
A, B = map(int,input().split(sep=' '))
T = int(input())
T_a = T//60
T_b = T%60

if T_b+B >= 60:
    A = A+T_a+1
    B = (T_b+B)-60
    if A >= 24:
        A = A-24
        print(A, B)
    else:
        print(A, B)
elif T_b+B < 60:
    A = A+T_a
    B = T_b+B
    if A >= 24:
        A = A-24
        print(A, B)
    else:
        print(A, B)

# 좋은 풀이법
h,m=map(int,input().split())
cookT=int(input())
total=h*60+m+cookT
if total>=1440:
    total-=1440
    print(total//60, total%60)
else:
    print(total//60, total%60)
