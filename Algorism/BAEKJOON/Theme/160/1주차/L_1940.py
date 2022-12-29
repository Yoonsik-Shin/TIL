N = int(input())
M = int(input())

materials = list(map(int,input().split()))
materialsDict = {}
count = 0

for i in range(N):
  materialsDict[materials[i]] = 1

for j in range(N):
  if (M-materials[j]) in materialsDict and materialsDict[materials[j]] == 1 and M-materials[j] != materials[j]:
    count += 1
    materialsDict[M-materials[j]] = 0
    materialsDict[materials[j]] = 0

print(count)