import sys
input = sys.stdin.readline

N = int(input())
lst = [1, 2]

for i in range(2, N):
    lst.append((lst[i-2]+lst[i-1])%15746)

if N == 1:
    print(1)
else:
    print(lst[-1])