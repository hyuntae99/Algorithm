def solve(N):
    s = 0
    for num in range(1,N+1):
        if num % 2 == 1:
            s += num
        else:
            s -= num
    return s


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    ans = solve(N)

    print(f'#{test_case} {ans}')