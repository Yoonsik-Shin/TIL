def solution(array, commands):
    answer = []
    
    for i in commands:
        one = array[i[0]-1:i[1]]
        two = sorted(one)
        three = two[i[2]-1]
        answer.append(three)
    
    return answer