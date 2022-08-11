for i in range(3):
    number = list(map(int,input()))
    count = 1
    max_count = 1

    for j in range(len(number)-1):
        if number[j] == number[j+1]:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 1

    print(max_count)