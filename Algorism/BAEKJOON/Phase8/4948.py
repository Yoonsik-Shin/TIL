import sys

while True: 
    n = int(sys.stdin.readline())
    if n:
        a = [False,False] + [True]*(2*n-1)
        lst = []

        for i in range(2, 2*n+1):
            if a[i]:
                lst.append(i)
                for j in range(2*i, 2*n+1, i):
                    a[j] = False

        count = 0

        for k in lst:
            if k > n:
                count+=1

        print(count)
    else:
        break