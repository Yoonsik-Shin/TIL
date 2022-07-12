numbers = [0, 20, 100]

max = numbers[0]

for i in numbers:
    if max < i:
        max = i

numbers = list(set(numbers))
numbers.remove(max)

max = numbers[0]

for i in numbers:
    if max < i:
        max = i

print(max)