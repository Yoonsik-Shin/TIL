t = int(input())

for _ in range(t):
  n = int(input())
  dp = [1, 1, 1]

  for i in range(3, n):
    dp.append(dp[i-3] + dp[i-2])

  print(dp[-1])