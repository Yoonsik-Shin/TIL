N, K = map(int,input().split())

tempList = list(map(int,input().split()))
totalSum = []
lst = []

for i in range(N):
  if i == 0:
    totalSum.append(tempList[i])
  else:
    totalSum.append(totalSum[i-1] + tempList[i])

for j in range(N):
  if j < K-1:
    continue
  if j == K-1:
    lst.append(totalSum[j])
  elif j >= K:
    lst.append(totalSum[j]-totalSum[j-K])

print(max(lst))