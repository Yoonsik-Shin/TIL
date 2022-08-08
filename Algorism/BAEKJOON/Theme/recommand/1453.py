N = int(input())

lst = list(map(int,input().split()))
lst2 = []
count = 0

for i in lst:
    if i not in lst2:
        lst2.append(i)
    else:
        count += 1

print(count)