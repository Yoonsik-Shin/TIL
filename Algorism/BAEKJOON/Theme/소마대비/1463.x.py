# 그리디 알고리즘인줄 알았으나, 중간에 예외가 존재함
# 모든 경우 봐야함 => DP활용
# 개념 헷갈림

X = int(input())
count = 0

while True:
  # 종료조건
  if X == 1:
    break

  if X % 3 == 0:
    count += 1
    X //= 3
  elif X % 2 == 0:
    count += 1
    X //= 2
  else:
    X -= 1
    count += 1

print(count)