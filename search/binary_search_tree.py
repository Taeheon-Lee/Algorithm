"Binary Search Tree 이진 탐색 트리"

# 이진 트리의 형태로서 왼쪽 부분 트리에는 부모 노드보다 작은 키값이 위치하고, 오른쪽 부분에는 부모 노드보다 큰 키값이 위치하도록 조직된 형태
# 키값을 부모 노드와 비교하여 작으면 왼쪽 경로를 탐색하고 크면 오른쪽 경로를 탐색
# 데이터의 삽입, 삭제, 탐색 등이 자주 발생하는 경우에 효율적인 구조

# 이진 탐색 트리가 만족해야 할 성질은 다음과 같음
# 1. 모든 노트는 트리에서 유일한 키값을 가져야 함
# 2. 왼쪽 부분 트리에 있는 모든 노드의 키값들은 루트 노드의 키값보다 작음
# 3. 오른쪽 부분 트리에 있는 모든 노드의 키값들은 루트 노드의 키값보다 큼
# 4. 왼쪽 부분 트리와 오른쪽 부분 트리 모두 이진 탐색 트리

# 시간 복잡도는 이진 트리가 균형적으로 생성되어 있는 최선의 경우 O(logn)이며, 한쪽으로 치우친 현향 이진 트리의 경우, O(n)으로 순차 탐색과 시간 복잡도가 같음

class Node:                                     # 노드 생성
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def searchbst(bst, k):
    if bst == None:                             # 트리가 없는 경우
        return -1
    if bst.data == k:                           # 탐색 성공한 경우
        return bst
    if bst.data < k:
        return searchbst(bst.right, k)          # 노드 값보다 큰 경우 오른쪽 경로 탐색
    else:
        return searchbst(bst.left, k)           # 노드 값보다 작은 경우 왼쪽 경로 탐색

def insertbst(bst, k):                          # 트리 노드 삽입 함수
    new = Node(k)                               # 노드 생성
    p = bst
    if p == None:                               # 트리가 없는 경우
        return new
    while p != None:                            # 삽입할 노드를 트리의 끝단으로 이동
        if p.data > k:                          # 노드의 값보다 삽입할 값이 작은 경우
            if p.left == None:
                p.left = new
                break
            p = p.left
        else:
            if p.right == None:                 # 노드의 값보다 삽입할 값이 큰 경우
                p.right = new
                break
            p = p.right
    return bst

def deletebst(bst, k):                          # 트리 노드 삭제 함수
    p = bst
    while p != None:                            # 탐색 시작
        if p.data == k:
            break
        if p.data > k:
            p = p.left
        else:
            p = p.right
    if p == None:                               # 탐색 실패한 경우
        return -1
    if p.left == None and p.right == None:      # 삭제할 노드의 자식이 없는 경우
        p = None
    elif p.left != None and p.right != None:    # 삭제할 노드의 자식이 2개 모두 있는 경우
        start = p
        parent = p
        p = p.left                              # 왼쪽 경로의 가장 큰 값을 삭제할 노드의 값으로 끌어올림
        while p.right != None:
            parent = p
            p = p.right
        start.data = p.data
        parent.right = None
    else:                                       # 삭제할 노드의 자식이 1개 있는 경우
        start = p
        parent = p
        if p.right == None:                     # 왼쪽 자식이 존재하는 경우
            p = p.left                          # 왼쪽 경로의 가장 큰 값을 삭제할 노드의 값으로 끌어올림
            while p.right != None:
                parent = p
                p = p.right
            start.data = p.data
            parent.right = None
        else:                                   # 오른쪽 자식이 존재하는 경우
            p = p.right                         # 오른쪽 경로의 가장 작은 값을 삭제할 노드의 값으로 끌어올림
            while p.left != None:
                parent = p
                p = p.left
            start.data = p.data
            parent.left = None
    return bst

lst = list(map(int, input().split()))           # 삽입 리스트 입력
bst_lst = None
for elem in lst:                                # 트리에 삽입
    bst_lst = insertbst(bst_lst, elem)
key = int(input())
ret = searchbst(bst_lst, key)                   # 탐색 실행
print(False if ret == -1 else True)             # 결과 출력