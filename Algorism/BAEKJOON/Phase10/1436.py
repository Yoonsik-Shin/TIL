N = int(input())
i = 0
count = 0
dict_={}

while True:
    i += 1
    if str(i).find('666') != -1:
        dict_[i] = count
        count+=1
    if count == N:
        print(i)
        break