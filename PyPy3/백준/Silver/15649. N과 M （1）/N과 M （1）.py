def dfs(n, lst):
    # 목표하는 자릿수를 채웠다면 종료
    if n == M:
        ans.append(lst)
        return

    for j in range(1, N + 1):
        if v[j] == 0: # 선택하지 않은 숫자인 경우 추가
            v[j] = 1
            dfs(n + 1, lst + [j])
            v[j] = 0

N, M = map(int, input().split())
ans = []
v = [0] * (N + 1)
dfs(0, [])
for lst in ans:
    print(*lst)