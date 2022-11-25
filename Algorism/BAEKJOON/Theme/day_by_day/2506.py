N = int(input())
lst = list(map(int,input().split()))
a = 0
total = 0

for i in range(N):
    if lst[i] == 1:
        a += 1
        total += a
    elif lst[i] == 0:
        a = 0

print(total)