"Floyd Warshall 플로이드 워셜 알고리즘"

# 모든 노드에서 다른 모든 노드까지의 경로를 모두 계산하여 모든 정점 사이의 최단 경로를 구하는 알고리즘
# 2차원 테이블(행렬)에 최단 거리 정보를 저장하며 진행
# 각 단계마다 특정한 노드(경유 노드) k를 거쳐 가는 경우를 확인
# 즉 출발 노드에서 도착 노드로 가는 최단 거리보다 경유지 k를 거쳐 가는 거리가 더 짧은지 검사하는 것
# 이에 대한 점화식은 "Dist(ab) = min(Dist(ab), Dist(ak)+Dist(kb), a는 출발지, b는 도착지, k는 경유지"
# 다익스트라 알고리즘과 달리 가중치가 음수의 경우에서도 적용 가능
# 그러나 음수 가중치가 사이클을 이루고 있는 경우는 작동 불가 (사이클을 이루는 구간의 가중치의 합이 음수이면 안됨)
# 3중 for문을 수행하기 때문에 복잡도는 O(n³)

def floyd(node, graph, start_node):
    dic_node_num = dict()                                                                       # 노드를 정수화 시킬 딕셔너리 생성
    dic_num_node = dict()                                                                       # 정수화 시킨 수의 노드 정보를 넣을 딕셔너리 생성
    i = 0
    for n in node:                                                                              # 노드 사전(딕셔너리) 생성
        dic_node_num[n] = i
        dic_num_node[i] = n
        i += 1

    matrix = [[float('inf') for _ in range(len(node))] for _ in range(len(node))]               # 2차원 테이블(행렬) 생성 및 무한으로 초기화

    for n in node:                                                                              # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
        matrix[dic_node_num[n]][dic_node_num[n]] = 0
    for edge in graph:                                                                          # 각 경로 정보를 행렬에 입력
        matrix[dic_node_num[edge[0]]][dic_node_num[edge[1]]] = edge[2]
    for k in range(len(node)):                                                                  # 점화식에 따라 플로이드 워셜 알고리즘 수행
        for start in range(len(node)):
            for end in range(len(node)):
                matrix[start][end] = min(matrix[start][end], matrix[start][k] + matrix[k][end])
    start_from = matrix[dic_node_num[start_node]]                                               # start_node에서 각 노드로 가는 최단 경로 정보 출력
    ans = []
    for i in range(len(start_from)):                                                            # 무한대로 남아 있는 정보는 경로가 없는 것이기 때문에 제거
        if start_from[i] != float('inf'):
            ans.append([dic_num_node[i], start_from[i]])
    return ans                                                                                  # 최단 경로 정보 리턴

node = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
graph = [                                                                                       # 방향 그래프 입력
    ('A','B',3),
    ('A','C',5),
    ('A','D',2),
    ('B','E',-4),
    ('C','F',6),
    ('D','G',3),
    ('F','C',-3),
    ('G','D',-6),
    ('E','H',4),
    ('F','H',8),
    ('G','H',7)
]
print("start from A :", floyd(node, graph, 'A'))