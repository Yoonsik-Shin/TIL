N = input()

new=''
i=0

if int(N)>=10:
    A = N[0]
    B = N[1]
    C = int(A)+int(B)
    new_C = C%10
    new = B+str(new_C)
    i += 1
elif N == '0':
    new = N
    i += 1
elif int(N)<10:
    new_N = '0'+ N[0]
    new = N[0]+new_N[1]
    i += 1


while True:
    if int(new)>=10:
        A = new[0]
        B = new[1]
        C = int(A)+int(B)
        new_C = C%10
        new = str(int(B+str(new_C)))
        i += 1
        if N==new:
            break
    elif int(new) == 0:
        break
    elif int(new)<10:
        new_N = '0'+ new[0]
        new = new[0]+new_N[1]
        i += 1
        if N==new:
            break

print(i)

#-----------------------------------------------------------------
#못품