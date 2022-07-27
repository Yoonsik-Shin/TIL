x = input()

for i in range(len(x)):
    if x[i] == '(':
        count_l = x[:i].count('@')

    if x[i] == ')':
        count_r = x[i:].count('@')

print(count_l, count_r)