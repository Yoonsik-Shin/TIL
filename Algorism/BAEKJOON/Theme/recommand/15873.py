n = input()

if n[1] == '0' and len(n) == 3:
    A = int(n[:2])
    B = int(n[-1])
    print(A+B)
elif n[1] != '0' and len(n) == 3:
    A = int(n[0])
    B = int(n[1:])
    print(A+B)
elif n == '1010':
    A = 10
    B = 10
    print(A+B)
else:
    A = int(n[0])
    B = int(n[1])
    print(A+B)