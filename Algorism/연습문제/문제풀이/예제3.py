# numbers = input().split()
# print(sum(numbers))

'''
TypeError 발생

원인
: input().split()은 문자열 리스트을 반환함
: sum함수는 문자열리스트를 연산할 수 없음

해결법
: numbers리스트의 값들을 map함수를 이용하여 정수형으로 변환해줌
'''

# 올바른 풀이
numbers = map(int,input().split())
print(sum(numbers))