def bfs(si, sj, ei, ej):
    q = []
    v = [[0] * M for _ in range(N)] # 점수판
    q.append((si, sj)) # 시작점
    v[si][sj] = 1 # 시작 점수

    while q:
        ci, cj = q.pop(0)
        
        # 도착한 경우 (항상 도착하므로 오류 처리는 없어도 됨)
        if (ci, cj) == (ei, ej):
            return v[ci][cj]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 4방향에 대해서
            ni, nj = ci + di, cj + dj # 이동 좌표
            # x, y축 범위 안에 들어 있으며, 방문하지 않았고, 길이 있는 경우
            if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]
ans = bfs(0, 0, N-1, M-1)
print(ans)


