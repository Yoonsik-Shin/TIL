a,b = map(int,input().split())
c = bool(a)
d = bool(b)
print((c and d) or ((not c) and (not d)))