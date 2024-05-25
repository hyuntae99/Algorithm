def solution(m, n, puddles):
    MOD = 1000000007
    
    # DP 배열 초기화
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    # 웅덩이 위치 설정
    for puddle in puddles:
        x, y = puddle
        dp[y-1][x-1] = -1
    
    for i in range(n):
        for j in range(m):
            # 웅덩이인 경우
            if dp[i][j] == -1:  
                dp[i][j] = 0
            else:
                # 위쪽 경로에서 추가
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                # 왼쪽 경로에서 추가
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    print(dp)
    return dp[n-1][m-1]