# import sys
# sys.stdin = open('./Algorism/SWEA/level1/input.txt','r')

T = int(input())

for i in range(T):
    a, b = map(int,input().split())
    ans_1 = a//b
    ans_2 = a%b
    print(f'#{i+1} {ans_1} {ans_2}')