lst = list(range(0,31))
visited = [0] * 31

for i in range(1, 29):
    n = int(input())
    if n in lst:
        visited[n] = 1

for j in range(1, len(visited)):
    if visited[j] == 0:
        print(lst[j])