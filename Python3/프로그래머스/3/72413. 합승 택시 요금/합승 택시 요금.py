import heapq
INF = float('inf')

def dijkstra(start, n, graph):
    distances = [INF] * (n + 1)
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

def solution(n, s, a, b, fares):
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for u, v, cost in fares:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    # 다익스트라로 최단 거리 계산
    dist_from_s = dijkstra(s, n, graph)  # s에서 각 지점까지의 최단 거리
    dist_from_a = dijkstra(a, n, graph)  # a에서 각 지점까지의 최단 거리
    dist_from_b = dijkstra(b, n, graph)  # b에서 각 지점까지의 최단 거리
    
    # 최소 비용 계산
    min_cost = INF
    for i in range(1, n + 1):
        # s -> i (합승) + i -> a + i -> b
        min_cost = min(min_cost, dist_from_s[i] + dist_from_a[i] + dist_from_b[i])
    
    return min_cost
