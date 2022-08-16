# https://www.acmicpc.net/problem/2635

from copy import deepcopy

N = int(input())
lst = [N]

def ans(N):

    max_count = -1e9

    for j in range(1,N+1):
        i = 0
        lst = [N]
        lst.append(j)

        while True:
            lst.append(lst[i]-lst[i+1])
            
            if lst[i+2] < 0:
                break

            i += 1
        
        if len(lst) > max_count:
            max_count = len(lst)-1
            lst.pop()
            ans_lst = deepcopy(lst)
    
    return ans_lst

print(len(ans(N)))
for _ in ans(N):
    print(_, end=' ')