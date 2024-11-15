def solve():
    for _ in range(cnt):
        mx = max(arr)
        mn = min(arr)
        arr[arr.index(mx)] -= 1
        arr[arr.index(mn)] += 1

    mx = max(arr)
    mn = min(arr)
    return mx - mn


T = 10
for test_case in range(1, T+1):
    cnt = int(input())
    arr = list(map(int, input().split()))

    ans = solve()
    print(f'#{test_case} {ans}')