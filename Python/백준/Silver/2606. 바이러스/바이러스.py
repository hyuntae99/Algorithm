def bfs(c):
    q = [] # 큐 생성
    q.append(c)
    ans_bfs.append(c)
    v[c] = 1 # 방문 처리

    while q:
        s = q.pop(0)
        for n in adj[s]: # 인접한 노드 중
            if not v[n]: # 방문하지 않은 노드로
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1


N = int(input()) # 컴퓨터 수
M = int(input()) # 간선 수

adj = [[] for _ in range(N+1)] # 인접 행렬

# 양방향 간선 등록
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

v = [0] * (N+1) # 정점에 대한 방문 배열
ans_bfs = []
bfs(1) # 1번 컴퓨터에서 순회 시작
print(len(ans_bfs)-1)



