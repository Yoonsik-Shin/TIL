lst_W = []
for W in range(10):
    lst_W.append(int(input()))

lst_K = []
for K in range(10):
    lst_K.append(int(input()))

lst_W.sort()
lst_K.sort()

ans_W = sum(lst_W[-3:])
ans_K = sum(lst_K[-3:])

print(ans_W, ans_K)