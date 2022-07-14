word = 'banana'
change = ord('a')-ord('A')

for i in word:
    print(chr(ord(i)-change), end='')