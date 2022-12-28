S = input()
alphaDict = {}

for i in range(97, 123):
  alphaDict[chr(i)] = 0
  
for j in S:
  if j in alphaDict:
    alphaDict[j] += 1

for value in alphaDict.values():
  print(value, end=' ')