x = input()
num = ''
total = 0

for i in x:
    if i == '-':
        total += int(num)
        num = '-'
        continue

    elif i == '+' and int(num) > 0:
        total += int(num)
        num = ''
        continue

    elif i == '+' and int(num) < 0:
        total += int(num)
        num = '-'
        continue

    num += i

else:
    total += int(num)

print(total)