import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())

    if x:
        heapq.heappush(heap, (abs(x),x))
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])