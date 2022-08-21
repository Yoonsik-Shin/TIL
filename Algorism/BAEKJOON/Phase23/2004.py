# https://www.acmicpc.net/problem/2004
# 못품

from math import comb
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

k = comb(n, m)
str_k = str(k)

count = 0
for i in range(len(str_k)-1, 0, -1):
    if str_k[i] == '0':
        count += 1
    else:
        break

print(count)

