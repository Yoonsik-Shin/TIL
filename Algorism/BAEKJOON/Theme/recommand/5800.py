X = int(input())

for class_number in range(1,X+1):
    lst = list(map(int,input().split()))
    lst2 = []
    score_lst = lst[1:]
    score_lst.sort(reverse=True)

    for i in range(len(score_lst)-1):
        lst2.append(score_lst[i] - score_lst[i+1])

    print(f'Class {class_number}')
    print(f'Max {max(score_lst)}, Min {min(score_lst)}, Largest gap {max(lst2)}')