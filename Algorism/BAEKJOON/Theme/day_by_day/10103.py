n = int(input())

A = 100
B = 100

for i in range(n):
    a, b = map(int,input().split())

    if a > b:
        B -= a
    elif a < b:
        A -= b

print(A)
print(B)