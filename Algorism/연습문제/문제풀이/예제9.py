from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

'''
에러발생 x, 원하는 값이 안나옴

원인
: if문의 실행문에서 딕셔너리에 값을 추가하는 논리가 틀렸음

해결법
: 딕셔너리에 값을 추가하는 방법인 'dict[key] = value' 형식으로 바꿔줌

'''

# 올바른 풀이
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1

pprint(fruit_count)