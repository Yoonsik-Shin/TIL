n = int(input())
i = 0
total = 0

while True:
    total+=i
    i+=1
    if total >= n:
        print(total)
        break