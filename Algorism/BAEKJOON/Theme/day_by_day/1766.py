import sys
import heapq
input = sys.stdin.readline

N, M = map(int,input().split())
heap = []

for i in range(M):
    (A, B) = map(int,input().split())
    heap.append((A, B))

for j in range(M):
    print(heapq.heappop(heap))
