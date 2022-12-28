N = int(input())
pattern = input()
point = pattern.find('*')
patternStart = pattern[:point]
patternEnd = pattern[point+1:]

for _ in range(N):
  needValidationWord = input()
  if len(needValidationWord) < len(pattern)-1:
    print('NE')
  else:
    if needValidationWord[:len(patternStart)] == patternStart and needValidationWord[(-1)*len(patternEnd):] == patternEnd:
      print('DA')
    else:
      print('NE')