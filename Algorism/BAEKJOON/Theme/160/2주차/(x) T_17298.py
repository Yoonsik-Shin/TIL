n = int(input())

A = list(map(int,input().split()))
re_A = A[::-1]
stack = []

for i in range(n):
  check = re_A.pop()

  if len(re_A) == 0:
      print(-1, end=' ')
      break

  while True:
    if len(re_A) == 0:
      print(-1, end=' ')
      for k in range(len(stack)):
        re_A.append(stack.pop())
      stack = []
      break

    comparison = re_A.pop()
    stack.append(comparison)

    if check < comparison:
      print(comparison, end=' ')
      for k in range(len(stack)):
        re_A.append(stack.pop())
      stack = []
      break
      
    


  # while True:
  #   if len(re_A) == 0:
  #     print(-1, end=' ')
  #     break
    
    
