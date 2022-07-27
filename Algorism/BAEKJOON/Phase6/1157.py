x = input().upper()
lst = []
ans_dict = {}

for i in x:
    if i not in lst:
        lst.append(i)

for i in lst:
    ans_dict[i] = x.count(i)

a = list(ans_dict.values())
b = sorted(ans_dict.items(), key = lambda x:x[1])

if a.count(max(a)) != 1:
    print('?')
else:
    print(b[-1][0])