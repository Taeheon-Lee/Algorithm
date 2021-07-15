"Bubble Sort 버블 정렬"

# 서로 이웃한 데이터들을 비교하며 가장 큰 데이터를 가장 뒤로 보내며 정렬하는 방식
# 마치 거품 방울(bubble)을 물 위로 하나씩 떠올리는 것과 비슷한 모양
# 버블 정렬을 매우 단순하지만 정렬할 데이터가 많은 경우에는 수행시간이 많이 걸림 "n(n-1)/2 번 수행"
# 시간 복잡도는 O(n²)

def bubble_sort(lst):
    "버블 정렬 함수"
    length = len(lst)                       # 리스트 길이
    for i in range(length-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:           # j 번째보다 j+1 번째 요소가 작을 경우 교환
                lst[j], lst[j+1] = lst[j+1], lst[j]

lst = list(map(int, input().split()))       # 정렬할 리스트 입력

bubble_sort(lst)                            # 버블 정렬 수행
print(lst)                                  # 결과 출력