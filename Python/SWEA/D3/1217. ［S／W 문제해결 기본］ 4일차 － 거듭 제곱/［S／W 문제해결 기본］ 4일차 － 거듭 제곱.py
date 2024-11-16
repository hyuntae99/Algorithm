def solve(n,m,s):
    global ans
    if m == M:
        ans = s
        return
    # print(s)
    solve(n,m+1,s*n)

T = 10
for _ in range(T):
    test_case = int(input())
    N,M = map(int,input().split())
    ans = 0
    solve(N,0,1)
    print(f'#{test_case} {ans}')