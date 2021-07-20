"Radix Sort 기수 정렬"

# 정렬한 원소의 키값(자리값)을 나타내는 숫자의 자릿수(radix)를 기초로 정렬하는 방법
# 키값의 최하위 자리인 가장 작은 자릿수(least significant digit)부터 최상위 자릿수(most significant digit)까지 차례로 한자리씩 정렬
# 계수 정렬에서 한단계 발전시킨 것으로 각 데이터의 자리수별로 나누어서 순차적으로 계수 정렬을 하는 것 (1의 자리부터)
# 비교 연산자를 사용하지 않으며, 전체 시간 복잡도는 O(dn)
# d는 데이터의 자릿수를 나타내며, 이는 진법에 따라 달라질 수 있으며, 보통 10진수를 넘어가지 않음 (d < 10)

def counting_sort(lst, digit):
  
    sorted_lst = [0] * len(lst)                             # 정렬된 데이터를 삽입하기 위한 리스트 생성
    count_lst = [0] * 10                                    # Counting을 위한 리스트 생성
    
    for i in range(len(lst)):
        count_lst[lst[i]//digit%10] += 1                    # 지정된 자리수 counting   
        
    for i in range(9):
        count_lst[i+1] += count_lst[i]                      # 누적 counting 사용

    for i in range(len(lst)-1, -1, -1):                     # 정렬 과정에 의하여 뒤부터 체크를 시작해야 오름차순 정렬이 가능
        sorted_lst[count_lst[lst[i]//digit%10]-1] = lst[i]  # 누적값을 사용하기 때문에 count_lst 계수의 값에 대응하는 sorted_lst 위치에 값을 그대로 대입
        count_lst[lst[i]//digit%10] -= 1                    # 누적값을 사용하기 때문에 해당 위치에 값을 입력 후, 값을 1 감소시켜야 함
    
    return sorted_lst

def radix_sort(lst):
    maxValue = max(lst)                                     # 모든 수의 자리수를 탐색해야 하기 때문에 리스트 데이터 중 가장 큰수의 자리수 확인
    digit = 1                                               # 1의 자리수부터 탐색하기 위하여 초기화

    while maxValue // digit > 0:                            # 가장 큰수의 자리수를 모두 확인하면 나머지 데이터들의 자리수도 확인하는 것이기 때문에 큰수의 자리수 확인
        lst = counting_sort(lst, digit)                     # 자리수 별로 계수 정렬 수행
        digit *= 10                                         # 자리수를 10배씩 증가

    return lst
 
lst = list(map(int, input().split()))                       # 정렬할 리스트 입력
lst = radix_sort(lst)                                       # 기수 정렬 수행
print(lst)                                                  # 결과 출력