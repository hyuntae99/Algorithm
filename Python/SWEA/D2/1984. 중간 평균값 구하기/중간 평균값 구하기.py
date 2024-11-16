def solve(arr):
    arr.sort()
    avg = round(sum(arr[1:-1]) / (len(arr)-2))
    return avg

T = int(input())
for test_case in range(1,T+1):
    arr = list(map(int,input().split()))
    ans = solve(arr)
    print(f'#{test_case} {ans}')