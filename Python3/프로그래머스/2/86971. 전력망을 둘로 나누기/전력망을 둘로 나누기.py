from collections import defaultdict, deque

# 넓이 우선 탐색으로 순회한 노드 수 반환
def bfs(graph, start):
    visited = [start]  
    q = deque([start])  # 시작 노드를 큐에 추가
    n = 1  # 방문한 노드의 수를 초기화

    while q:
        node = q.popleft()  # 큐의 앞에서 노드를 꺼냄
        for adjacent in graph[node]:  # 인접한 모든 노드를 순회
            if adjacent not in visited:  # 인접 노드가 방문되지 않았다면
                visited.append(adjacent)  # 방문한 노드로 표시
                q.append(adjacent)  # 인접 노드를 큐에 추가
                n += 1  # 방문한 노드의 수 증가

    return n  # 방문한 총 노드의 수 반환


def solution(n, wires):
    arr = []  

    for i in wires:  # 자를 각 전선을 순회
        graph = defaultdict(list)  # 그래프를 리스트의 딕셔너리로 초기화
        x, y = i  # 자를 전선의 양 끝 노드를 가져옴
        for j in wires:
            if i == j:  # 현재 자를 전선은 건너뜀
                continue
            a, b = j  # 다른 전선의 양 끝 노드를 가져옴
            # 그래프에 간선을 추가 (무방향)
            graph[a].append(b)  
            graph[b].append(a)  
        print(graph)
        n1 = bfs(graph, x)  
        n2 = bfs(graph, y)  
        arr.append(abs(n1 - n2))  # 두 서브트리 크기의 차이를 리스트에 추가

    answer = min(arr) 

    return answer  
