T = int(input())
lst = list(range(10))

for i in range(1, T+1):

    N = input()
    lst2 = []
    count = 0
    
    while len(set(lst2)) != len(lst):
        k = str(int(N)*(count+1))
        for j in k:
            if j not in lst2:
                lst2.append(j)
        count+=1

    print(f'#{i} {k}')