N = int(input())

# 0(배치x) 1 2
dp = [[0] * 3 for _ in range(N+1)]
dp[1] = [1] * 3

for i in range(2, N+1):
    d_sum = sum(dp[i-1]) % 9901
    dp[i][0] = d_sum # 배치x라서 다 가능
    dp[i][1] = d_sum - (dp[i-1][1] % 9901) # 1에 놓기 위해서 전에 1에 놓으면 안됨
    dp[i][2] = d_sum - (dp[i-1][2] % 9901) # 2에 놓기 위해서 전에 2에 놓으면 안됨

# for a in dp:
#     print(*a)

print(sum(dp[N]) % 9901)