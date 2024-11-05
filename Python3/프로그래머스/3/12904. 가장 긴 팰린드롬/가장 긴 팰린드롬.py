def solution(s):
    n = len(s)
    answer = 1  # 최소 길이는 1 (한 글자)

    # DP 테이블 초기화
    dp = [[False] * n for _ in range(n)]

    # 길이 1인 부분 문자열은 모두 팰린드롬
    for i in range(n):
        dp[i][i] = True

    # 길이 2 이상 부분 문자열 검사
    for length in range(2, n + 1):  # 부분 문자열의 길이
        for start in range(n - length + 1):
            end = start + length - 1

            # 양 끝 문자가 같고, 길이가 2이거나 내부 부분 문자열이 팰린드롬인 경우
            if s[start] == s[end] and (length == 2 or dp[start + 1][end - 1]):
                dp[start][end] = True
                answer = max(answer, length)

    return answer
