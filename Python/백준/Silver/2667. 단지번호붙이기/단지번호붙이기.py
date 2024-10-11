def bfs(si, sj):
    q = []
    v = [[0] * N for _ in range(N)]
    q.append((si, sj))
    v[si][sj] = 1
    maps[si][sj] = 0
    count = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0 , 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and maps[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = 1
                maps[ni][nj] = 0
                count += 1

    return count

N = int(input())
maps = [list(map(int, input())) for _ in range(N)]

sizes = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            size = bfs(i, j)
            sizes.append(size)
            
sizes.sort()
print(len(sizes), *sizes, sep='\n')
