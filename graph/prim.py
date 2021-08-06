"Prim 프림 알고리즘"

# 최소 신장 트리 알고리즘 중 하나로 하나의 정점에 연결된 모든 간선들 중 가중치가 가장 작은 간선을 선택해가며 최소 비용 신장 트리를 만들어가는 방식
# 시작 정점에서부터 출발하여 신장 트리 집합을 단계쩍으로 확장해 나가는 방법이며 정점 선택을 기반으로 하는 알고리즘

# 알고리즘 순서는 다음과 같음
# 1. 모든 간선 정보를 저장 (edges)
# 2. 임의의 정점을 선택한 뒤 연결된 노드 집합 (selected_nodes)에 삽입
# 3. 선택된 정점에 연결된 간선들을 후보 간선 리스트(candidate_edges)에 삽입
# 4. 간선 리스트(candidate_edges)에서 최소 가중치를 가지는 간선부터 추출(pop)
# 5. 해당 간선에 인접한 정점들이 selected_nodes에 있을 경우, 사이클이 발생한 것으로 스킵
# 6. 없을 경우, 해당 간선을 최소 신장 트리 리스트(mst)에 삽입하고 인접 정점을 selected_nodes에 삽입
# 7. 삽입한 정점에 연결된 간선들 중 인접 정점이 selected_nodes에 없는 노드와 연결된 간선들만 candidate_edges에 삽입
# 8. candidate_edges가 없을 때까지 4~7번을 반복

# 최소 가중치를 정렬하기 위해서 최소힙 구조 사용 (heapq)

import heapq

def prim(graph, start_node):
    mst = []                                                                        # 최소 신장 트리 리스트 생성
    mst_weight = 0                                                                  # 가중치 변수
    edges = dict()                                                                  # 모든 간선 정보를 저장할 리스트 생성
    for n1, n2, weight in graph:                                                    # 모든 간선 정보를 리스트에 입력
        if n1 not in edges.keys():
            edges[n1] = [[weight, n1, n2]]                                          # 히프 정렬을 위하여 가중치를 첫번쨰 인덱스로 이동
        else:
            edges[n1].append([weight, n1, n2])

    selected_nodes = [start_node]                                                   # 시작 노드를 연결된 노드 집합에 삽입
    candidate_edges = edges[start_node]                                             # 선택된 정점에 연결된 간선들을 후보 간선 리스트에 삽입
    heapq.heapify(candidate_edges)                                                  # 가중치를 기준으로 오름차순 히프 정렬
    
    while len(candidate_edges) != 0:                                                # candidate_edges가 없을 때까지,
        selected_edge = heapq.heappop(candidate_edges)                              # 후보 간선 리스트에서 최소 가중치를 가지는 간선부터 추출
        start, end, weight = selected_edge[1], selected_edge[2], selected_edge[0]   # 간선의 start 노드, end 노드, weight를 변수로 생성 (이해를 위하여)
        if end in selected_nodes:                                                   # 도착 노드가 연결된 노드 집합에 있을 경우, 사이클 발생으로 스킵
            continue
        else:                                                                       # 없을 경우
            mst.append((start, end, weight))                                        # 최소 신장 트리 리스트에 삽입
            mst_weight += weight                                                    # 가중치 누적
            selected_nodes.append(end)                                              # 노드를 연결된 노드 집합에 추가
            candidate_edges = []                                                    # 도착 노드에서 다시 경로 판별을 위하여 후보 간선 리스트를 초기화
            heapq.heapify(candidate_edges)
            for elem in edges[end]:                                                 # 노드에 인접한 간선들을 탐색
                node = elem[2]                                                      # 간선의 도착 노드를 노드 변수로 만듬 (이해를 위하여)
                if node in selected_nodes:                                          # 도착 노드가 연결된 노드 집합에 존재할 경우 스킵
                    continue
                else:                                                               # 없을 경우
                    heapq.heappush(candidate_edges, elem)                           # 해당 경로를 판별을 위하여 후보 간선 리스트에 추가
    return [mst, mst_weight]            

graph = [                                       # 그래프 입력
    ('A','F',10),
    ('A','B',29),
    ('B','A',29),
    ('B','C',16),
    ('B','G',15),
    ('C','B',16),
    ('C','D',12),
    ('D','C',12),
    ('D','G',18),
    ('D','E',22),
    ('E','D',22),
    ('E','G',25),
    ('E','F',27),
    ('F','A',10),
    ('F','E',27),
    ('G','B',15),
    ('G','D',18),
    ('G','E',25)
]

ans = prim(graph, 'A')                      # 프림 알고리즘 수행
print("Minimum Spanning Tree:", ans[0])
print("Weight Cost:", ans[1])