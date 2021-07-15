"Quick Sirt 퀵 정렬"

# 기준값에 해당하는 피벗(pivot)을 기준으로 두 데이터의 키값을 비교하여 위치를 교환하는 정렬 방식
# 오름차순 정렬의 경우, 피벗을 기준으로 작거나 같은 데이터는 왼쪽으로 가도록 하고, 큰 데이터는 오른쪽으로 가도록 함
# 피벗은 전체 데이터 중 가운데 위치한 것이나, 처음 또는 끝에 위치한 것, 별도의 수식을 사용한 것 등 다양한 방법으로 선택 가능
# 퀵 정렬 알고리즘은 원래의 문제를 더 작은 크기의 하위 문제로 쪼개어 해결한다는 특징이 있는 분할 정복 알고리즘에 해당함
# 시간 복잡도는 평균적으로 O(nlogn), 최악의 경우 O(n²)

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]                                          # 비교할 중간값 선택
    left, right, equal = [], [], []                                     # 중값값을 기준으로 작은 값과 큰 값, 같은 값을 넣을 배열(리스트) 생성
    for num in lst:
        if num < pivot:
            left.append(num)                                            # 비교값보다 작은 값을 삽입
        elif num > pivot:
            right.append(num)                                           # 비교값보다 큰 값을 삽입
        else:
            equal.append(num)                                           # 비교값과 동일한 값을 삽입
    return quick_sort(left) + quick_sort(equal) + quick_sort(right)     # 생성한 리스트를 크기 순으로 결합

lst = list(map(int, input().split()))                                   # 정렬할 리스트 입력
lst = quick_sort(lst)                                                   # 퀵 정렬 수행
print(lst)                                                              # 결과 출력