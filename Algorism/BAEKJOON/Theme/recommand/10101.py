angles = []

for _ in range(3):
    angles.append(int(input()))

if angles[0] == 60 and angles[1] == 60 and angles[2] == 60:
    print('Equilateral')
elif sum(angles) == 180 and ((angles[0] == angles[1] and angles[0] != angles[2]) or (angles[1] == angles[2] and angles[0] != angles[1]) or (angles[2] == angles[0] and angles[1] != angles[2])):
    print('Isosceles')
elif sum(angles) == 180 and (angles[0] != angles[1] and angles[0] != angles[2] and angles[1] != angles[2]):
    print('Scalene')
else:
    print('Error')