"Breadth First Search 넓이 우선 탐색"

# 시작 정점을 방문한 후 시작 정점과 인접한 정점들을 모두 차례로 방문하는 방법
# 방문한 다음 방금 방문한 정점에 인접하고 아직 방문하지 않은 정점들을 다시 모두 방문하는 과정을 반복
# 방금 방문한 정점과 인접한 정점들에 대해 탐색을 한 후 차례로 다시 너비 우선 탐색을 진행해야 하므로 선입선출 형태의 자료구조인 큐(Queue)를 활용
# 일반적인 시간 복잡도는 노드 수가 N개, 간선 수가 M개라고 할 경우, O(N+M)

def bfs(graph, start_node):
    visit_lst = []                      # 방문한 순서 리스트 생성
    queue = []                          # 방문할 순서 큐 생성
    queue.append(start_node)            # 큐에 처음 방문할 노드 삽입
    
    while len(queue) != 0:              # 큐가 없어질 때까지, 즉 더 이상 방문할 노드가 없을 때까지
        node = queue.pop(0)             # 큐에서 방문할 노드 값을 가져옴
        if node not in visit_lst:       # 해당 순서가 아직 방문한 적이 없는 곳일 경우
            visit_lst.append(node)      # 해당 노드를 방문하고 체크
            queue.extend(graph[node])   # 해당 노드에 연결된 근접 노드를 방문할 큐에 추가
            
    return visit_lst                    # 방문한 순서 리스트 리턴

graph = dict()                          # 그래프 생성

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'E']
graph['E'] = ['B']
graph['C'] = ['A', 'F']
graph['F'] = ['C', 'D', 'G']
graph['D'] = ['F']
graph['G'] = ['F']

print(graph)
print(bfs(graph, 'A'))                  # 방문 순서 출력