x = input()
total = 0

for i in range(len(x)):
    if i == 0:
        total += 10
        continue
    if x[i-1] == x[i]:
        total += 5
    else:
        total += 10

print(total)