L, P = map(int,input().split())
lst = list(map(int,input().split()))

guess = L * P

for i in lst:
    print(i - guess, end=' ')