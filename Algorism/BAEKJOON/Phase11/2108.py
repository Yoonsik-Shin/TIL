from statistics import mode, median
import sys

N = int(input())
lst = []

for i in range(N):
    x = int(sys.stdin.readline())
    lst.append(x)

print(round(sum(lst)/N))
print(median(lst))
print(mode(lst))
print(abs(max(lst)-min(lst)))

