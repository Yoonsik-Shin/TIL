T = int(input())

for i in range(T):
    a, b = map(int,input().split())
    if a > b:
        ans = '>'
    elif a == b:
        ans = '='
    elif a < b:
        ans = '<'
    print(f'#{i+1} {ans}')