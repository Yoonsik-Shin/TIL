N, M = map(int,input().split())

dict_ = {}

for i in range(N):
    dict_[input()] = 0

check_lst = []
for j in range(M):
    check_word = input()
    check_lst.append(check_word)

for k in check_lst:
    if dict_.get(k) == None:
        continue
    else:
        dict_[k] += 1

print(sum(dict_.values()))