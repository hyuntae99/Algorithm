MAX = 100

def solve():
    mx = 0

    # 세로합
    for i in range(MAX):
        s = 0
        for j in range(MAX):
            s += arr[j][i]
        mx = max(mx, s)

    # 가로합
    s = 0
    for j in range(MAX):
        s = sum(arr[j])
        mx = max(mx, s)

    # 대각합 (\)
    s = 0
    for i in range(MAX):
        s += arr[i][i]
    mx = max(mx,s)

    # 대각합 (/)
    s = 0
    for i in range(MAX):
        s += arr[MAX-i-1][i]
    mx = max(mx,s)

    return mx


T = 10
for _ in range(T):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(MAX)]

    ans = solve()
    print(f'#{test_case} {ans}')