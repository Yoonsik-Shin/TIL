h, w = map(int,input().split())
ans = [[-1] * w for _ in range(h)]

for i in range(h):
  check = list(input())

  if 'c' in check:
    num = 0
    for j in range(w):
      if num != 0 and check[j] != 'c':
        ans[i][j] = num
        num += 1
        continue

      if check[j] == 'c':
        num = 0
        ans[i][j] = num
        num += 1
  
for p in range(h):
  for q in range(w):
    print(ans[p][q], end=' ')
  print()