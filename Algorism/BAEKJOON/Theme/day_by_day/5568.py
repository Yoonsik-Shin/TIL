from itertools import permutations

n = int(input())
k = int(input())
lst = []
lst2 = set()

for _ in range(n):
    lst.append(input())

for i in permutations(lst, k):
    lst2.add(''.join(i))

print(len(lst2))