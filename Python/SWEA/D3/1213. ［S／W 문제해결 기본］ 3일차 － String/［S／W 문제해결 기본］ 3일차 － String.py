def solve(arr, target):
    return arr.count(target)

T = 10
for _ in range(T):
    test_case = int(input())
    target = str(input())
    arr = str(input())
    ans = solve(arr, target)
    print(f'#{test_case} {ans}')