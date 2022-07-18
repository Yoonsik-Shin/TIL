number = int(input())
count = 1

while True:
    number = number/10
    if number < 1:
        break
    count += 1

print(count)