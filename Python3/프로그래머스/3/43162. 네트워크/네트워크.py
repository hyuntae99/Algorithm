from collections import deque

def solution(n, computers):
    v = [0] * n
    num_networks = 0
    
    # 모든 컴퓨터에 대해서
    for i in range(n):
        # 방문하지 않았다면
        if not v[i]:
            bfs(i, n, computers, v)
            num_networks += 1
    
    return num_networks

def bfs(start, n, computers, v):
    q = deque()
    q.append(start)
    v[start] = 1
    while q:
        c = q.popleft() # 현재 노드
        for i in range(n):
            # 현재 노드의 주변 노드가 1이고 방문하지 않을 때
            if computers[c][i] == 1 and not v[i]:
                v[i] = True # 방문 처리
                q.append(i) # 인접 노드 큐에 추가