import sys
from collections import Counter

N = int(input())
lst = []

for i in range(N):
    number = int(sys.stdin.readline().rstrip())
    lst.append(number)

ans = sorted(Counter(lst).items(), key=lambda x:(-x[1],x[0]))

print(ans[0][0])