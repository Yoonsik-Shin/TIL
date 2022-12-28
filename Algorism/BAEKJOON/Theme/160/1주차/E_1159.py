n = int(input())
firstNameDict = {}
SelectionList = []

for i in range(n):
  firstName = input()[0]

  if firstName not in firstNameDict:
    firstNameDict[firstName] = 1
  else:
    firstNameDict[firstName] += 1

for key, value in firstNameDict.items():
  if value >= 5:
    SelectionList.append(key)

SelectionList.sort()

print(''.join(SelectionList)) if SelectionList else print('PREDAJA')