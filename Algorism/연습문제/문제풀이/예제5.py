# number = 22020718
# print(len(number))

'''
TypeError 발생

원인
: 정수값은 len()함수를 적용할 수 없음

해결법
: 정수값을 문자열로 바꾼 후 다시 계산 

'''

# 올바른 풀이
number = 22020718
number = str(number)
print(len(number))
