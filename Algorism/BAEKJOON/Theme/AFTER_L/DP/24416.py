n = int(input())

def fib(n):
    if (n == 1 or n == 2):
        return 1
    else: 
        return (fib(n - 1) + fib(n - 2))

dict_ = {}

def F(n):
    if n in dict_:
        return dict_[n]
    if n == 0:
        dict_[0] = 0
        return 0
    if n == 1:
        dict_[1] = 1
        return 1
    if n >= 2:
        dict_[n] = F(n-1) + F(n-2)
        return dict_[n]

