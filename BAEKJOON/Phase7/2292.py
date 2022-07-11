N = int(input())

a, b, n = 1, 1, 1
while True:
    if b+6*n > N:
        break
    else:
        a = b+1
        b = b+6*n
        n+=1
n+=1
print(n)