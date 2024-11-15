def solve():
    M = N // 2
    s = 0

    # 위 삼각형
    for i in range(M+1):
        s += sum(arr[M-i][i:N-i])

    # 아래 삼각형
    for i in range(1, M+1):
        s += sum(arr[M+i][i:N-i])

    return s

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    ans = solve()
    print(f'#{test_case} {ans}')