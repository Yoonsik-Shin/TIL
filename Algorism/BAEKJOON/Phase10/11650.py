N = int(input())
lst2 = []

for i in range(N):
    lst = list(map(int,input().split()))
    lst2.append(lst)

lst2.sort()
lst3 = []

for j in range(len(lst2)):
    lst3.append(' '.join(list(map(str,lst2[j]))))
    
for k in lst3:
    print(k)