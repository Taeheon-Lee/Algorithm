"우선 순위 큐를 이용한 다익스트라 알고리즘 구현"

import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):

    # start로 부터 거리 값을 저장하기 위하여 distances 변수 사용
    distances = {node: float('inf') for node in graph}   # (-)inf는 (음)양의 무한대 (float 형에서만 사용 가능하며, 알고리즘 문제 풀이 시, 최솟값, 최댓값을 구할 때 자주 사용)

    # 시작 거리 값을 0으로 지정
    distances[start] = 0

    # 노드를 넣을 우선 순위 큐 리스트 생성
    queue = []

    #시작 노드부터 탐색을 시작하기 위하여 큐 리스트에 시작 값 입력
    heapq.heappush(queue, [distances[start], start])    # 우선 순위 큐에 값을 삽입 시, 최소 값 순서대로 저장되는데 리스트를 값으로 삽입 시, 리스트의 첫(0)번째 인덱스를 기준으로 사용

    # queue에 남아 있는 노드가 없을 때까지 반복
    while queue:

        # 탐색 할 거리(current_distance)와 노드(current_destination)를  가져옴
        current_distance, current_destination = heapq.heappop(queue)    # 우선 순위 큐에서 첫 번째 인자 즉 가장 작은 값을 꺼내는 명령

        # 기존에 있는 거리보다 길다면, 더이상 찾을 필요가 없기 때문에 skip
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():    # graph 내부의 current_destination 위치의 인자 값을 2개의 변수에 대입

            # 해당 노드를 거쳐 갈 때의 거리
            distance = current_distance + new_distance

            # 알고 있는 거리 보다 작으면 갱신
            if distance < distances[new_destination]:
                distances[new_destination] = distance

                # 다음 인접 거리를 계산 하기 위하여 큐에 삽입
                heapq.heappush(queue, [distance, new_destination])

    # inf 값이 남아 있는 노드는 도착할 수 없는 노드이기 때문에 제거
    ans = {}
    for elem in distances.keys():
        if not distances[elem] == float('inf'):
            ans[elem] = distances[elem]
    return ans

print("Start from A :", dijkstra(graph, 'A'))
print("Start from B :", dijkstra(graph, 'B'))
print("Start from C :", dijkstra(graph, 'C'))
print("Start from D :", dijkstra(graph, 'D'))
print("Start from E :", dijkstra(graph, 'E'))
print("Start from F :", dijkstra(graph, 'F'))