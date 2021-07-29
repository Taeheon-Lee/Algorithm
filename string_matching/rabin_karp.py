"Rabin-Karp 라빈-카프 알고리즘"

# 패턴의 해시값과 본문 안에 있는 하위 문자열의 해시값만을 비교하여 탐색
# 즉 문자열 패턴을 수치로 바꾸어 문자열의 비교를 수치 비교로 전환해 매칭하는 방법
# 해싱은 인덱스만 계산하면 바로 값을 참조할 수 있기 떄문에 연산 속도가 O(1)로 매우 빠름
# 해싱 값은 문자열이 달라도 같을 수 있기 때문에 해싱 값이 같을 경우, 단순 비교를 시작
# 따라서 최악의 경우, 해싱이 모두 같고 매칭이 다른 경우가 발생할 수 있어 시간 복잡도가 O(mn)
# 평균적인 시간 복잡도는 선형에 가까운 O(m+n)으로 매우 빠름

def rabin_karp(T, P):
    n = len(T)                          # 본문의 길이
    m = len(P)                          # 패턴의 길이
    hash_p = hash(P)                    # 패턴의 해시 값
    for i in range(n+1-m):              # 처음부터 탐색 시작
        if hash_p == hash(T[i:i+m]):    # 해시값이 서로 같은 경우, 단순 비교 시작
            cnt = 0                     # 매칭을 위한 인덱스 초기화
            while cnt != m:             # 매칭 확인 시작
                if P[cnt] != T[i+cnt]:  # 매칭 실패 경우
                    break
                cnt += 1
            if cnt == m:                # 매칭 성공 경우
                return i                # 처음 위치 리턴
            else:
                continue                # 실패 시 다음으로 넘어가 탐색
    return -1                           # 탐색 실패

P = input("Input pattern: ")    # 패턴 입력
T = input("Input String: ")     # 본문(string) 입력
ans = rabin_karp(T, P)
print("Matching fail" if ans == -1 else ans)