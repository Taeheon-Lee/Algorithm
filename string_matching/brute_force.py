"Brute Force 직선적 알고리즘"

# 텍스트의 매 위치에서 패턴 일치가 발생하는지를 조사하는 가장 간단한 형태의 알고리즘
# 본문 문자열을 처음주터 끝까지 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작
# 텍스트 문자열의 길이를 n이라 하고 패턴 문자열의 길이를 m이라 하면 n*m번의 비교를 수행 즉, 시간 복잡도는 O(nm)

def brute_force(P, T):
    M = len(P)                  # 패턴의 길이
    N = len(T)                  # 텍스트의 길이
    i, j = 0, 0
    while i < N and j < M:
        if T[i] != P[j]:        # 매칭 실패 시
            i = i - j           # 시작 자리로 이동
            j = -1              # 패턴 처음 자리로 이동
        i += 1
        j += 1

    if j == M:                  # 매칭 성공 시
        return i - M            # 패턴 시작 자리를 리턴
    else:
        return -1               # 매칭 실패

P = input("Input pattern: ")    # 패턴 입력
T = input("Input String: ")     # 본문(string) 입력
ans = brute_force(P, T)
print("Matching fail" if ans == -1 else ans)