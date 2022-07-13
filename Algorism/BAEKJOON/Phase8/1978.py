import collections

N = int(input())
lst = list(map(int,input().split()))
lst2 = []
lst3 = []

for i in lst:
    for j in range(1,i+1):
        if i%j == 0:
            lst2.append(i)

s = collections.Counter(lst2)

for k in range(len(s)):
    if list(s.values())[k] == 2:
        lst3.append(list(s.keys())[k])
print(len(lst3))

# 좀 더 나아보이는 풀이
number = int(input())
n = map(int, input().split())
sosu = 0

for i in n:
    error = 0 
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
                sosu += 1
print(sosu)