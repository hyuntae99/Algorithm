from collections import deque

# BFS 함수 정의
def bfs(maze, start, target):
    N, M = len(maze), len(maze[0])  # 맵의 크기
    v = [[0] * M for _ in range(N)]  # 방문 여부 저장
    q = deque()
    
    q.append((start[0], start[1], 0)) # 시작점 (i, j, 거리)
    v[start[0]][start[1]] = 1  # 시작점 방문 처리
    
    while q:
        i, j, dist = q.popleft()

        # 목표 지점에 도달했을 때 거리 반환
        if (i, j) == target:
            return dist

        # 네 방향으로 탐색
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = i+di, j+dj

            # 맵의 범위 내에 있고, 벽이 아니며, 방문하지 않은 곳이면 이동
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] != 'X' and not v[ni][nj]:
                v[ni][nj] = 1
                q.append((ni, nj, dist + 1))

    return -1  # 도달할 수 없는 경우

def solution(maps):    
    # 맵을 순회하며 S, L, E의 좌표를 찾음
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            # 시작점
            if maps[i][j] == 'S':
                start = (i, j)
            # 레버
            elif maps[i][j] == 'L':
                lever = (i, j)
            # 출구
            elif maps[i][j] == 'E':
                end = (i, j)
    
    # 1단계: S -> L까지의 최단 거리 구하기 
    to_lever = bfs(maps, start, lever)
    # 도달할 수 없다면
    if to_lever == -1:
        return -1 
    
    # 2단계: L -> E까지의 최단 거리 구하기
    to_end = bfs(maps, lever, end)
    # 도달할 수 없다면
    if to_end == -1:
        return -1
    
    # 최종 결과는 두 경로의 합
    return to_lever + to_end
