import sys

N = int(sys.stdin.readline())
dict_name = {}

for i in range(N):
    a = sys.stdin.readline().rstrip('\n')
    if a in dict_name:
        dict_name[a] -= 1
    else:
        dict_name[a] = 0

for j in range(N-1):
    dict_name[sys.stdin.readline().rstrip('\n')] += 1
    
ans = sorted(dict_name.items(), key=lambda x:x[1])[0][0]

print(ans)