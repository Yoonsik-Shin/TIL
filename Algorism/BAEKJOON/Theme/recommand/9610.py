n = int(input())

Q1_count = 0
Q2_count = 0
Q3_count = 0
Q4_count = 0
axis_count = 0

for i in range(n):
    x, y = map(int,input().split())

    if x == 0 or y == 0:
        axis_count += 1
    elif x > 0 and y > 0:
        Q1_count += 1
    elif x < 0 and y > 0:
        Q2_count += 1
    elif x < 0 and y < 0:
        Q3_count += 1
    elif x > 0 and y < 0:
        Q4_count += 1

print(f'Q1: {Q1_count}')
print(f'Q2: {Q2_count}')
print(f'Q3: {Q3_count}')
print(f'Q4: {Q4_count}')
print(f'AXIS: {axis_count}')