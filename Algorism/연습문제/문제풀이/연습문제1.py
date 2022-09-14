# n = 14

# if n%3 == 0 and n&2 == 0:
# 	print('참')
# else:
# 	print('거짓')

N = int(input())

A = sorted(map(int,input().split()))
B = map(int,input().split())
sorted_B = sorted(B, reverse=True)

S = 0

for i in range(N):
    S += A[i] * sorted_B[i]
    
print(S)