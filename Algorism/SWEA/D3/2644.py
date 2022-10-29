n = int(input())

a, b = map(int,input().split())

m = int(input())

lst = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int,input().split())
    lst[x].append(y)
    lst[y].append(x)

print(lst)

count = 



for j in lst[a]:
    if b in lst[j]:
        count += 1
    else:
        