N = int(input())
total = 0
i = 0

while True:
    total += i
    if total >= N:
        break
    i += 1
print(i)