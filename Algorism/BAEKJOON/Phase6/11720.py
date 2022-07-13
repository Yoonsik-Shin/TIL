N = int(input())
x = input()
total = 0

for i in range(N):
    total += int(x[i])

print(total)


# 더 간결한 풀이
n = int(input())

print(sum(map(int, input())))