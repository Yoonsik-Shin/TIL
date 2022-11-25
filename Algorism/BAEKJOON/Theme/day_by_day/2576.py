min_lst = []

for i in range(7):
    n = int(input())
    
    if n%2:
        min_lst.append(n)

min_lst.sort(reverse=True)

if len(min_lst):
    print(sum(min_lst))
    print(min_lst[-1])
else:
    print(-1)