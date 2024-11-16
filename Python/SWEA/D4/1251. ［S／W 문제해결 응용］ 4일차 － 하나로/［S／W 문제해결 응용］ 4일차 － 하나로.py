import heapq

# 두 좌표 간 거리 제곱과 환경 부담 세율 계산
def calculate_cost(x1, y1, x2, y2, e):
    return e * ((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 우선순위 큐를 사용한 Prim's Algorithm
def prim_mst(n, coordinates, e):
    visited = [False] * n
    pq = [(0, 0)]  # (cost, start_node)
    total_cost = 0
    count = 0

    while pq and count < n:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        total_cost += cost
        count += 1

        for next_node in range(n):
            if not visited[next_node]:
                next_cost = calculate_cost(
                    coordinates[node][0],
                    coordinates[node][1],
                    coordinates[next_node][0],
                    coordinates[next_node][1],
                    e
                )
                heapq.heappush(pq, (next_cost, next_node))

    return total_cost

# 입력 및 실행
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    x_coords = list(map(int, input().split()))
    y_coords = list(map(int, input().split()))
    E = float(input())

    # 좌표를 리스트로 정리
    coordinates = [(x_coords[i], y_coords[i]) for i in range(N)]

    # 최소 환경 부담금 계산
    result = prim_mst(N, coordinates, E)

    # 출력 결과는 소수 첫째 자리에서 반올림하여 정수 출력
    print(f"#{test_case} {round(result)}")
