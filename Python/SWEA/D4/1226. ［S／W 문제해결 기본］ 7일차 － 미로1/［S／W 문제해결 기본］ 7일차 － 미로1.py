from collections import deque

def check(arr):
    for i in range(MAX):
        for j in range(MAX):
            if arr[i][j] == 3:
                return i,j


MAX = 16
def bfs(arr,si,sj,ei,ej):
    q = deque()
    v = [[0] * MAX for _ in range(MAX)]

    q.append((si,sj))
    v[si][sj] = 1

    while q:
        ci,cj = q.popleft()

        if (ci,cj) == (ei,ej):
            return 1

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di,cj+dj
            # 범위내 + 미방문 + 벽 x
            if 0 <= ni < MAX and 0 <= nj < MAX and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni,nj))
                v[ni][nj] = 1

    return 0

T = 10
for _ in range(T):
    test_case = int(input())
    arr = [list(map(int, input())) for _ in range(MAX)]

    ei,ej = check(arr)
    ans = bfs(arr,1,1,ei,ej)
    print(f'#{test_case} {ans}')
