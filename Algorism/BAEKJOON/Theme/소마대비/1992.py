def re(row, col, n):
  global ans
  first = tree[row][col]

  for i in range(row, row+n):
    for j in range(col, col+n):
      if tree[i][j] != first:
        ans += '('
        re(row, col, n//2)
        re(row, col + n//2, n//2)
        re(row + n//2, col, n//2)
        re(row + n//2, col + n//2, n//2)
        ans += ')'
        return
  
  ans += first

n = int(input())
tree = []
ans = ''

for _ in range(n):
  tree.append(input())

re(0,0,n)
print(ans)