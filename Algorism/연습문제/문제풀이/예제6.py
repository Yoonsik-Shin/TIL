# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

'''
AttributeError 발생

원인
: 튜플은 생성,수정,삭제가 불가능하기 때문에 .append 메소드를 사용할 수 없음

해결법 
: answer값 초기화를 리스트 형식으로 만들어줌

'''

# 올바른 풀이
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)
