word = 'kiwi '
count = 0

for i in word:
    if i == 'a':
        break
    count += 1
else:
    count = -1

print(count)