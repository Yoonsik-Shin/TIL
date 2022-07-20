N = input()
lst = []

for i in N:
    lst.append(int(i))

lst.sort(reverse=True)

for j in lst:
    print(j, end='')