import sys

N = int(input())
count = [0] * 10000

for i in range(N):
    x = int(sys.stdin.readline())
    count[x-1] += 1

for i in range(10000):
    if count[i] != 0:
          for j in range(count[i]):
            print(i+1)