import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pocketMonDictNum = {}
pocketMonDictStr = {}

for i in range(N):
  listPocketMon = input().rstrip()
  pocketMonDictNum[i+1] = listPocketMon
  pocketMonDictStr[listPocketMon] = i+1

for j in range(1, M+1):
  pocketMon = input().rstrip()
  if pocketMon.isnumeric():
    print(pocketMonDictNum[int(pocketMon)])
  else:
    print(pocketMonDictStr[pocketMon])