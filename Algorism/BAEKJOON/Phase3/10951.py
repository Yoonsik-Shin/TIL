import sys

while True:
    try:
        A, B = map(int,sys.stdin.readline().split())
        print(A+B)
    except:
        break


# 예외처리
'''
try:
    print(~)
except:
    print(~~)
'''