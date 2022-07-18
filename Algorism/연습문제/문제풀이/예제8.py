word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or "e" or "i" or "o" or "u":
        count += 1

print(count)


'''
에러발생 x, 원하는 값이 안나옴

원인
: 문자열 자체는 항상 True가 나옴,
따라서 char == 'a'값이 False여도 뒤에 나오는 문자열들이 무조건 True임으로
or 연산에 의해 char == 'a'값에 상관없이 True가 됨

해결법
조건을 따로따로 만들어주어야 함

'''

# 올바른 풀이
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)