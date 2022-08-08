import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    count = 0
    N, M = map(int,input().split())
    for i in range(N, M+1):
        count += str(i).count('0')

    print(count)