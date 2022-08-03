A, B = input().split()

Max_A, Max_B = A, B
Min_A, Min_B = A, B

for a in Max_A:
    if a == '5':
        Max_A = Max_A.replace(a,'6')

for b in Max_B:
    if b == '5':
        Max_B = Max_B.replace(b,'6')

for a in Min_A:
    if a == '6':
        Min_A = Min_A.replace(a,'5')

for b in Min_B:
    if b == '6':
        Min_B = Min_B.replace(b,'5')

print(int(Min_A)+int(Min_B) , int(Max_A)+int(Max_B))