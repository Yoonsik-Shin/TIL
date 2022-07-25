from collections import Counter
import sys

sys.stdin = open('Algorism/SWEA/D2/1204.txt')

T = int(input())

for i in range(T):
    n = int(input())
    lst = map(int,input().split())
    ans = Counter(lst).items()
    ans = sorted(ans, key=lambda x:x[1], reverse=True)
    
    print(f'#{n} {ans[0][0]}')


# Counter 함수활용
'''
from collections import Counter

ans = Counter(순회가능한 것들)
'''