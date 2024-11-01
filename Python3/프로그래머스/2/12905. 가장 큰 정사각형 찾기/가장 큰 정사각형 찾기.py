def solution(matrix):
    if not matrix or not matrix[0]:
        return 0

    N,M = len(matrix),len(matrix[0])
    d = [[0] * M for _ in range(N)]
    mx = 0  # 가장 큰 정사각형의 한 변의 길이를 추적

    # DP 배열 채우기
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:  # 첫 행이나 첫 열은 그대로 설정
                    d[i][j] = 1
                else:
                    # 위, 왼쪽, 왼쪽 위 값 중 최소값 + 1
                    d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
                
                # 최대 길이 업데이트
                mx = max(mx, d[i][j])

    # 가장 큰 정사각형의 면적을 반환
    return mx ** 2
