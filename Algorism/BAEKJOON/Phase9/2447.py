def recur(num):
    if num == 3:
        lst = ['***','* *','***']
        return lst
    else:
        new_star_list = [x*3 for x in recur(num//3)] + [x+' '*(num//3) + x for x in recur(num//3)] + [x * 3 for x in recur(num//3)]
        return new_star_list

N = int(input())

for i in recur(N):
    print(i)