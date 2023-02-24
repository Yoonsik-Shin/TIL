import heapq
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  m = int(input())
  if m <= 10:
    arr = list(map(int,input().split()))
    heap = arr
  else:
    arr = []
    for _ in range(m//10 + 1):
      a = list(map(int,input().split()))
      for b in a:
        arr.append(b)
    heap = arr
  med = 0
  heapq.heapify(heap)
  print(heap)
  print(arr)

  for i in range(m):
    if i % 2 == 0:
      for _ in range(i):
        med = heapq.heappop(heap)
      print(med, end=' ')