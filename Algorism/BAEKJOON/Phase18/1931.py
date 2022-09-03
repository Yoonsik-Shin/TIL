N = int(input())
lst2 = []

for _ in range(N):
    lst = tuple(map(int,input().split()))
    lst2.append(lst)

lst2.sort()
print(lst2)
