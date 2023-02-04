import sys
input = sys.stdin.readline
N = int(input())
rope_lst = []
ans = 0

for i in range(N):
  rope_lst.append(int(input()))

re = sorted(rope_lst, reverse=True)

for j in range(N):
  c = re.pop()
  if ans < c * (len(re)+1):
    ans = c * (len(re)+1)
  
print(ans) 
