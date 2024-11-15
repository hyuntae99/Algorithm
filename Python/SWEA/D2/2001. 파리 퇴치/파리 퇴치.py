def solve():
    mx = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            mx = max(mx, attack(i,j))
    return mx

def attack(ci,cj):
    cnt = 0
    for i in range(ci,ci+M):
        for j in range(cj,cj+M):
            cnt += arr[i][j]
    return cnt

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve()
    print(f'#{test_case} {ans}')