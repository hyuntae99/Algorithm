from collections import deque

def solution(maps):
    # 방향 벡터 (상, 우, 하, 좌)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = 0
    height = len(maps)  # 맵의 높이
    width = len(maps[0])  # 맵의 너비

    # 방문 여부를 저장할 2차원 리스트
    visited = [[0] * width for _ in range(height)]
    # 거리 정보를 저장할 2차원 리스트
    distance = [[0] * width for _ in range(height)]
    # BFS에 사용할 큐
    queue = deque()

    # 시작점 초기화
    visited[0][0] = 1
    distance[0][0] = 1
    queue.append((0, 0))

    while queue:
        now = queue.popleft()  # 큐의 앞에서 현재 노드를 꺼냄

        for i in range(4):  # 4개의 방향을 탐색
            x = now[0] + dx[i]
            y = now[1] + dy[i]

            # 맵의 범위를 벗어나지 않는지 확인
            if 0 <= x <= height - 1 and 0 <= y <= width - 1:
                # 방문하지 않았고 길이 있는 경우
                if visited[x][y] == 0 and maps[x][y] == 1:
                    visited[x][y] = 1  # 방문 표시
                    distance[x][y] = distance[now[0]][now[1]] + 1  # 거리 갱신
                    queue.append((x, y))  # 다음 좌표 큐에 추가
                    
    result = distance[height - 1][width - 1]
    
    # 도달할 수 없을 때
    if result == 0:
        result = -1

    return result  
