from itertools import permutations

n, m = map(int,input().split())

for i in list(permutations(range(1, n+1), m)):
  for j in i:
    print(j, end=' ')
  print()



# 또다른 풀이
N, M = map(int,input().split())

lst = []
visited = [0] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str,lst)))
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            lst.append(i)
            recur(num+1) # 재귀함수가 끝날때까지 밑에 구문은 실행이 안됨
            visited[i] = 0
            lst.pop()

recur(0)