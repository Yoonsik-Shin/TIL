N_1, N_2 = map(int,input().split())

N = max(N_1, N_2)
lst = []

for i in range(1, N+1):
    if N_1 % i == 0 and N_2 % i == 0:
        lst.append(i)
    
least = lst[-1]
print(least)
print(least * (N_1//least) * (N_2//least))