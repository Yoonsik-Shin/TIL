lst = []

# 입력값 받기
for i in range(9):
  lst.append(int(input()))

checkPoint = sum(lst)-100  # 두수의 합 조건
checkOne = False  # 조건이 맞을 경우 첫번째 for문까지 종료

for m in range(9):
  if checkOne == False:  # 조건에 맞는 값을 찾지 못할때 두번째 for문 실행
    for n in range(9):
      if m == n:  # 같은 배열은 제외
        continue
      if lst[m] + lst[n] == checkPoint: # 두수의 합이 조건에 부합하면
        a, b  = lst[m], lst[n]
        checkOne = True
        break

lst.remove(a)
lst.remove(b)
lst.sort()

for j in lst:
  print(j)