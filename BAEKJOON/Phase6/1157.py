x = input().upper()
lst = []
lst2 = []

for i in x:
    lst.append(i)

# print(lst)

sets = list(set(lst))

# print(sets)

for j in sets:
    lst2.append(x.count(j))

# print(lst2)

lst3 = "".join(list(map(str,lst2)))

# print(lst3)
# print(lst3.find(str(max(lst2))))
# print(lst3.rfind(str(max(lst2))))
if lst3.find(str(max(lst2))) != lst3.rfind(str(max(lst2))):
    print('?')
else:
    print(sets[lst2.index(max(lst2))])