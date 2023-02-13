n, m = map(int,input().split())
j = int(input())
ans = 0
s, e = 1, m

for _ in range(j):
    d = int(input())

    if s <= d <= e:
      continue

    if d > s and d > e:
      ans += (d - e)
      s = d - m + 1
      e = d 
      continue
    
    if d < s and d < e:
      ans += (s - d)
      s = d
      e = d + m - 1
      continue
    
print(ans)