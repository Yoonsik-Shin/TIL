# import sys
# input = sys.stdin.readline

# N = int(input())

# numbers = list(map(int,input().rstrip().split()))
# stack = []

# for i in range(N-1):
#     for j in range(i+1, N):
#         if numbers[i] < numbers[j]:
#             print(numbers[j], end = ' ')
#             break
#     else:
#         print(-1, end = ' ')

# print(-1)

N = int(input())
lst = list(map(int,input().rstrip().split()))
stack = []

for i in range(len(lst)):
    if len(stack) == 0:
        stack.append(i)
    elif stack[-1] < lst[i]:
        a = stack.pop()
        lst[a] = lst[i]

if len(stack) == 0:
    lst[-1] == -1
    print(lst)