from collections import deque

MAX = 100

def bfs(si,sj,ei,ej):
    v = [[0] * MAX for _ in range(MAX)]
    q = deque()

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()

        if (ci,cj) == (ei,ej):
            return True

        # 좌우 우선 이동
        for di,dj in ((0,-1),(0,1),(1,0)):
            ni,nj = ci+di,cj+dj
            # 범위 내 + 미방문
            if 0 <= ni < MAX and 0 <= nj < MAX and v[ni][nj] == 0 and arr[ni][nj] != 0:
                q.append((ni,nj))
                v[ni][nj] = 1
                break

    return False

T = 10
for _ in range(T):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(MAX)]
    lst = []

    for i in range(MAX):
        if arr[0][i] == 1:
            lst.append((0,i))
        if arr[MAX-1][i] == 2:
            ei,ej = MAX-1,i

    ans = 0
    for si,sj in lst:
        if bfs(si,sj,ei,ej):
            ans = sj
            break

    print(f'#{test_case} {ans}')