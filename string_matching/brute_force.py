"Brute Force 직선적 알고리즘"

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
T = input("Input String: ")     # 전체 텍스트(string) 입력
ans = brute_force(P, T)
print("Matching fail" if ans == -1 else ans)