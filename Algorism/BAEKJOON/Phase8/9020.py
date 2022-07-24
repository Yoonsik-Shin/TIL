import sys

T = int(input())

for i in range(T):
    n = int(sys.stdin.readline())
    a = [0,0] + [1]*n
    lst = []

    for j in range(2, n+1):
        if a[j]:
            lst.append(j)
            for k in range(2*j, n+1, j):
                a[k] = False

    lst.sort(reverse=True)
    lst2 = []

    for m in lst:
        if n - m in lst and n - m <= m:
            lst2.append([n-m, n-(n-m)])
    print(lst2[-1][0], lst2[-1][1])



# 좀 더 나은 풀이
arr = [0 for i in range(10001)]
arr[1] = 1
for i in range(2,98):
    for j in range(i * 2,10001, i):
        arr[j] = 1
t = int(input())
for _ in range(t):
    a = int(input())
    b = a // 2
    for k in range(b,1,-1):
        if arr[a-k] == 0 and arr[k] == 0:
            print(k,a-k)
            break 

'''
시간을 줄이는 꼼수
:문제에 주어진 범위값을 이용하여 풀이
'''