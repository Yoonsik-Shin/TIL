demension = []

for j in range(10):
    lst = list(map(int,input().split()))
    demension.append(lst)

demension[1][1] = 9

for i in range(1,9):
    if demension[i][i+1] == 2:
        demension[i][i+1] = 9
        break
    elif demension[i+1][i] == 2:
        demension[i+1][i] = 9
        break
for m in range(1,9):
    if demension[m][m+1] == 0:
        demension[m][m+1] = 9
    elif demension[m][m+1] == 1:
        demension[m+1][m] = 9
        

for k in demension:
    ans = ' '.join(list(map(str,k)))
    print(ans)