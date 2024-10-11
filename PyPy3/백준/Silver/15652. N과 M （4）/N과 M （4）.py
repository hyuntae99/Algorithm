def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(1, N + 1):
        if len(lst) > 0:
            if lst[-1] <= i:
                dfs(n + 1, lst + [i])
        else:
            dfs(n + 1, lst + [i])

N, M = map(int, input().split())

ans = []
dfs(0, [])

for a in ans:
    print(*a)