while True:
    lst = list(map(int,input().split()))

    if lst == [0,0,0]:
        break

    lst.sort()

    for i in range(3):
        lst[i] **= 2

    if lst[0] + lst[1] == lst[2]:
        print('right')
    else:
        print('wrong')