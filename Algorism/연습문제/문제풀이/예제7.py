number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)

'''
에러발생 x, 원하는 값이 안나옴

원인
: 총합인 total은 잘 계산되었지만, 
리스트의 항목 개수를 세는 count가 잘못 계산됨

해결법
: count문을 for문 안으로 들여쓰기 해주어 반복적으로 더해질 수 있게해주기

'''

# 올바른 풀이
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total // count)