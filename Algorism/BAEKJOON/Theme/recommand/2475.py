lst = list(map(int,input().split()))
total = 0

for i in lst:
    total += i**2

print(total%10)