word = input()

for i in word:
    if i == 'A' or i == 'B' or i == 'C':
        print(chr(ord(i) + 23), end='')
    else:
        print(chr(ord(i) - 3), end='')