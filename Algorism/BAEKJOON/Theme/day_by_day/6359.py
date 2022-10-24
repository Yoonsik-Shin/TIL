T = int(input())

for t in range(T):
    n = int(input())
    visited = [0] * (n+1)
    k = 0

    for _ in range(n):
        k += 1
        for i in range(k, n+1, k):
            if visited[i] == 0:
                visited[i] = 1
            else:
                visited[i] = 0

    print(sum(visited))
