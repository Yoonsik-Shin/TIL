# number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")


'''
TypeError 발생

원인
: max라는 예약어를 변수로 사용해 max에 상수가 반환되어버려 max함수로써의 기능을 상실함

해결책
: 첫 번째 리스트의 최대값 변수명을 바꿔줌

'''

# 올바른 풀이
number_list = [1, 23, 9, 6, 91, 59, 29]
max_1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max_2 = max(number_list2)

if max_1 > max_2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max_1 < max_2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")