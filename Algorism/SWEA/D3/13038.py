for t in range(1, int(input())+1):
    n = int(input())
    lst = list(map(int,input().split()))
    lst2 = []
    print(lst)
    first = lst.index(1)
    a = True
    count = 0

    for j in range(7):
        if lst[j] == 1:
            lst2.append(j)

    if n == 1:
        print(f'#{t} 1')
    else:
        for _ in range(len(lst2)):
            n-=_
            while True:            
                if a == False:
                    break
                for i in range(7):
                    if lst[i] == 1:
                        n -= 1
                        count += 1
                        if n == 0:
                            a = False
                            break
                    elif count == 0:
                        continue
                    else:
                        count += 1
            print(f'#{t} {count-first}')

'''
1
2
0 1 0 0 1 1 1
'''