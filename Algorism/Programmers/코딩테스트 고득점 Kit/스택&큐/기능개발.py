def solution(progresses, speeds): 
    p = list(reversed(progresses))
    s = list(reversed(speeds))
    answer = []
    count = 0
    
    while True:
        if sum(answer) == len(progresses):
            break
            
        
        for i in range(len(p)):
            if p[i] >= 100:
                p[i] = 100
                continue
            else:
                p[i] += s[i]
            
            
        if p[-1] == 100 and len(p):
            p.pop()
            count += 1
            while True:
                if len(p) == 0:
                    answer.append(count)
                    count = 0
                    break
                if p[-1] == 100:
                    p.pop()
                    count += 1
                else:
                    answer.append(count)
                    count = 0
                    break
                    
    return answer