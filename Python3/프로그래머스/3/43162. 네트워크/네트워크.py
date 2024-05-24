from collections import deque

def solution(n, computers):
    visited = [False] * n
    num_networks = 0
    
    # 모든 컴퓨터에 대해서
    for i in range(n):
        # 방문하지 않았다면
        if not visited[i]:
            bfs(i, n, computers, visited)
            print('끝')
            num_networks += 1
    
    return num_networks

def bfs(start, n, computers, visited):
    queue = deque([start])
    while queue:
        node = queue.popleft() # 현재 노드
        for neighbor in range(n):
            # 현재 노드의 주변 노드가 1이고 방문하지 않을 때
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True # 방문 처리
                queue.append(neighbor) # 인접 노드 큐에 추가