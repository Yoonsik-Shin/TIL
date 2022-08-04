# https://www.acmicpc.net/problem/2512

# my
N = int(input())
lst = list(map(int,input().split()))
M = int(input())

min = min(lst)
max = max(lst)

for i in range(max,min,-1):
    for j in range(N):
        if lst[j] > i:
            lst[j] = i
    if sum(lst) <= M:
        print(i)
        break

# 이분탐색 활용

N = int(input())
lst = list(map(int,input().split()))
M = int(input())

# 상한액이 upper_bound일 때, 필요한 예산을 계산하는 함수
def calculate_needed_budget(upper_bound: int) -> int:
    needed_budget = 0
    for i in lst:
        needed_budget += min(i, upper_bound)

    return needed_budget

# 이분 탐색을 수행하는 메인 로직
low = 0
high = max(lst)
good_upper_bound = -1

while low <= high:
    mid = (low + high) // 2

    if calculate_needed_budget(mid) <= M:
        good_upper_bound = mid
        low = mid + 1
    else:
        high = mid - 1

answer = -1
for j in lst:
    given = min(j, good_upper_bound)
    answer = max(answer, given)
print(answer)