N = int(input())

b, n = 1, 1
while True:
    if b >= N:
        break
    else:
        b = b+6*n
        n+=1
print(n)