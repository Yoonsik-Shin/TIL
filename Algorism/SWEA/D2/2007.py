T = int(input())

for i in range(1, T+1):
    string = input()
    for j in range(1,10):
        if string[:j+1] == string[j+1:j+1+len(string[:j+1])]:
            print(f'#{i} {j+1}')
            break