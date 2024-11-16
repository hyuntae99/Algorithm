def dfs(n):
    global ans
    if n == N:    # N행까지 진행한 경우 경우의수 가능: 성공
        ans += 1
        return

    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0:  # 열/대각선 모두 Q없음
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    ans = 0
    """
    00 01 02 03 
    10 11 12 13
    20 21 22 23
    30 31 32 33
    """
    v1 = [0] * N # 열
    v2 = [0] * (2*N) # / (합이 같음)
    v3 = [0] * (2*N) # \ (차가 같음)
    dfs(0)
    print(f'#{test_case} {ans}')