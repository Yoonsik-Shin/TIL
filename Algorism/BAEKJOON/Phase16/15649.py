N, M = map(int,input().split())

lst = []
visited = [0] * (N+1)

def recur(num):
    k = 0
    if num == M:
        print(' '.join(map(str,lst)))
    for i in range(k, N+1):
        if visited[i] == 0:
            visited[i] = 1
            lst.append(i)
            recur(num+1) # 재귀함수가 끝날때까지 밑에 구문은 실행이 안됨
            visited[i] = 0
            lst.pop()

recur(0)