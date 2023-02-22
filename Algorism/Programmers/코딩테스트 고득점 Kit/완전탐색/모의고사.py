def solution(answers):
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    c_one, c_two, c_three = 0, 0, 0
    
    for i in range(len(answers)):
        if one[i] == answers[i]:
            c_one += 1
        if two[i] == answers[i]:
            c_two += 1
        if three[i] == answers[i]:
            c_three += 1
    
    m = max(c_one, c_two, c_three)
    lst = [(1, c_one), (2, c_two), (3, c_three)]
    
    ans = []
    for j in lst:
        if j[1] == m:
            ans.append(j[0])
    
    return ans