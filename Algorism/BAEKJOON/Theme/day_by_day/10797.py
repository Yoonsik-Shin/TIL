x = input()
count = 0
lst = input().split()

for i in lst:
    if i[0] == x:
        count += 1

print(count)