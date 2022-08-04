from collections import Counter

lst = []

for i in range(10):
    lst.append(int(input()))

print(int(sum(lst)/10))
print(sorted(Counter(lst).items(), key=lambda x:x[1], reverse=True)[0][0])