lst = []

while True:
    x = input()
    if x == '문제':
        lst.append(x)
    elif x == '고무오리':
        if '문제' not in lst:
            lst.append('문제')
            lst.append('문제')
        else:
            lst.pop()
    elif x == '고무오리 디버깅 끝':
        if len(lst) == 0:
            print('고무오리야 사랑해')
            break
        else:
            print('힝구')
            break