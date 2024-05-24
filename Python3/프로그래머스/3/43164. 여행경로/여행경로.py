def solution(tickets):
    from collections import defaultdict

    # 그래프 초기화
    graph = defaultdict(list)
    # 출발지에서 도착지로 갈 수 있는 모든 경로를 그래프에 저장
    for start, end in tickets:
        graph[start].append(end)

    # 도착지 기준으로 알파벳으로 정렬
    for key in graph:
        graph[key].sort()

    route = [] # 여행 경로를 저장할 리스트

    def dfs(node):
        # 더 이상 갈 곳이 없을 때까지 탐색
        while graph[node]:
            next_node = graph[node].pop(0)  # 알파벳 순서로 도착지 선택
            dfs(next_node)  # 다음 도착지로 재귀 호출
        route.append(node)  # 마지막 경로부터 추가

    # "ICN"에서 시작
    dfs("ICN")
    
    # 경로를 뒤집어서 반환 
    return route[::-1]