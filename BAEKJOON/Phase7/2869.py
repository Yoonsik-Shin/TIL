import math
A, B, V = map(int,input().split())

C=A-B
D=V-A

print(math.ceil(D/C)+1)
