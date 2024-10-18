N = int(input())

# [-1] 0 1 2 3 ... 8 9 [10]
#   0  1 2 3 4 ... 9 10 11
dp = [[0] * 12 for _ in range(N+1)]
dp[1][2:-1] = [1] * 9

for i in range(2, N+1):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

# for a in dp:
#     print(*a)

print(sum(dp[N]) % 1000000000)
