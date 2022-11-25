from copy import deepcopy

N, K = map(int,input().split())
lst = [_ for _ in range(2, N+1)]
test = False
count = 0
lst_copy = deepcopy(lst)

while True:
    if test == True:
        break

    P = lst_copy[0]
    for i in range(len(lst)):
        if lst[i]%P == 0:
            a = lst[i]
            try:
                lst_copy.remove(lst[i])
            except:
                continue
            count += 1
        if count == K:
            test = True
            break

print(a)

# 더 좋은 풀이
import sys
input = sys.stdin.readline


def find(n,k):
    count = 0
    nlist = [True for i in range(n + 1)]
    for i in range(2,n+1):
        for j in range(i, n+1, i):
            if nlist[j] != True:
                continue 
            nlist[j] = False
            count += 1
            if count == k:
                return j

N, K= map(int,input().split())
print(find(N,K))