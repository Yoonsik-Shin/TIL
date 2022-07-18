# words = list(map(int, input().split()))
# print(words)

'''
ValueError 발생

원인
:문자열은 int형으로 변환될 수 없음

해결법
:input().split() 자체가 문자열을 반환하므로 이를 사용

'''

# 올바른 풀이
words = input().split()
print(words)
