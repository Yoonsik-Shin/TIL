# https://www.acmicpc.net/problem/2004

def f(p, k):
    ans = 0
    while p:
        p //= k
        ans += p
    return ans

n, m = map(int,input().split())

print(min(f(n, 2) - f(n-m, 2) - f(m, 2), f(n, 5) - f(n-m, 5) - f(m, 5)))