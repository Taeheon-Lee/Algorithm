"KMP 알고리즘"

# Knuth, Morris, Pratt 세 명의 이니셜을 따서 만든 알고리즘
# 검색을 왼쪽부터 시작해서 오른쪽으로 이동해가며 직접 비교해가는 방식이지만, 비교가 필요 없는 부분은 스킵하고 필요한 부분은 비교하는 융통성 있는 알고리즘
# 핵심은 패턴의 각 위치에 대한 매칭이 실패했을 때, 돌아갈 곳을 알려주는 일차원 배열을 준비하고 이를 이용해 텍스트를 훑어 나간다는 점
# 중간에 불일치가 발생했을 때, 여러 칸을 옮기게 되어 불필요한 비교를 줄일 수 있음
# 패턴 자체의 정보를 이용하여 이동 위치를 효율적으로 결정 가능
# 불일치가 발생한 텍스트 문자열의 앞부분에 어떤 문자가 있는지를 미리 알고 있으므로 불일치가 발생한 앞부분에 대하여 다시 비교하지 않고 매칭을 수행
# 시간 복잡도는 O(m+n)

def KMPSearch(pat, txt):
    m = len(pat)                                            # 패턴의 길이
    n = len(txt)                                            # 본문 텍스트의 길이

    lps = [0]*m

    computeLPS(pat, lps)                                    # 패턴 내부의 작은 패턴 검사

    i = 0                                                   # 본문 인덱스
    j = 0                                                   # 패턴 인덱스
    while i < n:
        if pat[j] == txt[i]:                                # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
            i += 1
            j += 1
        elif pat[j] != txt[i]:                              # Pattern을 찾지 못한 경우
            if j != 0:                                      # j!=0인 경우는 짧은 lps에 대해 재검사
                j = lps[j-1]
            else:                                           # j==0이면 일치하는 부분이 없으므로 인덱스 증가
                i += 1

        if j == m:                                          # Pattern을 찾은 경우
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]                                    # 이전 인덱스의 lps값을 참조하여 계속 검색

def computeLPS(pat, lps):
    leng = 0                                                # length of the previous longest prefix suffix

    i = 1                                                   # 항상 lps[0]==0이므로 while문은 i==1부터 시작한다.
    while i < len(pat):
        if pat[i] == pat[leng]:                             # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:                                   # 일치하지 않는 경우
                leng = lps[leng-1]                          # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사
            else:                                           # 다시 검사해야 하므로 i는 증가하지 않음
                lps[i] = 0                                  # 이전 인덱스에서도 같지 않았다면 lps[i]는 0 이고 i는 1 증가
                i += 1

txt = 'ABXABABXAB'
pat = 'ABXAB'
KMPSearch(pat, txt)