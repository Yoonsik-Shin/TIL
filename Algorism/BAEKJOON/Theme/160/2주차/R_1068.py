def dfs(start):
  visited[start] = 1
  
  if len(tree[start]) != 0:
    for c in tree[start]:
      if not visited[c]:
        if tree[c]:
          dfs(c)
        else:
          tree[c].append(-1)
          visited[c] = 1
  else:
    tree[start].append(-1)

  return tree

n = int(input())
visited = [0] * (n)
tree = [[] for _ in range(n)]
nodes = list(map(int,input().split()))

for i in range(n):
  if nodes[i] == -1:
    continue
  tree[nodes[i]].append(i)

erased_node = int(input())

ret = dfs(erased_node)
for p in range(n):
  if erased_node in ret[p]:
    ret[p].remove(erased_node)

count = 0
for j in ret:
  if len(j) == 0:
    count += 1

print(count)