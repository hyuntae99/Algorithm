def dfs(n, idx, lst):
    if n == M:
        ans.append(tuple(lst))  # 리스트를 튜플로 변환하여 저장
        return

    for i in range(idx, N):
        if not v[i]:
            v[i] = 1
            if len(lst) > 0:
                if lst[-1] <= nums[i]:
                    dfs(n + 1, idx + 1, lst + [nums[i]])
            else:
                dfs(n + 1, idx + 1, lst + [nums[i]])
            v[i] = 0


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []
v = [0] * (N + 1)
dfs(0, 0, [])

# 중복을 제거한 후 결과 출력
ans_set = list(set(ans))

for a in sorted(ans_set):
    print(*a)
