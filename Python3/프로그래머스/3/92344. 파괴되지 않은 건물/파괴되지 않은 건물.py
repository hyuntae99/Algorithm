def solution(board, skill):
    n, m = len(board), len(board[0])
    damage = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 각 스킬에 따라 damage 배열에 영향 미치기
    for type, i1, j1, i2, j2, degree in skill:
        if type == 1:  # 공격
            degree = -degree
        # 스킬 범위에 누적합 기록
        damage[i1][j1] += degree
        damage[i1][j2+1] -= degree
        damage[i2+1][j1] -= degree
        damage[i2+1][j2+1] += degree

    # damage 배열을 이용해 누적합 계산
    for i in range(n):
        for j in range(1, m):
            damage[i][j] += damage[i][j-1]
    for j in range(m):
        for i in range(1, n):
            damage[i][j] += damage[i-1][j]
    
    # damage 값을 board에 적용하고 0보다 큰 값 카운트
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += damage[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer
