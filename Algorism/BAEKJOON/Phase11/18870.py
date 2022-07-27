import sys

N = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))

count_lst = [0] * N

for i in range(N-1):
    for j in range(i+1, N):
        if lst[i] < lst[j]:
            count_lst[j] += 1
        elif lst[i] > lst[j]:
            count_lst[i] += 1
        elif lst[i] == lst[j]:
            continue

lst2 = []
a = int(N/len(set(lst)))
for k in count_lst:
    ans = k//a
    print(ans, end=' ')
