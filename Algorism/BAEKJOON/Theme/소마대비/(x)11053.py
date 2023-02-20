n = int(input())
A = list(map(int,input().split()))
lst = []
check = 0

for i in A:
  if i > check:
    lst.append(i)
    check = i

print(len(lst))