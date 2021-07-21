"Bucket Sort 버킷 정렬"

# 여러 개의 버킷에 분류 기준을 부여하고 데이터를 해당 버킷에 분배하고 수집하는 것을 반복하면서 정렬하는 방식
# 적당한 기준으로 나누고 각 부분들을 다른 알고리즘으로 정렬한 뒤, 순서에 맞게 합치는 것
# 각 부분 구간(버킷)은 동일한 버킷 정렬을 사용하여 다시 정렬하거나, 다른 알고리즘을 사용하여 정렬 수행

# 버킷의 구체적인 수행과정은 다음과 같음
# 1) 데이터 n개가 주어졌을 때, 데이터의 범위를 n개로 나누어 이에 해당하는 버킷 생성
# 2) 각각의 데이터를 해당하는 버킷에 분배 (같은 버킷에 해당하는 데이터의 경우, 연결리스트로 연결)
# 3) 비어있지 않은 각 버킷을 정렬
# 4) 버킷 번호순으로 스캔하여 출력

# 버킷 정렬은 거의 혼자서는 사용되지 않으며 다른 알고리즘과 함께 사용
# 최악의 경우는 모든 데이터가 하나의 버킷에 들어가는 경우이며, 최선의 경우는 모두 균등하게 나누어 들어가는 경우
# 평균적인 시간 복잡도는 O(n)

def sorting_fuc(bucket):
    "각 버킷을 정렬하기 위해 사용할 정렬 함수 입력"
    pass

class bucket:                                       # 버킷 생성
    def __init__(self, data):
        self.data = data
        self.next = None

def bucket_sort(lst, base):
    bucket_lst = [0] * len(lst)                     # 리스트의 길이 만큼의 버킷 리스트 생성
    
    for i in range(len(lst)):
        tmp = int(lst[i]*base%10)                   # 데이터를 소수점 첫째 자리수 기준으로 버킷을 나누어 버킷 리스트에 삽입 (입력값은 1미만 0초과의 소수)
        if bucket_lst[tmp] == 0:                    # 기준 버킷 리스트에 버킷이 없을 경우
            bucket_lst[tmp] = bucket(lst[i])        # 버킷을 생성하여 삽입
        else:                                       # 기준 버킷 리스트에 버킷이 있을 경우
            b = bucket_lst[tmp]
            while b.next != None:
                b = bucket_lst[tmp].next            # 버킷의 끝으로 이동
            b.next = bucket(lst[i])                 # 버킷의 끝에 새로운 버킷을 생성하여 연결
    sorted_lst = []                                 # 정렬된 값을 넣을 리스트 생성
    for i in range(len(bucket_lst)):
        if bucket_lst[i] == 0:                      # 버킷 리스트에서 빈 버킷은 통과
            continue
        sorted_bucket = sorting_fuc(bucket_lst[i])  # 각 버킷 영역에 정렬 함수 적용
        while sorted_bucket != None:                # 정렬된 각 버킷 영역을 모두 탐색
            sorted_lst.append(sorted_bucket.data)   # 정렬된 값을 생성한 sorted_lst에 추가
            sorted_bucket = sorted_bucket.next
    return sorted_lst                               # 정렬된 리스트 리턴

lst = list(map(float, input().split()))             # 정렬할 리스트 입력
lst = bucket_sort(lst, 10)                          # 버킷 정렬 수행
print(lst)                                          # 결과 출력