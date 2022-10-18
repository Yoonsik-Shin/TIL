N = int(input())
order = list(map(int,input().split()))
lst = []

for i in range(1, N+1):
    if order[i-1] == 0:
        lst.append(i)
    else:
        lst.insert(len(lst)-order[i-1], i)
    

print(*lst)