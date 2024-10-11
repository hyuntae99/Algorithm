from collections import deque

def bfs(i, j, h):
    q = deque()
    q.append((i,j))
    v[i][j] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)): # 4방향에 대해서
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > h and not v[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 최대 물 높이 계산
max_h = 0
for a in arr:
    max_a = max(a)
    if max_h < max_a:
        max_h = max_a

answer = 0
for h in range(0, max_h): # 물이 점차 높아짐
    cnt = 0
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j] and arr[i][j] > h: # 방문하지 않고 물에 잠기지 않은 영역에 대해서
                bfs(i, j, h)
                cnt += 1
    answer = max(answer, cnt) # 최댓값 최신화

print(answer)