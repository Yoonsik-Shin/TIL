# https://www.acmicpc.net/problem/7785
import sys

n = int(input())
dict_ = {}

for i in range(n):
    name, log = sys.stdin.readline().split()
    dict_[name] = log

reverse_dict_ = sorted(dict_.items(),reverse=True)

for i in reverse_dict_:
    if i[1] == 'enter':
        print(i[0])
    else:
        continue