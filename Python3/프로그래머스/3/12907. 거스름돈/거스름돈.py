def solution(n, money):
    # DP 배열 초기화: dp[i]는 금액 i를 만들 수 있는 경우의 수
    dp = [0] * (n + 1)
    dp[0] = 1  # 금액 0을 만드는 방법은 1가지 (동전 사용 X)

    # 각 동전 사용하여 금액을 만들 수 있는 방법의 수 업데이트
    for coin in money:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
        # print(dp)
    
    # 결과 반환 (방법의 수를 1,000,000,007로 나눈 나머지)
    return dp[n] % 1000000007
