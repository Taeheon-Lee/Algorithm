"Heap Sort 히프 정렬"

# 히프 자료구조를 사용하는 정렬 알고리즘으로 히프는 최댓값, 최솟값을 쉽게 추출할 수 있는 완전 이진 트리 형태의 자료구조
# 히프의 각 노드는 유일한 키값을 가지며, 모든 노드의 키값은 자식 노드의 키값보다 항상 크거나 같음 (루트 노드가 최대값)
# 오름차순에는 최소 히프를, 내림차순에는 최대 히프를 사용
# 먼저 정렬하고자 하는 데이터를 히프에 다 넣고 삭제 연산을 반복하여 순서대로 정렬된 결과를 얻음
# 삽입 연산은 우선 히프의 마지막 노드에 이어서 삽입하고 히프의 특성에 맞게 부모 노드들과 위치를 교환
# 삭제 연산은 루트 노드를 삭제하면서 출력
# 루트 노드를 삭제한 뒤 히프 노드의 가장 마지막 노드 값을 루트 노드로 가져와서 히프의 특성에 맞게 정렬한 뒤, 다시 루트 노드를 삭제하여 출력하는 방식으로 진행
# 히프 정렬은 완전 이진트리로 전체 높이는 logn이기 때문에 히프를 재구성하는 시간이 logn만큼 걸리며, 데이터 개수가 n개이면 nlogn의 시간이 소요됨으로 시간복잡도는 O(nlogn) (매우 효율적인 정렬 알고리즘)

# Method 1 Heap 구현

def heapify(lst, index, heap_size):
  largest = index                                             # 비교를 위하여 가장 큰 값으로 현재 부모 노드의 위치값을 선택
  left_idx = index * 2 + 1                                    # 부모 노드의 왼쪽 자식 노드
  right_idx = index * 2 + 2                                   # 부모 노드의 오른쪽 자식 노드
  if left_idx < heap_size and lst[left_idx] > lst[largest]:   # 왼쪽 자식 노드가 존재하고 선택된 값이 왼쪽 자식 노드의 값보다 작을 경우
    largest = left_idx                                        # 가장 큰 값을 왼쪽 자식 노드의 위치값으로 변경
  if right_idx < heap_size and lst[right_idx] > lst[largest]: # 오른쪽 자식 노드가 존재하고 선택된 값이 오른족 자식 노드의 값보다 작을 경우
    largest = right_idx                                       # 가장 큰 값을 오른쪽 자식 노드의 위치값으로 변경
  if largest != index:                                        # 가장 큰 값이 초기에 선택된 위치값과 다른 경우, 즉 부모 노드의 값이 자식 노드의 값보다 작을 경우
    lst[largest], lst[index] = lst[index], lst[largest]       # 부모 노드의 값과 자식 노드의 값을 서로 교환
    heapify(lst, largest, heap_size)                          # 부모 노드의 값이 자식 노드의 값보다 컸을 경우, 히프 자료구조의 특성상 아래에 모두 작은 값이기 때문에
                                                              # heapify 변환을 종료해도 되지만, 작아서 교환된 경우, 아래 더 큰 값이 존재할 수 있기 때문에 함수를 재귀적으로 수행 필요
def heap_sort(lst):
  length = len(lst)                                           # 리스트의 길이
  for i in range(length//2-1, -1, -1):                        # 히프 자료구조는 완전 이진트리 형태이기 때문에 각 부모 노드를 탐색
    heapify(lst, i, length)                                   # 각 부모 노드와 자식 노드를 히프 자료구조 형태로 변환
  for i in range(length-1, 0, -1):                            # 히프 자료구조 특성상 루트값이 가장 큰 값이기 때문에 해당 값을 리스트 가장 끝으로 이동 시키기 위하여 가장 뒤에서부터 탐색
    lst[0], lst[i] = lst[i], lst[0]                           # 가장 마지막 값과 루트값을 교환, 가장 큰 값이 리스트 마지막으로 이동 됨
    heapify(lst, 0, i)                                        # 마지막으로 이동된 큰 값은 고정된 값이기 때문에 다시 히프 자료구조와 시키는 리스트에서 제외하고 히프 자료구조화
  return lst                                                  # 최종 정렬된 리스트를 반환

lst = list(map(int, input().split()))                         # 리스트 값 입력
lst = heap_sort(lst)                                          # 히프 정렬 수행
print(lst)                                                    # 정렬된 리스트 출력

# 해당 방식은 최대 히프 자료구조 방식으로 정렬하며 오름차순 리스트를 만들기 위하여 사용한다.
# 최소 히프 자료구조 방식으로 내림차순 정렬을 하고 싶을 경우, 부등호를 반대로 바꾸면 된다.

# Method 2 Heap 패키지 import

import heapq                                                  # 히프 패키지 import

def heap_sort(lst):
    sorted_lst = []                                           # 정렬된 값을 저장하기 위한 리스트 입력
    heapq.heapify(lst)                                        # 입력된 리스트를 히프 자료구조화 시키는 함수
    while lst:
        sorted_lst.append(heapq.heappop(lst))                 # 생성한 리스트에 작은 값부터 출력시켜 삽입
    return sorted_lst                                         # 리스트를 반환

lst = list(map(int, input().split()))                         # 리스트 값 입력
                                                              # 입력과 동시에 히프 자료구조로 만들고 싶은 경우, heapq.heappush(lst, input()) 사용

lst = heap_sort(lst)                                          # 히프 정렬 수행
print(lst)                                                    # 정렬된 리스트 출력

# 방법 1과 달리, heapq 패키지는 최소 히프 자료구조 방식으로만 사용 가능하며 루트 값부터 차례대로 출력하여 오름차순으로 정렬하는 방식을 사용한다.
# 반대로 이를 오름차순을 위한 최대 히프 자료구조로 사용하고 싶을 경우, (우선 순위, 값) 구조의 튜플 또는 딕셔너리 자료 구조를 사용하여 기존 값을 음수화 시켜 우선 순위로 사용하여
# 정렬을 수행하고 1열의 값을 출력하는 방식으로 사용하면 된다.
# ex. heapq.heappush(heap, (-num, num))