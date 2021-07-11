"Selection Sort"

# 정렬되지 않은 데이터들에 대해 가장 작은 데이터를 찾아 가장 앞의 데이터와 교환해가는 방식
# 입력 값에 상관 없이 모든 곳을 탐색하기 때문에 입력에 민감하지 않고 항상 일정한 시간 복잡도를 가짐
# 비교 횟수에 비해 교환 횟수는 상당히 적어 교환이 많이 이루어져야 하는 데이터 상태에 효율적
# 시간 복잡도는 O(n²)

def swap(lst, x, y):
    "입력 받은 2개의 리스트 자리를 서로 교환"
    tmp = lst[x]
    lst[x] = lst[y]
    lst[y] = tmp
    return lst

def selection_sort(lst):
    "선택 정렬 함수"
    length = len(lst)
    for i in range(length-1):
        least = i
        for j in range(i+1, length):        # 최솟값 탐색
            if lst[j] < lst[least]:
                least = j
        if i != least:                      # 최솟값이 자기 자신이면 자료 이동을 하지 않음
            lst = swap(lst, i, least)
    return lst

lst = list(map(int, input().split()))       # 정렬할 리스트 입력

selection_sort(lst)                         # 선택 정렬 수행
print(lst)                                  # 결과 출력