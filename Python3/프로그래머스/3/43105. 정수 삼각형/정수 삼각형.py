def solution(triangle):
    # DP 배열 초기화
    dp = [row[:] for row in triangle]
    
    # 맨 아래에서부터 위로 올라가면서 DP 값을 갱신
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 아래 왼쪽과 아래 오른쪽 중 큰 쪽을 더해서 최신화
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])
    return dp[0][0]