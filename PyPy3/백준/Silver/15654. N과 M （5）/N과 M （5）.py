def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(N):
        if not v[i]:
            v[i] = 1
            dfs(n + 1, lst + [nums[i]])
            v[i] = 0


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []
v = [0] * (N + 1)
dfs(0, [])

for a in ans:
    print(*a)