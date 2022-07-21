N = int(input())
count = 1
k = 1
while N > k:
    count+=1
    k+=count

if count%2==0:
    print(f'{count-(k-N)}/{1+k-N}')
else:
    print(f'{1+k-N}/{count-(k-N)}')