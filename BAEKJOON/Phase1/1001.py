x = input()
lists = []
lists = x.split(sep=' ')
lists = list(map(int,lists))
print(lists[0]-lists[1])