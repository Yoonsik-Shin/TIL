N = int(input())
Pi_lst = list(map(int,input().split()))

Pi_lst.sort()
total = 0
total_min = 0

for i in Pi_lst:
    total += i
    total_min += total

print(total_min)