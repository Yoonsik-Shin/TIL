'''
내 풀이 >> 미해결
'''
# import math

# N = int(input())
# lst=[2,3]
# k = int(math.sqrt(N))

# for i in range(1,k):
#     e=0
#     for j in range(2,i+1):
#         if i%j == 0:
#             e+=1
#     if e == 1:
#         lst.append(i)

# for m in lst:
#     while N%m==0:
#         print(m)
#         N = N/m



'''
구글링
'''
import math

N = int(input())    # 나누어지는 수
d = 2               # 나누는 수
sqrt = int(math.sqrt(N)) # 나누어지는 수의 제곱근


while d <= sqrt:
    if N % d != 0:  # 나누어 떨어지지 않으면
        d += 1      # 나누는 수 1 증가
    else:           # 나누어 떨어지면
        print(d)    # 소인수니까 출력하고
        N //= d     # 나누어지는 수도 갱신

# 제곱근까지 나누어떨어지지 않으면, 소수이므로 그대로 출력
if N > 1:
    print(N)

'''
새로 알게된 개념
1. 소인수분해 아이디어
2. 시간복잡도 고려한 코딩
'''