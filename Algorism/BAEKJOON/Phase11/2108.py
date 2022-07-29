from statistics import median
import sys
from collections import Counter

N = int(input())
lst = []

for i in range(N):
    x = int(sys.stdin.readline())
    lst.append(x)

print(round(sum(lst)/N))
print(median(lst))
a = sorted(Counter(lst).items(),key=lambda x:(-x[1],x[0]))
if N == 1:
    print(a[0][0])
elif a[0][1] == a[1][1]:
    print(a[1][0])
else:
    print(a[0][0])
print(abs(max(lst)-min(lst)))