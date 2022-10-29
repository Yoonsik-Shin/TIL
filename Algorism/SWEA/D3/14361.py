from collections import Counter

for t in range(1, int(input())+1):
    
    N = input()
    count = len(N)
    k = 2
    a = N
    original = Counter(N)

    while True:
        if len(a) != count:
            print(f'#{t} impossible')
            break

        a = int(N)*k
        k+=1
        a = str(a)
        copy = Counter(a)
        if copy==original:
            print(f'#{t} possible')
            break