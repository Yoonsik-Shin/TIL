A_count = int(input())
A_lst = list(map(int,input().split()))

A_lst.sort()

print(A_lst[0] * A_lst[-1])