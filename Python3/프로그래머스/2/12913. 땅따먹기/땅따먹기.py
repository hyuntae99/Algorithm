def solution(land):
    N = len(land)
    d = [[0] * 4 for _ in range(N)]
    
    # dp 초기값
    for i in range(4):
        d[0][i] = land[0][i]
    
    for i in range(1, N):
        for j in range(4):
            mx = 0
            for idx in range(4):
                if j != idx: # 바로 연결되는 부분을 제외하고 최댓값 찾기
                    if mx < d[i-1][idx]:
                        mx = d[i-1][idx]
            d[i][j] = mx + land[i][j]

    return max(d[N-1])