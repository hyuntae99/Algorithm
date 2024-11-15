from collections import deque

def bfs(si, sj, ei, ej):
    inf = float('inf')
    v = [[inf] * N for _ in range(N)]
    q = deque()

    q.append((si, sj))
    v[si][sj] = 0

    while q:
        ci, cj = q.popleft()

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            # 범위 내 + 미방문 + 더 최소가 가능한 경우
            if 0 <= ni < N and 0 <= nj < N:
                mn = v[ci][cj] + arr[ni][nj]
                if v[ni][nj] > mn:
                    v[ni][nj] = mn
                    q.append((ni, nj))

    return v[ei][ej]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    ans = bfs(0, 0, N - 1, N - 1)

    print(f'#{test_case} {ans}')

