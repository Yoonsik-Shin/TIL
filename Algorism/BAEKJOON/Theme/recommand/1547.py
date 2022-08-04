M = int(input())

cup = [1, 2, 3]

for _ in range(M):
    change_l, change_r  = map(int,input().split())
    a = cup.index(change_l)
    b = cup.index(change_r)
    cup[a], cup[b] = cup[b], cup[a]
   
print(cup[0])