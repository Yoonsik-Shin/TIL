w, h, x, y, p = map(int,input().split())
r = h//2
count = 0

for i in range(p):
    a, b = map(int,input().split())

    if x > a and (x-a)**2+((y+r)-b)**2 <= r**2:
        count += 1
    elif x <= a and x+w >= a and y <= b and y+h >= b:
        count += 1
    elif x+w < a and (x+w-a)**2+((y+r)-b)**2 <= r**2:
        count += 1

print(count)