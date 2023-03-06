from collections import deque
from pprint import pprint

visited = [
      [0,  0,  0,  0,  0,  0,  0,  0,  0],
      [0, -1, -1, -1, -1, -1, -1, -1,  0],
      [0, -1,  0,  0,  0,  0,  0, -1,  0], 
      [0, -1,  0,  0,  0,  0,  0, -1,  0], 
      [0, -1, -1, -1,  0,  0, -1, -1,  0],
      [0,  0,  0, -1,  0,  0, -1,  0,  0], 
      [0,  0, -1, -1,  0,  0, -1, -1, -1], 
      [0,  0, -1,  0,  0,  0,  0,  0, -1], 
      [0,  0, -1, -1, -1,  0, -1, -1, -1], 
      [0,  0,  0,  0, -1, -1, -1,  0,  0], 
    ]

def bfs(sr, sc):
        queue = deque()
        queue.append((sr, sc))
        visited[sr][sc] += 1
        
        while queue:
            cr, cc = queue.popleft()
            for d in direction_4:
                dr, dc = d
                nr = cr + dr
                nc = cc + dc
                
                if nr < 1 or nr >= 10 or nc < 1 or nc >= 9: continue
                if visited[nr][nc] == -1:
                    visited[nr][nc] = visited[cr][cc] + 1
                    # if nr == itemY-1 and nc == itemX-1:
                    #     return visited[nr][nc]
                    queue.append((nr, nc))
        return visited

graph = set()
direction_8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
direction_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = bfs(3, 1)
pprint(ans)
print(ans[8][7])