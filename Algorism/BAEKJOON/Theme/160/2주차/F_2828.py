N, M = map(int,input().split())
J = int(input())
m = 0
l = 1

for i in range(J):
  d = int(input())
  s = 0

  while True:
    if d >= s and d < M + s:

      break
    elif d < s:
      s -= 1
      l -= 1
    else:
      s += 1
      l += 1

  m += s

print(m)