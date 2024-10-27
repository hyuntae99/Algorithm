import heapq

# 다익스트라 알고리즘 구현
def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]  # 각 마을에 연결된 경로를 저장할 그래프 초기화
    dist = [float('inf')] * (N + 1)  # 각 마을까지의 최단 거리를 무한대로 초기화
    dist[1] = 0  # 출발 마을(1번 마을)의 거리는 0으로 설정

    # 주어진 도로 정보를 그래프에 추가
    for u, v, w in road:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 우선순위 큐를 사용한 다익스트라 알고리즘
    queue = [(0, 1)]  # (거리, 마을 번호)로 초기화
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        
        # 이미 처리된 경로는 무시
        if current_dist > dist[current_node]:
            continue
        
        # 인접 마을들에 대해 거리 갱신
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:  # 더 짧은 경로 발견 시 업데이트
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    # K 이하의 거리에 도달 가능한 마을의 수를 반환
    return len([i for i in dist if i <= K])