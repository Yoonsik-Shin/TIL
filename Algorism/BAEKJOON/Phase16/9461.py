def P(n):
    lst = [0, 1, 1, 1]

    for i in range(4, n+1):
        lst.append(lst[i-3]+lst[i-2])

    return lst[-1]

T = int(input())

for _ in range(T):
    N = int(input())
    print(P(N))