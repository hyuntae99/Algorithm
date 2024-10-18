N = int(input())

dp = [0] * (1001) # N+1로 하면 1일 때 런타임 에러
dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 10007

print(dp[N])

