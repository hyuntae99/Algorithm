 #           5
 #   4       6        10
 # 3 5 8   5 7 12   9 11 20

from collections import deque

def bfs(s, e):
    q = deque()
    v = [0] * 200001 # 100000까지의 수가 있으므로 x2를 대비하여 최대 수 지정

    q.append(s)
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.popleft()

        if c == e:
            return v[e] - 1

        for n in (c-1, c+1, c*2): # 갈 수 있는 수를 계산
            if 0 <= n <= 200000 and not v[n]:
                ans_bfs.append(n)
                q.append(n)
                v[n] = v[c] + 1 # 노드 단계를 계산

    return -1 # 예외 처리


N, K = map(int, input().split())
ans_bfs = []
ans = bfs(N, K)
print(ans)
