N = int(input())

for i in range(1,N+1):
    if str(i).count('3') > 0 or str(i).count('6') > 0 or str(i).count('9'):
        print('-'*(str(i).count('3') + str(i).count('6') + str(i).count('9')), end=' ')
    else:
        print(i, end=' ')