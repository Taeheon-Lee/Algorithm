"Counting Sort 계수 정렬"

# 데이터들을 비교하지 않고 데이터가 등장한 횟수를 세서 그 기준으로 정렬하는 방법
# 키값(데이터, k)의 범위를 알고 있을 때, 적용 가능하며 작은 정수 범위에 있을 떄 적용 가능
# 선형 시간에 정렬하는 효율적인 알고리즘
# 같은 키값을 갖는 데이터가 여러 개일 때 효과적이며 O(n)의 빠른 시간복잡도를 가짐 (퀵 정렬보다 빠름)
# 정렬의 하기 위해 길이 n의 배열 하나와 계수를 위한 길이 k의 배열 하나가 필요하기 때문에 공간복잡도는 O(n+k)

def counting_sort(lst, k):
    count_lst = [0] * k
    sorted_lst = [0] * len(lst)

    for i in range(len(lst)):
        count_lst[lst[i]] += 1                      # 계수 Counting 입력

    for i in range(len(count_lst)-1):
        count_lst[i+1] += count_lst[i]              # 각 계수를 누적 시켜 적용

    for i in range(len(lst)-1, -1, -1):             # 계수 정렬에서는 뒤에서 비교를 시작하나 앞에서 비교를 시작하나 관계가 없으나, 이후에 사용하는 기수 정렬을 사용하기 위해 뒤에서부터 체크
        sorted_lst[count_lst[lst[i]]-1] = lst[i]    # 누적값을 사용하기 때문에 count_lst 계수의 값에 대응하는 sorted_lst 위치에 값을 그대로 대입
        count_lst[lst[i]] -= 1                      # 누적값을 사용하기 때문에 해당 위치에 값을 입력 후, 값을 1 감소시켜야 함

    return sorted_lst

lst = list(map(int, input().split()))               # 정렬할 리스트 입력
lst = counting_sort(lst, 10)                        # 범위를 미리 알고 있다는 가정하에 사용하는 알고리즘이기 때문에 범위값 k를 입력
print(lst)                                          # 정렬된 리스트 출력