"Merge Sort 합병 정렬"

# 기존 데이터를 원소의 개수가 동일한 부분 리스트로 분할하고 분할 된 각 부분리스트를 합병하여 정렬하는 방식
# 원래의 문제를 더 작은 크기의 하위 문제로 쪼개어 해결한다는 특징이 있는 분할 정복 알고리즘에 해당함
# n개의 정렬된 데이터 집합을 결합하는 경우 n-way 합병이라 함
# 시간 복잡도는 최선, 평균, 최악의 경우 모두 O(nlogn)으로 매우 효율적인 정렬 방식임

# 방식 1
# Slice Notation을 이용한 방식으로 간단한 코드 작성이 가능하나 slice 실행 시, 배열의 복제가 발생하기 때문에 메모리 사용 효율은 좋지 않음

def merge_sort(lst):
    if len(lst) < 2:                        # 재귀 함수 수행을 위한 탈출 조건 생성
        return lst

    mid = len(lst) // 2                     # 기존 리스트의 중간 위치 지정
    left = merge_sort(lst[:mid])            # 왼쪽 리스트로 분할
    right = merge_sort(lst[mid:])           # 오른쪽 리스트로 분할

    ret = []                                # return할 정렬된 리스트 생성
    i, j = 0, 0
    while i < len(left) and j < len(right): # 각 인덱스는 리스트의 크기를 넘어서면 안됨
        if left[i] < right[j]:              # 왼쪽 리스트와 오른쪽 리스트를 비교하여 정렬된 리스트에 작은 순서대로 삽입
            ret.append(left[i])             # 왼쪽 값이 작을 경우, 왼쪽 값 리스트 값 하나를 정렬된 리스트에 삽입
            i += 1                          # 다음 위치로 이동하여 비교할 왼쪽 값을 선택
        else:
            ret.append(right[j])            # 오른쪽 값이 작을 경우, 오른쪽 값 리스트 값 하나를 정렬된 리스트에 삽입
            j += 1                          # 다음 위치로 이동하여 비교할 오른쪽 값을 선택
    if i < len(left):                       
        ret += left[i:]                     # 비교를 완료한 뒤, 남은 리스트 값을 모두 정렬된 리스트 마지막에 삽입
    if j < len(right):
        ret += right[j:]                    # 비교를 완료한 뒤, 남은 리스트 값을 모두 정렬된 리스트 마지막에 삽입
    return ret

lst = list(map(int, input().split()))       # 정렬할 리스트 값 입력
lst = merge_sort(lst)                       # 합병 정렬 수행
print(lst)                                  # 정렬된 리스트

# 방식 2
# 기존 방식에서 최적화한 방식으로 Slice Notation을 사용하지 않고 index를 이용하여 처리한 방법

def merge(left, mid, right):
    i, j = left, mid+1                      # 왼쪽 시작과, 오른쪽 시작 위치 지정
    k = left                                # 왼쪽 시작 시점부터 정렬을 하기 때문에 왼쪽 시작 지점을 정렬 시작 지점으로 지정
    sorted_lst = []                         # 정렬된 값을 넣을 리스트 생성
    while i <= mid and j <= right:          # 각 인덱스는 자신의 구역을 넘어서는 안됨
        if lst[i] < lst[j]:                 # 왼쪽 리스트와 오른쪽 리스트를 비교하여 정렬된 리스트에 작은 순서대로 삽입
            sorted_lst.append(lst[i])       # 왼쪽 값이 작을 경우, 왼쪽 값 리스트 값 하나를 정렬된 리스트에 삽입
            i += 1                          # 다음 위치로 이동하여 비교할 왼쪽 값을 선택
        else:
            sorted_lst.append(lst[j])       # 오른쪽 값이 작을 경우, 오른쪽 값 리스트 값 하나를 정렬된 리스트에 삽입
            j += 1                          # 다음 위치로 이동하여 비교할 오른쪽 값을 선택
  
    while i <= mid:
        sorted_lst.append(lst[i])           # 비교를 완료한 뒤, 남은 리스트 값을 모두 정렬된 리스트 마지막에 삽입
        i += 1
    while j <= right:
        sorted_lst.append(lst[j])           # 비교를 완료한 뒤, 남은 리스트 값을 모두 정렬된 리스트 마지막에 삽입
        j += 1
    for elem in sorted_lst:
        lst[k] = elem                       # 정렬된 리스트의 값을 정렬 시작 위치부터 하나씩 변경하며 삽입
        k += 1

def merge_sort(left, right):
    if left < right:                        # 왼쪽 인덱스와 오른쪽 인덱스가 교차할 때까지 재귀 수행
        mid = (left + right) // 2           # 기존 리스트의 중간 위치 지정
        merge_sort(left, mid)               # 처음부터 중간까지 합병 정렬 수행
        merge_sort(mid+1, right)            # 중간부터 끝까지 합병 정렬 수행
        merge(left, mid, right)             # 처음, 중간, 끝을 합병

lst = list(map(int, input().split()))       # 정렬할 리스트 값 입력
merge_sort(0, len(lst)-1)                   # 합병 정렬 수행
print(lst)                                  # 정렬된 리스트