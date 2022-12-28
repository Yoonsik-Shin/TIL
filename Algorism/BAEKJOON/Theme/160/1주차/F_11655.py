S = input()

def ROT13(word):
  for i in word:
    if i == ' ':
      print(' ', end='')
      continue
    if i.isnumeric():
      print(i, end='')
      continue

    if ord(i) >= 65 and ord(i) <= 90:
      if ord(i) < 78:
        print(chr(ord(i)+13), end='')
      else:
        print(chr(ord(i)-13), end='')
    else:
      if ord(i) < 110:
        print(chr(ord(i)+13), end='')
      else:
        print(chr(ord(i)-13), end='')

ROT13(S)