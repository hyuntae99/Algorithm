# 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다.
from collections import deque

def bfs(tlst):
    # 벽 막기
    for i, j in tlst:
        arr[i][j] = 1

    cnt = CNT - 3 # 남은 빈칸 개수

    q = deque()
    w = [[0] * M for _ in range(N)]

    # 바이러스 위치
    for ti, tj in virus:
        q.append((ti,tj))
        w[ti][tj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)): # 4방향 탐색
            ni, nj = ci + di, cj + dj
            # 범위 내 + 미방문 + 빈 땅 => 바이러스 확산
            if 0 <= ni < N and 0 <= nj < M and not w[ni][nj] and arr[ni][nj] == 0:
                q.append((ni, nj))
                w[ni][nj] = 1
                cnt -= 1

    # 벽 해제 (다음 케이스를 위해서)
    for i, j in tlst:
        arr[i][j] = 0

    return cnt

def dfs(n, tlst):
    global ans
    if n == 3: # 벽을 모두 세운 경우
        ans = max(ans, bfs(tlst)) # 기존 값과 새로운 값 비교
        return

    for i in range(CNT): # 모든 빈칸에 대해서 탐색
        if not v[i]:
            v[i] = 1
            dfs(n + 1, tlst + [lst[i]]) # 벽을 세울 조합을 구성
            v[i] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

lst = [] # 빈칸
virus = [] # 바이러스

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            lst.append((i,j))
        elif arr[i][j] == 2:
            virus.append((i,j))

CNT = len(lst) # 빈칸의 총 개수
v = [0] * CNT
ans = 0

dfs(0, [])
print(ans)
