from itertools import combinations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# ans = 0
# for com in combinations(arr, 3):
#     if a <= M and abs(M - sum(com)) < abs(M - ans):
#         ans = sum(com)
# print(ans)

# 백트래킹
def dfs(num, cnt):
    if cnt == 3:
        answer.add(num)
        return

    for i in range(N):
        if not v[i]:
            v[i] = 1
            dfs(num+arr[i], cnt+1)
            v[i] = 0

v = [0] * N
answer = set()
dfs(0,0)
ans = 0
for a in answer:
    if a <= M and abs(M - a) < abs(M - ans):
        ans = a
print(ans)

