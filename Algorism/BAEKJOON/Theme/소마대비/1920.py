n = int(input())
A = set(map(int,input().split()))
m = int(input())
check_list = list(map(int,input().split()))

for check in check_list:
  if check in A:
    print(1)
  else:
    print(0)