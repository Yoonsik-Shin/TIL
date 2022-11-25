# pypy3 활용

def fib(n):
    global count_1
    if n == 1 or n == 2:
        count_1 += 1
        return 1
    else:
        return (fib(n-1)+ fib(n-2))

def fibonacci(n):
    global count_2
    lst_2 = [0, 1, 1]
    
    for i in range(3, n+1):
        lst_2.append(lst_2[i-2]+lst_2[i-1])
        count_2 += 1
    
    return lst_2[-1]
    
count_1 = 0
count_2 = 0
n = int(input())
fib(n)
fibonacci(n)
print(count_1, count_2)