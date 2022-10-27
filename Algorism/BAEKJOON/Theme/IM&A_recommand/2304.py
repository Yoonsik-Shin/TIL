N = int(input())
lst = []

for _ in range(N):
    point = list(map(int,input().split()))
    lst.append(point)

lst.sort()

print(lst)
height = 0
max_height = sorted(lst, key=lambda x:x[1])[-1][1]
total = 0
for i in range(lst[-1][0]+1):
    for j in lst:
        
        if i == j[0]:
            if height < j[1]:
                height = j[1]
    total += height

print(total)