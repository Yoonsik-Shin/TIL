n, m = map(int,input().split())
visited = [0] * (n+1)
lst = []

def re(num):
    if num == m:
        print(' '.join(map(str,lst)))
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            lst.append(i)
            re(num+1)
            visited[i] = 0
            lst.pop()

re(0)