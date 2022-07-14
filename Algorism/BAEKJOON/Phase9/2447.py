N = int(input())

def f(n):
    if n == 3:
        n_3 = [['*','*','*'],['*',' ','*'],['*','*','*']]
        for i in range(n):
            for j in range(n):
                if j == 2:
                    print(n_3[i][j])
                else:
                    print(n_3[i][j],end='')
    else:

        return f(n/3)
