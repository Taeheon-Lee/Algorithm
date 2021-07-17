"Heap Sort 히프 정렬"

# 히프 자료구조를 사용하는 정렬 알고리즘으로 히프는 최댓값, 최솟값을 쉽게 추출할 수 있는 완전 이진 트리 형태의 자료구조
# 히프의 각 노드는 유일한 키값을 가지며, 모든 노드의 키값은 자식 노드의 키값보다 항상 크거나 같음 (루트 노드가 최대값)
# 오름차순에는 최소 히프를, 내림차순에는 최대 히프를 사용
# 먼저 정렬하고자 하는 데이터를 히프에 다 넣고 삭제 연산을 반복하여 순서대로 정렬된 결과를 얻음
# 삽입 연산은 우선 히프의 마지막 노드에 이어서 삽입하고 히프의 특성에 맞게 부모 노드들과 위치를 교환
# 삭제 연산은 루트 노드를 삭제하면서 출력
# 루트 노드를 삭제한 뒤 히프 노드의 가장 마지막 노드 값을 루트 노드로 가져와서 히프의 특성에 맞게 정렬한 뒤, 다시 루트 노드를 삭제하여 출력하는 방식으로 진행
# 히프 정렬은 완전 이진트리로 전체 높이는 logn이기 때문에 히프를 재구성하는 시간이 logn만큼 걸리며, 데이터 개수가 n개이면 nlogn의 시간이 소요됨으로 시간복잡도는 O(nlogn) (매우 효율적인 정렬 알고리즘)

def heapify(lst, index, heap_size):
  largest = index
  left_idx = index * 2 + 1
  right_idx = index * 2 + 2
  if left_idx < heap_size and lst[left_idx] > lst[largest]:
    largest = left_idx
  if right_idx < heap_size and lst[right_idx] > lst[largest]:
    largest = right_idx
  if largest != index:
    lst[largest], lst[index] = lst[index], lst[largest]
    heapify(lst, largest, heap_size)

def heap_sort(lst):
  length = len(lst)
  for i in range(length//2-1, -1, -1):
    heapify(lst, i, length)
  for i in range(length-1, 0, -1):
    lst[0], lst[i] = lst[i], lst[0]
    heapify(lst, 0, i)
  return lst

lst = list(map(int, input().split()))
lst = heap_sort(lst)
print(lst)