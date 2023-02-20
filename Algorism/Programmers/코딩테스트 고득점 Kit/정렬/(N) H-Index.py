def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        # 1. hIndex는 n-i입니다.
        hIndex = n-i
        # 2. citations[i]가 hIndex보다 크거나 같으면, answer에 hIndex를 저장하고 반복을 멈춥니다. 
        if citations[i] >= hIndex:
            answer = hIndex
            break
    
    return answer