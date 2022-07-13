C = int(input())
lst=[]

for i in range(C):
    lists = list(map(int,input().split()))
    N = lists.pop(0)
    avg = sum(lists)/N
    for j in lists:
        if j > avg:
            lst.append(j)
    print(f'{len(lst)/N*100:.3f}%')
    lst = []
