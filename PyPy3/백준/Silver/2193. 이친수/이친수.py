N = int(input())
dp = [[0] * 2 for _ in range(N+1)]
dp[1][1] = 1

for i in range(2, N+1):
    dp[i][0] = sum(dp[i-1]) # 0으로 끝난 경우 -> 둘 다 가능
    dp[i][1] = dp[i-1][0] # 1로 끝난 경우 -> 0만 가능

# for a in dp:
#     print(*a)

print(sum(dp[N]))