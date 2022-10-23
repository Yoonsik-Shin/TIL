for t in range(1, int(input())+1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0

    while True:
        if N == 1:
            break
        if N%2 == 0:
            N//=2
            a += 1
            continue
        elif N%3 == 0:
            N//=3
            b += 1
            continue
        elif N%5 == 0:
            N//=5
            c += 1
            continue
        elif N%7 == 0:
            N//=7
            d += 1
            continue
        elif N%11 == 0:
            N//=11
            e += 1
            continue

    print(f'#{t} {a} {b} {c} {d} {e}')