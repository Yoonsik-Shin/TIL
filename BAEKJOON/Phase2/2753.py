year = int(input())

cond1 = year%4 == 0 and not(year%100 == 0)
cond2 = year%400 == 0
leap_year = cond1 or cond2

if leap_year:
    print('1')
else:
    print('0')