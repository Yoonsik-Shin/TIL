# https://www.acmicpc.net/problem/11051 

from math import factorial

N, K = map(int,input().split())

ans = (factorial(N) // (factorial(K) * factorial(N-K))) % 10007

print(ans)


'''
# Fraction을 이용한 유리수 표현
from fractions import Fraction
# 2/3 표현
frac1 = Fraction(2, 3)
'''

# 부동 소수점 관련글
# https://blog.winterjung.dev/2020/01/06/floating-point-in-python