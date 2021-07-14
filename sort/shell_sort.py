"Shell Sort 셸 정렬"

# Donald L. Shell이 제안한 방법으로 삽입 정렬을 보완한 알고리즘
# 매개변수를 설정한 후, 이 매개변수만큼 떨어져 있는 데이터들을 모아 부분리스트를 만든 다음 그 매개변수를 줄여가면서 정렬
# 즉 일정한 간격(Gap)만큼 떨어져 있는 데이터들끼리 부분 리스트를 구성하고 각각의 리스트를 삽입 정렬하는 작업 반복
# 각 단계마다 간격(매개변수, Gap)을 줄여가며, 셸 정렬의 마지막 단계에서는 간격을 1로 설정해야 함
# 셸 정렬 초기에는 부분 리스트의 데이터 개수가 적어 정렬되는 시간이 빠름
# 단계가 진행되면서 간격이 점점 감소하여 리스트의 데이터 개수가 증가하게 되는데 이전에 어느정도 정렬이 되어 있는 상태이기 때문에 수행 시간이 크게 증가하지 않음
# 셸 정렬은 데이터의 특성에 따라 간격을 생성하는 함수를 사용하며, 일반적으로 간격 k는 데이터 개수의 1/2을 사용하고 단계가 진행될 때마다 k의 값을 반으로 줄여감
# 시간 복잡도는 최악의 경우 O(n²), 평균적인 경우 O(n^1.5)

def shell_insert_sort(lst, first, last, gap):
    "셸 정렬을 위한 삽입 정렬 함수, gap 간격의 요소값을 서로 비교"
    for i in range(first+gap, last+1, gap):
        key = lst[i]
        for j in range(i-gap, first-1, -1*gap):
            if lst[j] < key:
                j += gap
                break
            lst[j+gap] = lst[j]
        lst[j] = key
    return lst

def shell_sort(lst):
    length = len(lst)
    if length != 1:
        gap = length // 2                                       # 간격 초기값을 리스트 길이의 절반으로 설정
        while gap > 0:
            for i in range(gap):
                lst = shell_insert_sort(lst, i, length-1, gap)
            gap //= 2                                           # 간격을 단계별로 절반으로 줄임
    return lst

lst = list(map(int, input().split()))                           # 정렬할 리스트 입력

shell_sort(lst)                                                 # 셸 정렬 수행
print(lst)                                                      # 결과 출력