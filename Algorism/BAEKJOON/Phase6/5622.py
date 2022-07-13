x = input()

dicts = {}
dicts['A'] = 2
dicts['B'] = 2
dicts['C'] = 2
dicts['D'] = 3
dicts['E'] = 3
dicts['F'] = 3
dicts['G'] = 4
dicts['H'] = 4
dicts['I'] = 4
dicts['J'] = 5
dicts['K'] = 5
dicts['L'] = 5
dicts['M'] = 6
dicts['N'] = 6
dicts['O'] = 6
dicts['P'] = 7
dicts['Q'] = 7
dicts['R'] = 7
dicts['S'] = 7
dicts['T'] = 8
dicts['U'] = 8
dicts['V'] = 8
dicts['W'] = 9
dicts['X'] = 9
dicts['Y'] = 9
dicts['Z'] = 9

ans = []
for i in x:
    ans.append(dicts[i]+1)
    
print(sum(ans))