# T = int(input())

# for i in range(T):
#     h_1, m_1, h_2, m_2 = map(int,input().split())
#     a = h_1*60 + m_1 + h_2*60 + m_2
#     if a // 60 == 12 or a // 60 == 24:
#         ans_h = 12
#     else:
#         ans_h = (a // 60) % 12
    
#     ans_m = (h_1*60 + m_1 + h_2*60 + m_2) % 60

#     print(f'#{i+1} {ans_h} {ans_m}')

for t in range(1, int(input())+1):
    times = list(map(int,input().split()))
    total_time = times[0]*60 + times[1] + times[2]*60 + times[3]
    hour = total_time // 60
    if hour > 12:
        hour -= 12
    minute = total_time % 60

    print(f'#{t} {hour} {minute}')