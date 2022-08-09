lst = []

x = int(input())
a = False

for i in range(x+1):
    for j in str(i):
        if j == '4' or j == '7':
            a = True
        else:
            a = False
        
        if a == False:
            break
    
    if a == True:
        lst.append(i)

print(lst[-1])

# 더 괜찮은 풀이

# N = int(input())
# res = 0
# for i in range(N, 0, -1):
#     a = str(i)
#     for j in range(len(a)):
#         if a[j] != '4' and a[j] != '7':
#             break
#     else:
#         print(i)
#         break
