N = int(input())

fact = 1

for i in range(1,N+1):
    fact *= i

count = 0
for j in range(len(str(fact))-1,0,-1):
    if str(fact)[j] == '0':
        count += 1
    else:
        break

print(count)