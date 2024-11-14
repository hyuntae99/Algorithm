def inord(n):
    if n <= N:
        inord(n * 2) # 왼쪽
        ans.append(lst[n])
        inord(n * 2 + 1) # 오른쪽


# T = int(input())
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    lst = [0] * (N + 1)
    for i in range(1, N + 1):
        tlst = input().split()
        lst[i] = tlst[1]

    ans = []
    inord(1)
    print(f'#{test_case} {"".join(ans)}')