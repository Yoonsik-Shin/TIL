import sys

T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split(sep=' '))
    print(A+B)


# 빠른 A+B
'''
새로 배운 개념
sys모듈 입력받기 >> sys.stdin.readline()
속도 더 빠름
'''