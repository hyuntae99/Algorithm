from collections import deque

# 우 하 좌 상
di = [0, -1, 0 ,1]
dj = [1, 0, -1, 0]

def solve(ci, cj, N):
    arr = [[0] * N for _ in range(N)] # 배열
    d = 0 # 방향
    cnt = N**2 # 목표

    q = deque()
    q.append((ci,cj,d))
    arr[ci][cj] = 1
    num = 2

    while q:
        ci,cj,dr = q.popleft()

        if num == cnt+1:
            return arr

        ni,nj = ci+di[dr],cj+dj[dr]

        # 범위내 + 방문 X
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            q.append((ni,nj,dr))
            arr[ni][nj] = num
            num += 1
        else:
            dr = (dr+1) % 4
            q.append((ci,cj,dr))

    return arr


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ans = solve(0,0,N)
    print(f'#{test_case}')
    for a in ans:
        print(*a)