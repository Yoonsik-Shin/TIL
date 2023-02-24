from collections import deque

n, k = map(int,input().split())
visited = set()

def bfs(start, depth):
    if start == k:
      return depth
    queue = deque([(start, depth)])
    visited.add(start)

    while queue:
      c, dep = queue.popleft()
      m = c - 1
      p = c + 1
      d = 2 * c
      dep += 1
      
      if m == k or p == k or d == k:
        return dep
      else:
        if not m in visited and 0 <= m <= 100000: 
          visited.add(m)
          queue.append((m, dep))
        if not p in visited and 0 <= p <= 100000: 
          visited.add(p)
          queue.append((p, dep))
        if not d in visited and 0 <= d <= 100000: 
          visited.add(d)
          queue.append((d, dep))   
print(bfs(n, 0))
