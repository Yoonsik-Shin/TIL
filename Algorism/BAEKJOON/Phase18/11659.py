# 정답 / 부분합 사용
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
psum = [lst[0]]

for i in range(1, N):
    psum.append(lst[i]+psum[i-1])

for j in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(psum[j-1])
    else:
        print(psum[j-1]-psum[i-2])


# 시간초과
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

lst = list(map(int,input().split()))

for _ in range(M):
    i, j = map(int,input().split())
    print(sum(lst[i-1:j]))