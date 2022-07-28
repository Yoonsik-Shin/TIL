'''
> 음수 간선에 관한 최단경로문제는 다음과 같이 분류가능
 1. 모든 간선이 양수인 경우
 2. 음수 간선이 있는 경우
    > 음수 간선 순환이 없는 경우
    > 음수 간선 순환이 있는 경우

> 벨만포드 최단경로 알고리즘은 음의 간선이 포함된 상황에서도 사용할 수 있음
> 또한 음수 간선의 순환 감지 가능
> 기본 시간 복잡도는 O(VE)로 다익스트라보다 느림
'''

'''
실행로직
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 다음 과정을 N-1번 반복
    > 1. 전체 간선 E개를 하나씩 확인
    > 2. 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# 만약 음수 간선 순환이 발생하는지 체크하고 싶다면 3번의 과정을 한번 더 수행
    > 이때, 최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재하는 것
'''

'''
다익스트라 vs 벨만포드
다익스트라
> 매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
> 음수 간선이 없다면 최적의 해를 찾을 수 있음

벨만포드
> 매번 모든 간선을 전부 확인 (따라서 다익스트라 알고리즘에서의 최적의 해를 항상 포함)
> 시간이 오래 걸리지만 음수 간선 순환 탐지가능
'''

# 코드
import sys
input = sys.stdin.readline()
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def bf(start):
    dist[start] = 0 # 시작 노드에 대해서 초기화
    for i in range(n): # 전체 n번의 라운드를 반복
        for j in range(m): # 매 반복마다 '모든 간선'을 확인하며
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신 된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False        


n, m = map(int, input().split()) # 노드의 개수, 간선의 개수를 입력받기
edges = [] # 모든 간선에 대한 정보를 담는 리스트 만들기
dist = [INF] * (n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a,b,c))

# 벨만포드 알고리즘 수행
negative_Cycle = bf(1) # 1번 노드가 시작 노드

if negative_Cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우, -1 출력
        if dist[i] == INF:
            print('-1')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(dist[i])