from statistics import median

lst = []

for i in range(5):
    lst.append(int(input()))

avg = sum(lst) // 5
med = median(lst)    

print(avg)
print(med)