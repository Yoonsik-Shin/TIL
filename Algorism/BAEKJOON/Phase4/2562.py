lists = []
num = 0 

for i in range(1,10):
    x = int(input())
    lists.append(x)
    if lists[i-1] == max(lists):
        num = i

print(max(lists))
print(num)