N = int(input())
count = 0

for i in range(N):

    word = input()
    dict = {}
    lst = []

    for j in word:
        if j not in dict:
            dict[j] = word.count(j)
    
    for key,value in dict.items():
        lst.append(key*value)

    for k in lst:
        if k not in word:
            break
    else:
        count+=1

print(count)