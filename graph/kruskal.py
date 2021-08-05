"Kruskal 크루스칼 알고리즘"

# 최소 신장 트리(Minimum Spanning Tree)의 하나로 그래프의 모든 간선 중 가중치가 최소인 간선을 하나씩 더해가면서 최소 신장 트리를 만드는 방식
# 먼저 간선의 가중치를 기준으로 정렬한 후 최소 신장 트리가 될 때까지 최소 가중치 간선을 하나씩 선택해 감
# 선택한 간선과 연결되어 있지 않은 간선이라도 가중치가 작은 간선을 순서대로 신장 트리에 추가
# 전체 n개의 정점에 대하여 n-1개의 간선이 연결되면 종료

# 그래프에서 사이클의 판단은 서로소 집합 알고리즘(Union-Find)을 사용함
# 서로소 집합알고리즘은 Disjoint Set을 표현할 떄 사용하는 알고리즘으로 트리 구졸르 활용
# 간단하게, 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할(합칠) 때 사용

# Disjoint Set(서로소 집합 자료구조)이란 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
# 공통 원소가 없는 (서로소, 상호 배타적인) 부분 집합들로 나눠진 원소들에 대한 자료구조를 의미함

# 서로소 집합 알고리즘은 다음과 같은 과정으로 진행
# 1. 초기화 (n개의 원소가 개별 집합으로 이뤄지도록 초기화)
# 2. Find (여러 노드가 존재할 떄, 두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 그룹의 최상단 원소(루트 노드)를 확인)
# 3. Union (두 개별 집합을 하나의 집합으로 합침, 두 트리를 하나의 트리로 만듬)

# Union-Find 알고리즘에서 고려할 점
# Union 순서의 따라서, 최악의 경우, 링크드 리스트와 같은 형태(편향 트리 형태)가 될 수 있음
# 이 경우, 계산량이 O(N)이 될 수 있으므로, 이를 해결하기 위하여 Union-by-rank, Path compression 기법 사용
# 이를 사용할 경우, 계산량은 O(logN)으로 낮출 수 있음 

# Union-by-rank 기법
# 각 트리에 대해 높이(rank)를 기억해 두고, Union 시 두 트리의 높이가 다르면, 높이가 작은 트리를 높이가 큰 트리 아래에 붙임
# 즉 높이가 작은 노드의 루트 노드의 부모 노드로 높이가 큰 노드의 루트 노드를 연결

# Path Compression 기법
# Find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
# 즉 각 루트까지 연결된 노드들은 모두 루트 노드에 직접 연결하여 루트 노드를 한번에 알 수 있도록 만듬

def find(node):
    "경로 압축을 위한 연결된 제일 최상단 부모 노드를 찾는 함수, Path Compression 기법"
    while node != parent[node]:                 # 노드의 부모가 자기 자신 노드, 즉 제일 최상단 부모 노드일 때까지
        node = parent[node]                     # 노드의 부모 노드로 이동
    return node

def union(node1, node2):
    "경로가 연결되면 하나의 집합이 되기 때문에 하나의 집합으로 합치는 함수, Union-by-rank 기법"
    root1 = find(node1)                         # node1의 부모 노드 탐색
    root2 = find(node2)                         # node2의 부모 노드 탐색
    
    if rank[root1] > rank[root2]:               # node1의 루트가 node2의 루트 보다 큰 경우
        parent[root2] = root1                   # node2의 루트 노드의 부모 노드로 node1의 루트 노드를 연결
    else:                                       # 나머지의 경우
        if rank[root1] == rank[root2]:          # 만약 서로의 높이가 같은 경우, 
            rank[root2] += 1                    # node2의 루트 노드의 높이를 임의적으로 1 높여서 연결
        parent[root1] = root2                   # node1의 루트 노드의 부모 노드로 node2의 루트 노드를 연결
    
def init_list(node):
    "초기화 함수"
    parent[node] = node
    rank[node] = 0

def kruskal(nodes, graph):
    mst = list()
    mst_weight = 0
    
    for node in nodes:                          # 초기화
        init_list(node)
    
    graph.sort(key = lambda x:x[2])             # 가중치 기반 오름차순 정렬
    
    for edge in graph:
        node1, node2, weight = edge
        if find(node1) != find(node2):          # 두 개의 집합이 서로 다를 경우 (사이클을 생성하지 않는 경우)
            union(node1, node2)                 # Union 연산
            mst.append(edge)                    # 최소 신장 트리 경로로 추가
            mst_weight += weight                # 최소 신장 트리 경로 가중치 누적
            
    return [mst, mst_weight]

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']     # 노드 입력
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

parent = dict()
rank = dict()

ans = kruskal(nodes, graph)
print("Minimum Spanning Tree:", ans[0])
print("Weight Cost:", ans[1])