T = int(input())

for _ in range(T):
    lst = input().split()
    for rev in lst:
        rev = rev[::-1]
        print(rev, end=' ')