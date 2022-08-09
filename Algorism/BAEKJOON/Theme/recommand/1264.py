lst = ['a', 'e', 'i', 'o', 'u']
lst2 = [' ', ',', '.', '!', '?']

while True:
    sentence = input()

    if sentence == '#':
        break

    for i in lst2:
        sentence = sentence.strip(i)

    sentence = sentence.lower()
    count = 0

    for i in sentence:
        if i in lst:
            count += 1

    print(count)