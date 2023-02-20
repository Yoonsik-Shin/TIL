def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


# 내 풀이
from itertools import combinations

def solution(clothes):
    c_dict = {}
    answer = 1
    
    for i in clothes:
        if i[1] not in c_dict:
            c_dict[i[1]] = 1
        else:
            c_dict[i[1]] += 1
 
    k = list(c_dict.values())
    
    for j in k:
        answer *= len(list(combinations(range(1, j+2), 1)))
    
    return answer-1
  