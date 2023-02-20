from itertools import product

n, m = map(int,input().split())
lst = list(range(1, n+1))

for i in list(product(*list(lst for _ in range(m)))):
  for j in i:
    print(j, end=' ')
  print()