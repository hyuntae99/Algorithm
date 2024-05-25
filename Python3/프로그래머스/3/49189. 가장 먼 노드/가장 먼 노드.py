import collections
def solution(n, edge):
    answer = 0
    graph = collections.defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [-1] * (n + 1)
    visited[1] = 0

    # BFS 시작
    queue = collections.deque([1]) # 1번 노드부터 시작
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == -1:  # 방문하지 않은 인접 노드일때
                visited[neighbor] = visited[current] + 1 # 방문 처리 및 거리 계산
                queue.append(neighbor) # 큐에 추가
                
    # 가장 먼 노드의 거리 찾기
    max_visited = max(visited)
    
    # 가장 먼 노드의 개수 세기
    answer = visited.count(max_visited)
    return answer