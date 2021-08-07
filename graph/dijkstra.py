"Dijkstra 다익스트라 알고리즘"

# 최단 경로 알고리즘의 하나로, 하나의 시작점을 기준으로 나머지 정점 사이의 최단 경로를 구하는 알고리즘, "단일 출발점 최단 경로"라고 함
# 어떠한 간선도 음수 값의 갖중치를 가지지 않아야 하며, 단일 출발점에서 다른 모든 정점까지의 최단 경로를 찾아줌
# 방향 그래프, 무방향 그래프 모두 사용 가능
# 탐욕 알고리즘을 기반으로 하며, 가중치 정렬을 위하여 우선 순위 큐(heapq)구조 사용

# 알고리즘의 순서는 다음과 같음

# 1단계 (초기화)
# 시작점을 기준으로 배열을 선언하여 시작점에서 각 정점까지의 거리를 저장 (배열은 딕셔너리 사용, dist{})
# 1-1. 생성한 dist에 시작 정점(start_node)과 목적지 정점들(end)까지의 경로를 dist[end][0], 가중치(거리)를 dist[end][1]로 정의
# 1-2. 첫 정점의 거리를 dist[start_node][0]=[start_node], dist[start_node][1]=0으로 입력하고 나머지 목적지 정점들의 dist[end][0]=[], dist[end][1]=∞(infinity)로 초기화
# 1-3. 우선 순위 큐 자료 구조로 생성 (candidate_edges)
# 1-4. 최초 시작점을 [첫 정점 거리(0), 첫 정점(start_node)]으로 우선 순위 큐에 삽입

# 2단계
# 우선 순위 큐에서 추출한 [0, start_node]를 기반으로 인접한 노드와의 거리 계산
# 2-1. 처음은 첫 정점만 저장되어 있기 때문에 첫 정점 [0, start_node]가 꺼내짐
# 2-2. 각 인접한 노드들에 대해, 첫 정점에서 각 정점까지의 거리를 비교
# 2-3. 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리와 경로를 업데이트
# 2-4. 각 노드까지의 거리는 ∞으로 초기화 되어 있기 떄문에 첫 정점에서 인접한 노드까지 가는 거리로 모두 업데이트 됨
# 2-5. 배열에 해당 노드의 거리가 업데이트된 경우, 해당 경로는 유의미하기 때문에 우선 순위 큐에 삽입

# 3단계
# 우선 순위 큐에서 첫 노드부터 특정 경로까지 유의미한 경로들 중 가장 작은 가중치를 가진 노드를 추출하여 해당 노드와 인접한 노드와의 거리 계산 
# 3-1. 우선 순위 큐는 최소 힙 방식으로 heappop 연산을 수행할 경우, 첫 노드부터 특정 경로까지 유의미한 경로들 중 가장 작은 가중치를 가진 노드가 추출
# 3-2. 추출된 경로는 이미 업데이트 된 경로이며, 해당 경로와 인접한 경로들을 탐색하여 인접한 노드들까지의 거리가 기존 해당 노드경로까지의 거리보다 짧을 경우 이 경로로 업데이트
# 3-3. 해당 경로 또한 유의미한 경로이기 때문에 우선 순위 큐에 삽입
# 3-4. 우선 순위 큐에 데이터가 모두 없어질 때까지 반복

import heapq

def dijkstra(edges, start_node):
    # 1 단계
    dist = {node : [[], float('inf')] for node in edges.keys()}         # 시작 정점(start_node)과 목적지 정점들(end)까지의 경로와 가중치(거리)를 저장할 dist 생성하고 ∞으로 초기화
    dist[start_node] = [[start_node], 0]                                # 목적지 정점이 시작 정점인 것은 이동할 필요가 없기 때문에 경로['A'], 거리 0으로 입력
    candidate_edges = []                                                # 우선 순위 큐 생성
    heapq.heappush(candidate_edges, [dist[start_node][1], start_node])  # 첫 정점 삽입
    
    # 2~3 단계
    while candidate_edges:
        current_weight, current_end = heapq.heappop(candidate_edges)    # 우선 순위 큐에서 경로 추출
        if dist[current_end][1] < current_weight:                       # 해당 경로가 기존 경로보다 큰 경우 경로 추출 경로 무시 (2단계 inf 확인 목적)
            continue
        for new_end, new_weight in edges[current_end].items():          # 추출된 경로의 인접 경로 탐색
            weight = current_weight + new_weight                        # 시작점부터 추출된 경로를 통한 인접 경로까지의 거리값 계산
            path = dist[current_end][0] + [new_end]                     # 시작점부터 추출된 경로를 통한 인접 경로까지의 경로 입력
            if weight < dist[new_end][1]:                               # 계산된 경로가 기존 해당 목적지까지의 경로보다 작을 경우
                dist[new_end][0] = path                                 # 거리값 업데이트
                dist[new_end][1] = weight                               # 경로 업데이트
                heapq.heappush(candidate_edges, [weight, new_end])      # 해당 업데이트된 경로를 유의미한 경로로 판단하고 우선 순위 큐에 삽입
    ans = {}
    for elem in dist.keys():
        if not dist[elem][1] == float('inf'):                           # 최종 결과 값에 inf가 존재할 경우, 해당 경로는 연결되지 않은 경로이기 때문에 경로에서 제거
            ans[elem] = dist[elem]
    return ans
    

graph = {                                                               # 방향 그래프 입력
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
print(dijkstra(graph, 'A'))                                             # dijkstar 알고리즘 수행