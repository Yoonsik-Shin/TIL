# https://www.acmicpc.net/problem/1010
 
from math import factorial

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    ans = factorial(M) // (factorial(N) * factorial(M-N))
    print(ans)

# 단순한 조합문제