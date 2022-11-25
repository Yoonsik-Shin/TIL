# 하노이 탑
def move(no, x, y):
    global count
    
    # no : 원반 갯수, x기둥에서 y기둥으로 옮김
    if no > 1:
        move(no-1, x, 6-x-y)

    lst.append((x, y))
    count += 1

    if no > 1:
        move(no-1, 6-x-y, y)

n = int(input())
count = 0
lst = []

move(n, 1, 3)
print(count)
for i in lst:
    print(*i)