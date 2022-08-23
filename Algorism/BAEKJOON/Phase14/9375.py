from math import factorial

T = int(input())

for i in range(T):

    n = int(input())
    dict_clothes = {}

    for j in range(n):
        a, b = input().split()
        if b not in dict_clothes:
            dict_clothes[b] = 1
        else:
            dict_clothes[b] += 1