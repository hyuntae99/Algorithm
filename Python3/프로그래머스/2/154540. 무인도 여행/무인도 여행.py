def solution(maps):
    
    from collections import deque

    def bfs(si,sj):
        q = deque()
        q.append((si,sj))
        v[si][sj] = 1
        s = int(maps[si][sj]) # 생존 일수

        # 4방향 탐색
        while q:
            ci,cj = q.popleft()
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                ni,nj = ci+di,cj+dj
                # 범위 내 + 방문 x + X가 아님
                if 0 <= ni < N and 0 <= nj < M and not v[ni][nj] and maps[ni][nj] != 'X':
                    q.append((ni,nj))
                    v[ni][nj] = 1
                    s += int(maps[ni][nj])
        ans.append(s)
    
    N = len(maps)
    M = len(maps[0])
    
    v = [[0] * M for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(M):
            # 방문x + X가 아닐 때
            if not v[i][j] and maps[i][j] != 'X':
                bfs(i,j)
                
    if len(ans) == 0:
        return [-1]
    else:
        return sorted(ans)