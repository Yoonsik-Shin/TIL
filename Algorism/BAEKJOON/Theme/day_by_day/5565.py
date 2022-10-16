lst = []
for i in range(10):
    lst.append(int(input()))
print(lst[0]-sum(lst[1:]))