lst = []

while True:
    try:
        lst.append(input())
    except EOFError:
        break
        