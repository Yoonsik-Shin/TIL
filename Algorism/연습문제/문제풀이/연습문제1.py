# n = 14

# if n%3 == 0 and n&2 == 0:
# 	print('참')
# else:
# 	print('거짓')

# N = int(input())

# A = sorted(map(int,input().split()))
# B = map(int,input().split())
# sorted_B = sorted(B, reverse=True)

# S = 0

# for i in range(N):
#     S += A[i] * sorted_B[i]
    
# print(S)

# T = int(input())

# for i in range(T):
#     x, y = map(int,input().split())
#     print(y-1)

# n, m = map(int,input().split())

# print((n-1) + (m-1)*n)

# t = int(input())
# m = int(input())
# b = int(input())
# coke = int(input())
# soda = int(input())

# burger = [t, m, b]
# drink = [coke, soda]

# print(min(burger)+min(drink)-50)

# N = int(input())

# for i in range(N,0,-1):
#     print(' '*(N-i), end='')
#     print('*'*i)

# word = input()

# for i in range(len(word)):
#     if i == 0:
#         print(word[i], end='')
#     elif i % 10 == 0:
#         print()
#         print(word[i], end='')
#     else:
#         print(word[i], end='')


# while True:
#     try:
#         print(input())
#     except:
#         break

# N = int(input())
# for i in range(N):
#     print(' '*(N-1-i) + '*'*(2*i+1))

# N = int(input())

# for i in range(N):
#     print(' '*i + '*'*(2*(N-i)-1))

# for j in range(N-2, -1, -1):
#     print(' '*j + '*'*(2*(N-j)-1))

# N = int(input())

# for i in range(1, N):
#     print('*'*i + ' '*(2*(N-i)) + '*'*i)

# for j in range(N, -1, -1):
#     print('*'*j + ' '*(2*(N-j)) + '*'*j)

# N = int(input())

# for j in range(N-1, 0, -1):
#     print(' '*j + '*'*(2*(N-j)-1))

# for i in range(N):
#     print(' '*i + '*'*(2*(N-i)-1))

# S = input()

# dict_alpha = {}

# for i in range(97, 123):
#     dict_alpha[chr(i)] = 0

# for j in S:
#     if j in dict_alpha:
#         dict_alpha[j] += 1
    
# for k in dict_alpha.values():
#     print(k, end=' ')

# N = int(input())

# for i in range(1, N):
#     print('*'*i)

# for j in range(N,0,-1):
#     print('*'*j)

# total = 0
# lst = []

# for _ in range(4):
#     a, b = map(int,input().split())
#     total += (b-a)
#     lst.append(total)

# print(max(lst))