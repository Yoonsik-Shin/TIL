count = int(input())
number = list(map(int,input().split()))

students_count = int(input())

for i in range(students_count):
    gender, given = map(int,input().split())

    if gender == 1:
        for j in range(count):
            if j % given == given-1: 
                if number[j] == 0:
                    number[j] = 1
                else:
                    number[j] = 0
    elif gender == 2:
        if given == 1:
            if number[0] == 0:
                number[0] = 1
            else:
                number[0] = 0
        else:

            if number[given-1] == 0:
                number[given-1] = 1
            else:
                number[given-1] = 0
             
            a = 1
            while True:
                if (given-1)-a < 0 or (given-1)+a >= count:
                    break
                if number[(given-1)-a] == number[(given-1)+a]:
                    if number[(given-1)-a] == 0:
                        number[(given-1)-a] = 1
                        number[(given-1)+a] = 1
                    else:
                        number[(given-1)-a] = 0
                        number[(given-1)+a] = 0
                    a += 1
                else:
                    break

for m in range(((count-1)//20)+1):
    ans = number[20*m : 20*(m+1)]
    print(*ans)