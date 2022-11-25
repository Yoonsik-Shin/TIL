import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    x = input().strip('\n')
    
    a = True
    if x == '[]':
        a = False
    else:
        lst = deque(list(map(int,x.rstrip(']').lstrip('[').split(','))))

    for i in p:
        if i == 'R':
            if a == False:
                print('[]')
                break
            lst = list(lst)
            lst = lst[::-1]
            lst = deque(lst)
            
        elif i == 'D':
            if a == False:
                print('error')
                break
            if len(lst) == 0:
                print('error')
                break
            else:
                lst.popleft()
    else:
        print('[', end='')
        for j in range(len(lst)-1):
            print(lst[j], end=',')
        if len(lst) != 0:
            print(lst.pop(), end='')
        print(']')