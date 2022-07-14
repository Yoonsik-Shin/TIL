N = input()
new = ''
count = 0

if int(N) < 10:
    N = '0'+N
    
new = N[1] + str((int(N[0])+int(N[1]))%10)

while True:
    if new == N:
        count += 1
        break
    else:
        new = new[1] + str((int(new[0])+int(new[1]))%10)
        count += 1

print(count)