S = input()
lst = []

for i in range(len(S)):
    for j in range(i+1,len(S)+1):
        lst.append(S[i:j])

print(len(set(lst)))