def solve(arr, N, K):
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 가로와 세로 체크
            if check_row(arr, N, K, i, j):
                cnt += 1
            if check_col(arr, N, K, i, j):
                cnt += 1
    return cnt

# 가로 체크
def check_row(arr, N, K, i, j):
    if j + K <= N:  # 범위를 벗어나지 않는지 확인
        # 전부 1 + 끝부분이 0이거나 경계 + 시작부분이 0이거나 경계
        if all(arr[i][j:j+K]) and (j + K == N or arr[i][j+K] == 0) and (j == 0 or arr[i][j-1] == 0):
            return True
    return False

# 세로 체크
def check_col(arr, N, K, i, j):
    if i + K <= N:  # 범위를 벗어나지 않는지 확인
        col = [arr[i+x][j] for x in range(K)]
        # 전부 1 + 끝부분이 0이거나 경계 + 시작부분이 0이거나 경계
        if all(col) and (i + K == N or arr[i+K][j] == 0) and (i == 0 or arr[i-1][j] == 0):
            return True
    return False

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve(arr, N, K)
    print(f'#{test_case} {ans}')
