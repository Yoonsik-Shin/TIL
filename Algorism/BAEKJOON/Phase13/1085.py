x, y, w, h = map(int,input().split())

up = h-y
down = y
right = w-x
left = x

lst = [up, down, right, left]
print(min(lst))