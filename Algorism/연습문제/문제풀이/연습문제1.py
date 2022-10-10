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

# A, I = map(int,input().split())

# ans = A * (I-1)

# print(ans+1)

# N = int(input())

# for i in range(1, N+1):
#     print(' '*(N-i) + '*'*i)

# for j in range(N-1, 0,-1):
#     print(' '*(N-j) + '*'*j)

# N = int(input())
# lst = []

# for i in range(N):
#     x = input()
#     x_len = len(x)
#     lst.append(x)

# for k in range(x_len):
#     for j in range(N-1):
#         if lst[j][k] != lst[j+1][k]:
#             print('?', end='')
#             break
#     else:
#         print(lst[-1][k], end='')

# S = input()
# lst = []

# for i in range(len(S)):
#     lst.append(S[i:])

# for _ in sorted(lst):
#     print(_)

# words = input()
# nums = []
# for i in range(10):
#     nums.append(str(i))

# for word in words:
#     if word in nums or word == ' ':
#         print(word, end='')
#     elif (ord(word) >= 78 and ord(word) <= 90) or (ord(word) >= 110 and ord(word) <= 122):
#         print(chr(ord(word)-13), end='')
#     else:
#         print(chr(ord(word)+13), end='')

# from itertools import combinations

# x = input()
# y = input()
# a = False

# for i in range(len(x), 0, -1):
#     if a == False:
#         for j in list(combinations(x, i)):
#             if j in list(combinations(y, i)):
#                 ans = len(j)
#                 a = True
#                 print(ans)
# T = int(input())

# for _ in range(T):
#     word = input()
#     print(word[0], word[-1], sep='')

# b = int(input(), 8)
# print(bin(b)[2:])

# import sys
# input = sys.stdin.readline

# N, M = map(int,sys.stdin.readline().rstrip().split())
# account = {}

# for i in range(N):
#     id, password = sys.stdin.readline().rstrip().split()
#     account[id] = password

# for j in range(M):
#     print(account[sys.stdin.readline().rstrip()])


# from collections import Counter

# game = {
#     0:'E',
#     1:'A',
#     2:'B',
#     3:'C',
#     4:'D',
# }

# while True:
#     try:
#         x = map(int,input().split())
#         bae = Counter(x)[0]
#         print(game[bae])
#     except:
#         break

# x = input()

# print(int(x, 16))

# score = {
#     'A+':4.3,
#     'A0':4.0,
#     'A-':3.7,
#     'B+':3.3,
#     'B0':3.0,
#     'B-':2.7,
#     'C+':2.3,
#     'C0':2.0,
#     'C-':1.7,
#     'D+':1.3,
#     'D0':1.0,
#     'D-':0.7,
#     'F':0.0,
# }

# x = input()
# print(score[x])

# from math import lcm

# a, b = map(int,input().split())

# print(lcm(a,b))