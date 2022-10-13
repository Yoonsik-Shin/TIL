
def DFS(n):
    
    if n == N:
        return DFS(n+1)
    else:
        print(n, end=' ')

N, M = map(int,input())
print(DFS(1))