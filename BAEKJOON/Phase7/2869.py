import math
A, B, V = map(int,input().split())

C=A-B
D=V-A

print(math.ceil(D/C)+1)


# k=(A-B)n 하룻밤 지난 위치
# V-k < A 도착 하루 전 위치