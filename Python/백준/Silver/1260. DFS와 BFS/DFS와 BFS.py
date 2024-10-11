def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    v[c] = 1 # 방문 처리

    for n in adj[c]: # 모든 인접 노드에 대해서
        if not v[n]: # 방문하지 않았다면
            dfs(n) # 재귀 처리

def bfs(s):
    q = [] # 큐 생성
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1 # 방문 처리

    while q:
        c = q.pop(0)
        for n in adj[c]:  # 모든 인접 노드에 대해서
            if not v[n]:  # 방문하지 않았다면
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1


N, M, V = map(int, input().split()) # N : 정점, M : 간선, V : 시작점
adj = [[] for _ in range(N+1)] # 인접행렬

# 인접행렬 (양방향 간선)
for i in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 각 인접 노드를 정렬
for i in range(1, N+1):
    adj[i].sort()

v = [0] * (N+1)
ans_dfs = []
dfs(V)
print(*ans_dfs)

v = [0] * (N+1)
ans_bfs = []
bfs(V)
print(*ans_bfs)