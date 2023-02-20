def solution(genres, plays):
    r = {}
    for i in range(len(genres)):
        if genres[i] not in r:
            r[genres[i]] = [(i, plays[i])]
        else:
            r[genres[i]].append((i, plays[i]))
    
    t = {}
    for k, v in r.items():
        total = 0
        for a in v:
            total += a[1]
        t[k] = total
        
    s = sorted(t.items(), key=lambda x:x[1], reverse=True)
    
    answer = []
    for k, _ in s:
        o = sorted(r[k], key=lambda x:(x[1], -x[0]))
        for i in range(2):
            if len(o) >= 1:
                answer.append(o.pop()[0])
            
    return answer