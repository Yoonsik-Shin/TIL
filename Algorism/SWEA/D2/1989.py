# T = int(input())

# for i in range(1,T+1):
#     x = input()
#     if x[::-1] == x:
#         print(f'#{i} 1')
#     else:
#         print(f'#{i} 0')


for t in range(1, int(input())+1):
    word = input()
    if word == word[::-1]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')