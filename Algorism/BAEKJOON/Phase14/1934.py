T = int(input())

for i in range(T):
    A, B = map(int,input().split())
    for j in range(1, B+1):
        if A % j == 0 and B % j ==0:
            