import sys

N = int(input())
lst = []

for i in range(N):
    x = sys.stdin.readline().rstrip('\n')
    if [len(x), x] not in lst:
        lst.append([len(x), x])

lst.sort()

for j in lst:
    print(j[1])