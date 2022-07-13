N = int(input())
lists = list(map(int,input().split()))
M = max(lists)
new_list = []

for i in lists:
    new_list.append((i/M)*100)

print(sum(new_list)/N)

# 더 간결한 풀이
N = int(input())
a=list(map(int, input().split()))
print(sum(a)/max(a)*100/len(a))