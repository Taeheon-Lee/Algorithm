"Depth First Search 깊이 우선 탐색"

# 시작 정점에서 출발하여 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면
# 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 돌아온 뒤, 다른 방향의 정점으로 탐색을 계속 반복하여 모든 정점을 방문하는 순회 방법
# 가장 마지막에 만났던 갈림길의 점점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택(Stack)을 사용
# 일반적인 시간 복잡도는 노드 수가 N개, 간선 수가 M개라고 할 경우, O(N+M)

def dfs(graph, start_node):
    visit_lst = []                      # 방문한 순서 리스트 생성
    stack = []                          # 방문할 순서 스택 생성
    stack.append(start_node)            # 스택에 처음 방문할 노드 삽입

    while len(stack) != 0:              # 스택이 없어질 때까지, 즉 더 이상 방문할 노드가 없을 때까지
        node = stack.pop()              # 스택에서 방문할 노드 값을 가져옴
        if node not in visit_lst:       # 해당 순서가 아직 방문한 적 없는 곳일 경우
            visit_lst.append(node)      # 해당 노드를 방문하고 체크
            stack.extend(graph[node])   # 해당 노드에서 연결된 근접 노드를 방문할 스택에 추가
    
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
print(dfs(graph, 'A'))                  # 방문 순서 출력