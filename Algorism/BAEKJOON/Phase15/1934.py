import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = map(int,input().split())
    C = max(A, B)
    for j in range(C, 0, -1):
        if A % j == 0 and B % j == 0:
            print(A//j * B//j * j)
            break
    else:
        print(A*B)