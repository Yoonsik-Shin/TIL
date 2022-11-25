import sys

N, M = map(int,input().split())

pocket_dict = {}

for i in range(1,N+1):
    str_i = str(i)
    a = sys.stdin.readline().rstrip('\n')
    pocket_dict[str_i] = a
    pocket_dict[a] = str_i

for j in range(M):
    print(pocket_dict[sys.stdin.readline().rstrip('\n')])