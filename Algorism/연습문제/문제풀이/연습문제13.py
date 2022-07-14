# My
word = 'apple'

print(word[::-1])


# 풀이
result = ''

for char in word:
    result = char + result

print(result)



# 내장 함수 이용
print(''.join(reversed(word)))



# index
for i in range(len(word)-1,-1,-1):
    print(word[i], end='')