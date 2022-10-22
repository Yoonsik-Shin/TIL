# T = int(input())

# for i in range(1, T+1):
#     string = input()
#     for j in range(1,10):
#         if string[:j+1] == string[j+1:j+1+len(string[:j+1])]:
#             print(f'#{i} {j+1}')
#             break



T = int(input())

for _ in range(1, T+1):
    word = input()
    for i in range(1, len(word)):
        if word[:i] == word[i:2*(i)]:
            print(f'#{_} {i}')
            break