A = int(input())
B = int(input())
C = int(input())

T = str(A*B*C)
for i in range(10):
    print(T.count(f'{i}'))
