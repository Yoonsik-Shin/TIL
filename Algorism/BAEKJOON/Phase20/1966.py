from collections import deque

T = int(input())

for _ in range(T):
    count = 0
    N, M = map(int,input().split())
    print_lst = deque(map(int,input().split()))
    lst_order = deque([i for i in range(N)])

    while True:
        
        a = -1
        
        if max(print_lst) == print_lst[0]:
            print_lst.popleft()
            a = lst_order.popleft()
            count += 1
        else:
            print_lst.append(print_lst.popleft())
            lst_order.append(lst_order.popleft())

        if a == M:
            print(count)
            break