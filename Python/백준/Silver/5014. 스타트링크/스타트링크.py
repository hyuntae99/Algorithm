from collections import deque

def bfs(s, e):
    q = deque()
    v = [0] * (F+1)

    v[s] = 1
    q.append(s)
    ans_bfs.append(s)

    while q:
        c = q.popleft()

        if c == e:
            return v[e] - 1

        for n in (c+U, c-D):
            if 1 <= n <= F and not v[n]:
                q.append(n)
                v[n] = v[c] + 1
                ans_bfs.append(n)

    return -1


F, S, G, U, D = map(int, input().split()) # 최대 층, 현재 층, 스타트 링크 위치, 위층, 아래층
ans_bfs = []
ans = bfs(S, G)

if ans == -1:
    print("use the stairs")
else:
    print(ans)