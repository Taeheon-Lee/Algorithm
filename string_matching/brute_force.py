def brute_force(P, T):
    M = len(P)              # 패턴의 길이
    N = len(T)              # 텍스트의 길이
    i, j = 0, 0
    while i < N and j < M:
        if T[i] != P[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == M:
        return i - M
    else:
        return i

P = input()                 # 패턴 입력
T = input()                 # 전체 텍스트(string) 입력
print(brute_force(P, T))