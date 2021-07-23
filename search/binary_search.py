"Binary Search 이진 탐색"

# 찾고자 하는 값을 대상 데이터 집합의 중간값과 비교하여 그 대상 범위를 축소시키면서 찾는 방법
# 찾고자 하는 키값을 먼저 가운데 있는 데이터와 비교
# 데이터가 정렬되어 있는 경우에 사용 가능
# 탐색이 한번 진행될 때마다 탐색 범위가 절반으로 줄어들기 때문에 시간 복잡도는 O(log₂n)

def binary_search(lst, low, high, k):
    if low > high:                                  # 끝까지 탐색하여 key값이 존재하지 않을 경우 탐색 실패
        return -1

    middle = (low + high) // 2                      # 리스트의 중간 위치 지정
    
    if k == lst[middle]:                            # 키값이 중간 값과 같은 경우 탐색 성공
        return middle
    elif k < lst[middle]:                           # 키값이 중간 값보다 작은 경우
        return binary_search(lst, low, middle-1)
    else:
        return binary_search(lst, middle+1, high)   # 키값이 중간 값보다 큰 경우

lst = list(map(int, input().split()))               # key를 탐색할 리스트 입력
key = int(input())                                  # key 입력
loc = binary_search(lst, key)                       # 이진 탐색 실행
print("not exist" if loc == -1 else loc)            # 결과 출력

# 항상 배열의 정렬 상태를 유지해야하기 때문에 리스트 내부에 데이터의 삽입 또는 삭제가 발생한 경우, 정렬을 유지하는 추가작업 필요