def solve(arr1,arr2):
    a,b = len(arr1),len(arr2)
    cnt = b-a+1
    mx = 0
    
    for idx in range(cnt):
        s = 0
        nb = arr2[idx:idx+a]
        for i in range(a):
            s += nb[i]*arr1[i]
        mx = max(s,mx)

    return mx

T = int(input())
for test_case in range(1,T+1):
    N,M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if N < M:
        ans = solve(arr1,arr2)
    else:
        ans = solve(arr2,arr1)
    print(f'#{test_case} {ans}')