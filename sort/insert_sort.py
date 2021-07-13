"Insert Sort 삽입 정렬"

# 아직 정렬되지 않은 임의의 데이터를 이미 정렬된 부분의 적절한 위치에 삽입해 가며 정렬하는 방식
# 선택된 키값을 앞쪽 데이터들의 키값과 비교하며 자신의 위치를 찾아 삽입하여 정렬
# 최선의 경우, n-1번 비교하면 정렬이 완료
# 최악의 경우, 모든 단계에서 앞에 놓인 데이터들을 전부 이동 "n(n-1)/2 번 수행"
# 시간 복잡도는 최선의 경우 O(n), 최악의 경우 O(n²)

def insert_sort(lst):
    "삽입 정렬 함수"
    length = len(lst)                       # 리스트 길이
    for i in range(1, length):              # 인덱스 0은 이미 정렬된 것으로 볼 수 있음
        key = lst[i]
        for j in range(i-1, -1, -1):
            if lst[j] < key:
                j += 1                      # 중간에 조건에 의하여 탈출할 경우, 키값 삽입을 위하여 인덱스값에 1을 더함
                break
            lst[j+1] = lst[j]               # 키값보다 큰 요소값은 오른쪽으로 이동
        lst[j] = key

lst = list(map(int, input().split()))       # 정렬할 리스트 입력

insert_sort(lst)                            # 삽입 정렬 수행
print(lst)                                  # 결과 출력