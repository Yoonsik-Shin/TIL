x = input()
lst=[]
lists=[]

# print(chr(97))
# print(chr(122))
for i in range(97,123):
    lst.append(chr(i))

for j in lst:
    lists.append(x.find(j))

ans = " ".join(list(map(str,lists)))
print(ans)


# 더 간결한 코드
l = input()

for i in range(97, 123, 1) :
    print(l.find(chr(i)), end=" ")

# end=' ' 사용법