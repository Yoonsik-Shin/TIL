N = int(input())
lst = []
matrix = [[0]*100 for _ in range(100)]

for t in range(N):
    x, y = map(int,input().split())
    for i in range(100):
        for j in range(100):
            if i >= y and j >= x and i < y+10 and j < x+10:
                matrix[i][j] = 1
for m in matrix:
    lst.append(sum(m))

print(sum(lst))