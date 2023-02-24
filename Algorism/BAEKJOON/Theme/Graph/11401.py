from math import factorial as f

n, k = map(int,input().split())

print((f(n)//(f(n-k) * f(k))) % 1000000007)