N = input()

N_lst = list(map(int,list(N)))

print(N_lst)
print(max(N_lst))
print(min(N_lst))
reversed_lst = list(reversed(N_lst[i:])).index(min(N_lst))
print(reversed_lst)

# if N_lst[0] == min(N_lst):

# for i in N_lst:
#     if N_lst[i] == min(N_lst)