def han(x):
    total = 0
    for i in range(1,x+1):
        if i>=100:
            a = i//100 #백의자리
            b = (i-(a*100))//10 #십의자리
            c = i-(a*100)-(b*10) #일의자리
            if (a+b+c)/3 == b:
                total+=1
        elif i<100:
            total+=1
    return total

N = int(input())


print(han(N))

''' 
# 교훈
연산자 순서를 잘 생각하자!!
'''