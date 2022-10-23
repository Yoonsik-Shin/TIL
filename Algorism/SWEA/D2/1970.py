money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, int(input())+1):
    N = int(input())

    print(f'#{t}')
    for i in money:
        if N//i == 0:
            print(0, end=' ')
        else:
            print(N//i, end=' ')
            N %= i
    print()