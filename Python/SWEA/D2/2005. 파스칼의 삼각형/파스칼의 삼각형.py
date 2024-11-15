def solve(N):
    arr = [[0] * N for i in range(N)]
    for i in range(N):
        arr[i][i] = 1 # 대각선
        arr[i][0] = 1 # 세로

    for i in range(1,N):
        for j in range(1,N):
            if arr[i][j] != 1:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    return arr

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    ans = solve(N)
    print(f'#{test_case}')
    for an in ans:
        for a in an:
            if a != 0:
                print(a, end=' ')
        print()