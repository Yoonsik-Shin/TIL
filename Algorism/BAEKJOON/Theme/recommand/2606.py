computer_count = int(input())
edge_count = int(input())

lst = [[] for _ in range(computer_count+1)]

for i in range(edge_count):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

ans_lst = lst[2:]
count = 0
lst2 = []


for j in ans_lst:
    for k in lst[1]:
        if k in j:
            lst2.append(j)
# print(lst2)
# set_ = set()
# for j in lst2:
#     for m in j:
#         set_.add(m)

# if 1 in set_:
#     set_.remove(1)

# print(set_)