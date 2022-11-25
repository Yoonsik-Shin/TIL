import sys
input = sys.stdin.readline

N, M = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(N)]
psum = []
psum_2 = []

for i in range(N):
    for j in range(N):
        if len(psum) != 0:
            psum.append(psum[j-1] + matrix[i][j])
        elif len(psum) == 0:
            psum.append(matrix[i][j])

    psum_2.append(psum)
    psum = []

for k in range(M):
    total = 0
    x1, y1, x2, y2 = map(int,input().split())

    for o in range(x1-1, x2):
        if y1 == 1:
            total += psum_2[o][y2-1]
        else:
            total += psum_2[o][y2-1] - psum_2[o][y1-2]
    
    print(total)