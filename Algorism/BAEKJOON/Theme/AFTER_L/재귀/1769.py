X = input()
count = 0

while True:
    total = 0
    if len(X) != 1:
        for i in X:
            total += int(i)
        count += 1
    else:
        total = int(X)

    if len(str(total)) == 1:
        print(count)
        if total % 3 == 0:
            print('YES')
            break
        else:
            print('NO')
            break
    else:
        X = str(total)