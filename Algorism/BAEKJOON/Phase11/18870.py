import sys

N = int(input())
lst = list(map(int,sys.stdin.readline().split()))
lst2 = list(set(lst))
lst2.sort()
print(lst2)
# dict = {}

# for i in lst2:
#     dict[i] = lst2.index(i)

