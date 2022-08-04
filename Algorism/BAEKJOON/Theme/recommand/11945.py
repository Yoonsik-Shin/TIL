N, M = map(int,input().split())

bread = [input()[::-1] for _ in range(N)]

for i in bread:
    print(i)