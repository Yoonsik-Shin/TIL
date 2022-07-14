word = 'banana'
lst = []
Dict = {}

for i in word:
    if i not in lst:
        lst.append(i)

count = 0
for j in lst:
    for k in word:
        if j == k:
            count+=1
    Dict[j] = count
    count = 0
for key in Dict:
    print(key, Dict[key])

'''
세트로 처리하면 순서가 변경돼 정답과 달라짐
'''

# s_lst = list(set(lst))
# print(s_lst)

# count = 0
# for j in s_lst:
#     for k in word:
#         if j == k:
#             count+=1
#     Dict[j] = count
#     count = 0
# for key in Dict:
#     print(key, Dict[key])]


# 풀이1

word = 'banana'

result = {}
for char in word:
    if not char in result:
        result[char] = 1
    else:
        result[char] += 1
print(result)


# 풀이2

word = 'banana'

result = {}
for char in word:
    result[char] = result.get(char, 0) + 1
print(result)