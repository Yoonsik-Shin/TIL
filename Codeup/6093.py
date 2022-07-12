n = int(input())
lst = list(map(int,input().split()))

lst = lst[::-1]
for i in range(n):
    print(lst[i],end=" ")
    
# ans = " ".join(map(str,lst))
# print(ans)