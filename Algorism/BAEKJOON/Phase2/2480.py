x = list(map(int,input().split(sep=' ')))
sets = list(set(x))

if len(sets) == 1:
    print(10000+sets[0]*1000)
elif len(sets) == 2:
    print(1000+((sum(x)-sum(sets))*100)) # 생각하는데 애먹음
elif len(sets) == 3:
    print(max(x)*100)