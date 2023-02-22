n = int(input())
graph = []
o = 0
x = 0
for _ in range(n):
  graph.append(list(map(int,input().split())))

def re(row, col, n):
  global o, x
  first = graph[row][col]
  
  for i in range(row, row+n):
    for j in range(col, col+n):
      if graph[i][j] != first:
        re(row, col, n//2)
        re(row, col + n//2, n//2)
        re(row + n//2, col, n//2)
        re(row + n//2, col + n//2, n//2)
        return
  if first == 0:
    x += 1
  else:
    o += 1

re(0, 0, n)

print(x)
print(o)
