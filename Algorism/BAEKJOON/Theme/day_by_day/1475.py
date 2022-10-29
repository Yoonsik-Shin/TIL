N = input()
count = 0
a = N.count('6') + N.count('9')
if a%2 == 0:
    count += a//2
    for i in range(10):
        if i == 6 or i == 9:
            continue
        else:
            if N.count(str(i)) > count:
                count = N.count(str(i))

else:
    count = (a+1)//2
    for j in range(10):
        if j == 6 or j == 9:
            continue
        else:
            if N.count(str(j)) > count:
                count = N.count(str(j))

print(count)