A, B, C = map(int,input().split())
timeDict = {}
total = 0

for i in range(3):
  a, b = map(int,input().split())
  
  for j in range(a, b):
    if j not in timeDict:
      timeDict[j] = 1
    else:
      timeDict[j] += 1
      
for value in timeDict.values():
  if value == 1:
    total += A
  elif value == 2:
    total += (B*2)
  elif value == 3:
    total += (C*3)

print(total)