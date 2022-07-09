lists = []

for i in range(1,11):
    lists.append(int(input())%42)

lists = set(lists)
print(len(lists))