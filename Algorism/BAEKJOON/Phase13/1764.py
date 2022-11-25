import sys

N, M = map(int,input().split())
lst = []
lst2 = []
dict_ = {}

for i in range(N):
    x = sys.stdin.readline().rstrip()
    dict_[x] = 0

for j in range(M):
    y = sys.stdin.readline().rstrip()
    if dict_.get(y) == None:
        continue
    else:
        dict_[y]+=1

count = 0
for k,v in dict_.items():
    if v == 1:
        count += 1
        lst.append(k)

print(count)
for o in sorted(lst):
    print(o)



# for i in range(N):
#     x = sys.stdin.readline().rstrip()
#     lst.append(x)

# for j in range(M):
#     y = sys.stdin.readline().rstrip()
#     lst2.append(y)

# count = 0
# lst3 = []
# for i in lst:
#     if i in lst2:
#         count+=1
#         lst3.append(i)

# print(count)
# for i in sorted(lst3):
#     print(i)