T = int(input())

for i in range(1,T+1):
    x = input()
    if x[::-1] == x:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')