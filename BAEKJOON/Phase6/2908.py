A,B = input().split()

def reverse(x):
    k_2 = x[0]
    k_1 = x[1]
    k_0 = x[-1]
    k = "".join([k_0,k_1,k_2])
    return k

lst = [reverse(A),reverse(B)]
print(max(map(int,lst)))