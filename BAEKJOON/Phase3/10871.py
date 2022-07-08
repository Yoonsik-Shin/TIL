N, X = map(int,input().split())
lists = list(map(int,input().split()))
ans = []

for i in lists:
    if i < X:
        ans.append(i)

ans = map(str,ans)
ans = " ".join(ans)
print(ans)



# 괜찮은 풀이
n, x = map(int, input().split())
c = list(map(int, input().split()))

for i in range(n):
    if c[i] < x:
        print(c[i], end = " ")

# join함수 정리
# "구분자".join(문자열 리스트)