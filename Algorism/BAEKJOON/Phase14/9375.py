from itertools import combinations

T = int(input())

for i in range(T):

    n = int(input())
    dict_clothes = {}
    ans = 1

    for j in range(n):
        a, b = input().split()
        if b not in dict_clothes:
            dict_clothes[b] = 1
        else:
            dict_clothes[b] += 1

    k = list(map(int,dict_clothes.values()))
    for i in k:
        ans *= len(list(combinations(range(1,i+2), 1)))
    print(ans-1)