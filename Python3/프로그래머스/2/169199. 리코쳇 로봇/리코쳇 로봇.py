# 하, 상, 우, 좌
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def solution(board):
    from collections import deque
    
    def bfs(si, sj, ei, ej):
        q = deque()  # (현재 위치 i, j, 이동 횟수)
        q.append((si, sj, 0))
        v[si][sj] = 1

        while q:
            ci, cj, cnt = q.popleft()
            
            # 종료 조건: 도착점에 도달한 경우
            if (ci, cj) == (ei, ej):
                return cnt
            
            # 4방향 탐색
            for d in range(4):
                ni, nj = ci, cj
                
                # 한 방향으로 끝까지 이동
                while True:
                    ni += di[d]
                    nj += dj[d]
                    
                    # 범위를 벗어나거나 장애물인 경우 멈춤
                    if not (0 <= ni < N and 0 <= nj < M) or board[ni][nj] == 'D':
                        ni -= di[d]
                        nj -= dj[d]
                        break

                # 미방문이면 다음 탐색 좌표로 추가
                if not v[ni][nj]:
                    v[ni][nj] = 1
                    q.append((ni, nj, cnt + 1))
        
        # 도착점에 도달하지 못한 경우
        return -1

    N = len(board)
    M = len(board[0])
    v = [[0] * M for _ in range(N)]

    # 출발점과 도착점 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                si, sj = i, j
            elif board[i][j] == 'G':
                ei, ej = i, j
    
    # BFS를 통해 결과 구하기
    return bfs(si, sj, ei, ej)
