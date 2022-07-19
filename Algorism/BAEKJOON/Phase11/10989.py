N = int(input())
lst = []

for i in range(N):
    x = int(input())
    lst.append(x)

lst.sort(reverse=False)

for j in lst:
    print(j)