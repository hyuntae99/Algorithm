from collections import deque

# 하나로 인접하는가?
def bfs(si, sj):
    q = deque()
    q.append((si,sj))
    vv = [[0] * 5 for _ in range(5)]
    vv[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)): # 4방향으로 탐색
            ni, nj = ci + di, cj + dj
            # 범위 안에 해당하고 방문하지 않았으며 칠공주인 위치
            if 0 <= ni < 5 and 0 <= nj < 5 and not vv[ni][nj] and v[ni][nj] == 1:
                q.append((ni,nj))
                vv[ni][nj] = 1
                cnt += 1

    return cnt == 7 # 칠공주가 모두 인접하면 True

# 처음 만나는 칠공주에 대해서 인접 판단
def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i, j)

def dfs(n, cnt, scnt):
    global ans

    if cnt > 7: # 칠공주 이미 완성
        return

    if n == 25: # 마지막 학생까지 탐색
        if cnt == 7 and scnt > 3: # 칠공주 완성 + S파가 우세함
            if check(): # 해당 칠공주가 모두 인접하는가?
                ans += 1
        return

    v[n // 5][n % 5] = 1 # 학생 번호에 대한 2차원 위치 (방문 처리)
    dfs(n + 1, cnt + 1, scnt + int(arr[n // 5][n % 5] == 'S')) # S파를 포함하는 경우
    v[n // 5][n % 5] = 0 # 방문 처리 해제

    dfs(n + 1, cnt, scnt) # 포함 x


arr = [input() for _ in range(5)]
ans = 0
v = [[0]*5 for _ in range(5)]
# 학생번호(0~24), 포함학생수, 다솜파학생수
dfs(0, 0, 0)
print(ans)
