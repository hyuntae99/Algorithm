from collections import deque

def bfs():
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]

    cnt = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    q.append((h,i,j)) # 익은 토마토 위치 추가
                    v[h][i][j] = 1
                elif arr[h][i][j] == 0: # 안익은 토마토 개수 추가
                    cnt += 1

    while q:
        ch, ci, cj = q.popleft()

        # 6방향으로 탐색
        for dh, di, dj in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            nh, ni, nj = ch + dh, ci + di, cj + dj
            # 좌표 안에 위치하며 안익은 토마토이고 방문 처리가 안된 경우
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and v[nh][ni][nj] == 0 and arr[nh][ni][nj] == 0:
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                q.append((nh, ni, nj))
                cnt -= 1 # 안익은 토마토 제거

    if cnt == 0:
        return v[ch][ci][cj] - 1
    else:
        return -1

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)
