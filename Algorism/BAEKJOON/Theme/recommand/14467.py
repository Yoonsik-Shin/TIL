N = int(input())
dict_cow = {}
count = 0

for _ in range(N):
    cow_num, cow_location = map(int,input().split())
    if cow_num not in dict_cow:
        dict_cow[cow_num] = cow_location
    elif cow_num in dict_cow and dict_cow[cow_num] == cow_location:
        continue
    else:
        count += 1
        dict_cow[cow_num] = cow_location

print(count)