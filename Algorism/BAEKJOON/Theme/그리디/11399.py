N = int(input())
lst = list(map(int,input().split()))
sorted_lst = sorted(lst)
lst2 = []
total = 0

for i in sorted_lst:
  total += i
  lst2.append(total)

print(sum(lst2))