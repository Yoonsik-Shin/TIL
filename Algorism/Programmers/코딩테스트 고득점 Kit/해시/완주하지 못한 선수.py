import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

  
# 내 풀이
def solution(participant, completion):
    p_dict = {}
    
    for p in participant:
        if p in p_dict:
            p_dict[p] += 1
        else:
            p_dict[p] = 1

    for q in completion:
        if q in p_dict:
            p_dict[q] -= 1

    for k, v in p_dict.items():
        if v > 0:
            return k