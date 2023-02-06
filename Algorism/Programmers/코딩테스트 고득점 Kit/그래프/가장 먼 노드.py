from collections import deque

def solution(n, edge):
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for i in edge:
        [ v1, v2 ] = i
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        visited[start] = 1
        
        while queue:
            c = queue.popleft()
            for j in graph[c]:
                if not visited[j]:
                    visited[j] = visited[c] + 1
                    queue.append(j)
        return visited
    
    f_node = max(bfs(1))
    answer = visited.count(f_node)
    
    return answer