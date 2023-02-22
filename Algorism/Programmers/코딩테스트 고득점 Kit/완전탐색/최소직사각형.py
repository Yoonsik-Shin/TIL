def solution(sizes):
    sv = [sorted(size) for size in sizes]
    mv = max([max(s) for s in sv])
    
    for i in sv:
        if mv in i:
            c = i[0]
    
    a = 0
    for j in sv:
        if j[0] >= c and a < j[0]:
            a = j[0]
            
    return a * mv