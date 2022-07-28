from collections import Counter

N = int(input())
book_list = []

for i in range(N):
    book_name = input()
    book_list.append(book_name)

ans = sorted(Counter(book_list).items(),key=lambda x:(-x[1],x[0]))
print(ans[0][0])