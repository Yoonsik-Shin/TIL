for i in range(1,10001):
    k = 0
    for j in range(len(str(i))):
        k = k + int(str(i)[j])
    print(k)
    # if k == i:
    #     continue
    
    # else:
    #     print(j)
