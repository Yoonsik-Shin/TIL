T = int(input())

for i in range(T):
    h_1, m_1, h_2, m_2 = map(int,input().split())
    a = h_1*60 + m_1 + h_2*60 + m_2
    if a // 60 == 12 or a // 60 == 24:
        ans_h = 12
    else:
        ans_h = (a // 60) % 12
    
    ans_m = (h_1*60 + m_1 + h_2*60 + m_2) % 60

    print(f'#{i+1} {ans_h} {ans_m}')