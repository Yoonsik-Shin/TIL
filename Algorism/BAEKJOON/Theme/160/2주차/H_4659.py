from collections import Counter

vowels = ['a', 'e', 'i', 'o', 'u`']
can1 = 'ee'
can2 = 'oo'

while True:
  p = input()
  v_count = 0
  c_count = 0
  check = True

  if p == 'end':
    break

  if not any(_ in p for _ in vowels):
    check = False
    print(f'<{p}> is not acceptable.')
    continue
  
  if sorted(list(Counter(p).values()))[-1] >= 3:
    check = False
    print(f'<{p}> is not acceptable.')
    continue
  
  if can1 not in p and can2 not in p:
    for i in range(len(p)):
      if p[i] in vowels:
        v_count += 1
        c_count = 0
      else:
        c_count += 1
        v_count = 0
    if v_count >= 2 or c_count >= 2:
      check = False
      print(f'<{p}> is not acceptable.')
      continue
  
  if check:
    print(f'<{p}> is acceptable.')


