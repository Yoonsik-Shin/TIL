# 못품

def merge_sort(A):
    p = A[0]
    r = A[-1]

    if p < r:
        q = (p + r)//2
        
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)    


def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 1
    tmp = [0] * len[A]
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t+1] =  A[i+1]
        elif A[i] >= A[j]:
            tmp[t+1] = A[j+1]

    while i <= q:
        tmp[t+1] = A[i+1]
    while j <= r:
        tmp[t+1] = A[j+1]
    
    i = p
    t = 1
    while i <= r:
        A[i+1] = tmp[t+1]


N, K = map(int,input().split())
A = list(map(int,input().split()))

print(merge_sort(A))
print(A)