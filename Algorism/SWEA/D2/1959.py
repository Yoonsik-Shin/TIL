for t in range(1, int(input())+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    max_num = 0
    total = 0

    if N < M:
        for j in range(M-N+1):
            for i in range(N):
                total += B[i+j] * A[i]
            if total > max_num:
                max_num = total
            total = 0
    else:
        for j in range(N-M+1):
            for i in range(M):
                total += A[i+j] * B[i]
            if total > max_num:
                max_num = total
            total = 0
                
    print(f'#{t} {max_num}')