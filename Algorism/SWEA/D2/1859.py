T = int(input())

for _ in range(1, T+1):
    N = int(input())
    count = 0
    total = 0
    stack_total = 0
    a = 0
    lst = list(map(int,input().split()))
    
    for i in range(N, 0, -1):
        num = lst[i] 
        if i+1 == N:
            stack_total += num
            count += 1
            total += ((stack_total * (-1)) + (count * num))
        elif num > lst[i+1]:
            if num == max(lst[a:]):
                a = i+1
                total += ((stack_total * (-1)) + (count * num))
                count = 0
                stack_total = 0
            else:
                stack_total += num
                count += 1            
        else:
            stack_total += num
            count += 1

    print(f'#{_} {total}')