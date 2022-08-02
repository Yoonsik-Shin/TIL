import sys
input = sys.stdin.readline

N = int(input())
log = {}
count = 0
for i in range(N):
    x = input().rstrip()
    if x == 'ENTER':
        log = {}
        continue
    if x not in log:
        log[x] = True
        count += 1