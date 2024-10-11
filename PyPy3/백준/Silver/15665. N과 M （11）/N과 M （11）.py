def dfs(n, lst):
    if n == M:
        ans.append(tuple(lst))  # 리스트를 튜플로 변환하여 저장
        return

    for i in range(N):
        dfs(n + 1, lst + [nums[i]])


N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = []

dfs(0, [])

# 중복을 제거한 후 결과 출력
ans_set = list(set(ans))

for a in sorted(ans_set):
    print(*a)
