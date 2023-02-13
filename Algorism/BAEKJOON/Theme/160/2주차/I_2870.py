N = int(input())
lst = []

for _ in range(N):
  word = input()
  num = ''

  for i in range(len(word)):
    if word[i].isnumeric():
      if num == '0':
        num = ''
        num += word[i]
      else:
        num += word[i]
    else:
      if num != '':
        lst.append(int(num))
        num = ''
  else:
    if num != '':
      lst.append(int(num))

ans = sorted(lst)

[print(a) for a in ans]