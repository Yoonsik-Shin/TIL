'''
BFS (Breadth-First Search)
> 너비 우선 탐색
> 가까운 노드부터 우선적으로 탐색
> 큐 자료구조 이용
'''
'''
실행 로직
1. 탐색 시작 노드를 큐에 삽입하고 방문처리
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접노드 중에서 방문하지 않은 노드를 모두 큐에
   삽입하고 방문처리
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
'''

# 코드
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)