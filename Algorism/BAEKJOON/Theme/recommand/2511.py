A = list(map(int,input().split()))
B = list(map(int,input().split()))
count_A = 0
count_B = 0
win_lose_lst = []

for i in range(10):
    if A[i] > B[i]:
        count_A += 3
        win_lose_lst.append('A')
    elif A[i] < B[i]:
        count_B += 3
        win_lose_lst.append('B')
    else:
        count_A += 1
        count_B += 1
        win_lose_lst.append('D')

print(count_A, count_B)

if count_A > count_B:
    print('A')
elif count_A < count_B:
    print('B')
elif count_A == count_B:
    if A == B:
        print('D')
    else:
        for j in win_lose_lst[::-1]:
            if j == 'D':
                win_lose_lst.pop()
            else:
                print(win_lose_lst[-1])
                break