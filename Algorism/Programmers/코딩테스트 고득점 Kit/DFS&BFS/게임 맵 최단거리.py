from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = [[0]*m for _ in range(n)]
    
    def bfs(sr, sc):
        queue = deque()
        queue.append((sr, sc))
        visited[sr][sc] = 1
        
        while queue:
            cr, cc = queue.popleft()
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                
                if nr<0 or nr>=n or nc<0 or nc>=m: continue
                if maps[nr][nc] == 1 and not visited[nr][nc]: 
                    visited[nr][nc] = 1
                    maps[nr][nc] = maps[cr][cc] + 1
                    queue.append((nr,nc))
        return maps
    
    if bfs(0, 0)[n-1][m-1] == 1:
        return -1
    else:
        return bfs(0, 0)[n-1][m-1]