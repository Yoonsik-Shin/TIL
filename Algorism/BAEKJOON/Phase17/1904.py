import sys
input = sys.stdin.readline

N = int(input())
lst = [0, 1, 2]

for i in range(3, N+1):
    lst.append((lst[i-2]+lst[i-1])%15746)

if N == 1:
    print(1)
else:
    print(lst[-1])