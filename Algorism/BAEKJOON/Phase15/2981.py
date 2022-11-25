# 시간초과
import sys
input = sys.stdin.readline

def divide(num, i):
    while num >= i:
        num %= i
    return num

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()
set_ = set()
max_lst = lst[-1]

for i in range(2, max_lst):
    for j in lst:
        set_.add(divide(j, i))
        if len(set_) == 0:
            continue
        elif len(set_) != 1:
            break

    if len(set_) == 1:
        print(i, end=" ")

    set_ = set()