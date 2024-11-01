from collections import deque

# 방향: 하, 상, 우, 좌
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def solution(board):
    N = len(board)
    # 각 위치와 방향에서의 최소 비용을 저장
    cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    q = deque()

    # 초기 상태 설정: 시작 위치에서 각 방향별 초기화
    for d in range(4):
        cost[0][0][d] = 0
        q.append((0, 0, d, 0))  # (행, 열, 방향, 비용)

    while q:
        ci, cj, d, cc = q.popleft()

        # 목적지 도달 시 최소 비용 반환
        if (ci, cj) == (N - 1, N - 1):
            continue

        for i in range(4):
            ni, nj = ci + di[i], cj + dj[i]

            # 범위 검사 및 벽 확인
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0:
                # 직선 도로 비용 100, 코너 비용 500
                new_cost = cc + (100 if i == d else 600)

                # 최소 비용 갱신 시 큐에 추가
                if new_cost < cost[ni][nj][i]:
                    cost[ni][nj][i] = new_cost
                    q.append((ni, nj, i, new_cost))

    # 목적지 (N-1, N-1)에서 모든 방향 중 최소 비용 반환
    return min(cost[N - 1][N - 1])
