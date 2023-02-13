t = int(input())

for _ in range(t):
  stack = []
  check = list(input())

  for i in check:
    # 스택이 비어있을 때
    if not stack:
      # ( 이면 stack에 담아줌
      if i == '(':
        stack.append(i)
      # ) 이면 조건에 위배됨, 스택에 넣고 브레이크
      else:
        stack.append(i)
        break
    # 스택이 비어있지 않을 때
    else:
      # 스택의 마지막 괄호 ['('만 가능] 와 비교하여 같으면 스택에 추가
      if stack[-1] == i:
        stack.append(i)
      # () 가 되는 경우 스택에서 비워내기
      else:
        stack.pop()

  # 끝까지 스택에 값이 남아잇으면 짝을 이룰 수 없음
  if stack:
    print('NO')
  else:
    print('YES')
