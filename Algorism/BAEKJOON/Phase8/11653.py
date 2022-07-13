N = int(input())
lst=[]
k = int((N/2)+1)
# print(k)

for i in range(1,k):
    e=0
    for j in range(2,i+1):
        if i%j == 0:
            e+=1
    if e == 1:
        lst.append(i)

for m in lst:
    while N%m==0:
        print(m)
        N = N/m

## 미해결
