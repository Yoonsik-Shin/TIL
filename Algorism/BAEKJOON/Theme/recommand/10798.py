lst2 = []
max_ = 0

for i in range(5):
    word = input()
    if len(word) > max_:
        max_ = len(word)
    lst = []
    for k in word:
        lst.append(k)
    lst2.append(lst)

for i in lst2:
    if len(i) != max_:
        i += [''] * (max_-len(i))

word = ''

for j in range(max_):
    for i in lst2:
        word += i[j]

print(word) 