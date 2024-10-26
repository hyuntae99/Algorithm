# 하, 우, 대각선 방향
di = [1, 0, -1]
dj = [0, 1, -1]

def solution(n):
    # 2차원 배열을 생성
    arr = [[0] * i for i in range(1, n + 1)]
    
    # 시작 위치 및 초기 숫자 설정
    num = 1
    i, j = 0, 0
    direction = 0  # 현재 진행 방향 (0: 하, 1: 우, 2: 대각선)

    # n개의 숫자를 채울 때까지 반복 
    for _ in range(n * (n + 1) // 2):
        arr[i][j] = num  # 현재 위치에 숫자를 채움
        num += 1
        
        # 다음 위치를 미리 계산
        ni, nj = i + di[direction], j + dj[direction]
        
        # 배열 범위를 벗어나거나 이미 값이 채워져 있는 경우 방향 전환
        if ni < 0 or ni >= n or nj < 0 or nj >= len(arr[ni]) or arr[ni][nj] != 0:
            direction = (direction + 1) % 3  # 방향을 변경
            ni, nj = i + di[direction], j + dj[direction]  # 새 방향으로 이동
        
        # 위치 업데이트
        i, j = ni, nj
    
    # 2차원 배열을 1차원 리스트로 변환하여 반환
    return sum(arr, [])
