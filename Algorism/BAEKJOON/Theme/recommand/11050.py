# https://www.acmicpc.net/problem/11050
from math import factorial

N, K = map(int,input().split())

ans =  factorial(N) // (factorial(K) * factorial(N-K))

print(ans)


# 함수식

def facto(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n, k = map(int, input().split())
print(facto(n) // facto(k) // facto(n-k))