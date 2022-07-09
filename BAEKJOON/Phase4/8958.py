n = int(input())
num=1
total=0

for i in range(n):
    x = input()
    for j in x:
        if j == 'O':
            total += num
            num += 1
        elif j == 'X':
            num = 1
    print(total)
    num = 1
    total=0