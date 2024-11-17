def solve(N):
    s = set()
    cnt = 0
    while True:
        if len(s) == 10:
            return cnt
        cnum = N * (cnt+1)
        for c in str(cnum):
            s.add(c)
        cnt += 1
        # print(cnum,s)

    return cnt


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    ans = solve(N)
    print(f'#{test_case} {ans*N}')