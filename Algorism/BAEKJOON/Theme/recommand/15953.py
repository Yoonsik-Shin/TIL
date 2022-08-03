price_1 = [5000000, 3000000, 2000000, 500000, 300000, 100000]
lst_1 = []
k = 2
for i in price_1:
    for _ in range(1,k):
        lst_1.append(i)
    k+=1

price_2 = [(2**9)*(10**4), (2**8)*(10**4), (2**7)*(10**4), (2**6)*(10**4), (2**5)*(10**4)]
lst_2 = []
p = 2

for j in price_2:
    for _ in range(1,p):
        lst_2.append(j)
    p = (p*2)-1

T = int(input())

for _ in range(T):
    a, b = map(int,input().split())
    if a > 21 and b <= 31:
        if b == 0:
            print(0)
        else:
            print(lst_2[b-1])
    elif a <= 21 and b > 31:
        if a == 0:
            print(0)
        else:
            print(lst_1[a-1])
    elif a > 21 and b > 31:
        print(0)
    elif a == 0:
        if b == 0:
            print(0)
        else:
            print(lst_2[b-1])
    elif b == 0:
        if a == 0:
            print(0)
        else:
            print(lst_1[a-1])
    else:
        print(lst_1[a-1] + lst_2[b-1])