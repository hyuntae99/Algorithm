def solve():
    global arr
    for oper in operation[1:]:
        # print(arr)
        op = oper.strip().split()
        idx, ln = int(op[0]), int(op[1])
        lst = op[2:]
        for o in lst[::-1]:
            arr.insert(idx,o)

T = 10
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(str, input().split()))

    M = int(input())
    operation = list(map(str, input().split('I')))

    solve()

    print(f'#{test_case}', end=' ')
    print(*arr[:10])